from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseRedirect
from urllib.parse import urlparse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Category, Document, Comment
from .forms import DocumentForm, CommentForm
from django.utils.text import slugify

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from django.db.models import Q

from django.http import JsonResponse
import requests, json

# class DocumentList(ListView):
#     model = Document
#     template_name = 'board/document_list.html'
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         if 'slug' in self.kwargs:
#             category = Category.objects.filter(slug=self.kwargs['slug'])
#             categories = category[0].sub_categories.all()
#             if category.exists():
#                 queryset = queryset.filter(category__in=categories).order_by('-id')
#             else:
#                 queryset = queryset.none()
#         return queryset

def document_list(request, category_slug):

    page = int(request.GET.get('page', 1))
    # print(page)

    search_keyword = request.POST.get('search', request.GET.get('search', None))

    # print(category_slug)
    category = Category.objects.filter(slug=category_slug)
    categories = category[0].sub_categories.all()
    if category.exists():
        if categories.exists():
            documents = Document.objects.filter(category__in=categories).order_by('-id')
        else:
            categories = Category.objects.filter(name=category[0].parent_category)[0].sub_categories.all()
            documents = Document.objects.filter(category__in=category).order_by('-id')
    else:
        documents = None

    context_data = {}

    if search_keyword:
        q = Q(author__username__icontains=search_keyword)
        q |= Q(title__icontains=search_keyword)
        q |= Q(text__icontains=search_keyword)
        documents = documents.filter(q)
        context_data.update({'search_keyword': search_keyword})


    paginator = Paginator(documents.order_by('doc_sort'), 10)

    if page > paginator.num_pages:
        page = 1

    page = paginator.page(page)

    # print(page)
    # print(paginator.num_pages)

    context_data.update({'object_list': page.object_list,
                         'current_category': category[0],
                         'sub_categories': categories,
                         'total_sub_category': categories[0].parent_category,
                         'is_paginated': True,
                         'paginator': paginator,
                         'page_obj': page})

    return render(request, 'board/document_list.html', context_data)

# class DocumentDetail(DetailView):
#     model = Document
#     template_name = 'board/document_detail.html'

@login_required
def document_detail(request, document_slug):
    document = get_object_or_404(Document, slug=document_slug)
    comment_form = CommentForm()
    comments = document.comments.all()
    # 동작하지 않는 경우
    # document = Document.objects.filter(slug=document_slug)
    # document[0].hits += 1
    # document[0].save()

    # 할당하면 동작함
    # test = document[0]
    # test.hits += 1
    # test.save()

    document.hits += 1
    document.save()
    return render(request, 'board/document_detail.html', {'object': document,
                                                          'comment_form': comment_form,
                                                          'comments': comments})

@login_required
def documment_recommend(request, document_slug):
    document = get_object_or_404(Document, slug=document_slug)
    user = request.user

    if user not in document.recommend.all():
        document.recommend.add(user)

    referer_url = request.META.get('HTTP_REFERER')
    path = urlparse(referer_url).path
    return HttpResponseRedirect(path)  # 도메인 주소 필요없이 경로만 필요하다.

# class DocumentCreate(CreateView):
#     model = Document
#     template_name = 'board/document_create.html'
#     form_class = DocumentForm
#
#     def form_valid(self, form):
#         form.instance.author_id = self.request.user.id
#         form.instance.slug = slugify(form.instance.title, allow_unicode=True)
#         return super().form_valid(form)

@login_required
def document_create(request, current_category_slug):
    category = Category.objects.filter(slug=current_category_slug)

    suser = request.user.is_superuser

    if request.method == "POST":
        document_form = DocumentForm(request.POST, request.FILES)

        app_name = request.POST.get('app_name')
        app_image = request.POST.get('app_image')
        app_price = request.POST.get('app_price')
        app_link = request.POST.get('app_link')

        # print(document_form.instance.title)
        if document_form.is_valid():
            # print(document_form.instance.category.name)
            # print(document_form.instance.title)
            document_form.instance.app_name = app_name
            document_form.instance.app_image = app_image
            document_form.instance.app_price = app_price
            document_form.instance.app_link = app_link
            document_form.instance.author_id = request.user.id
            document_form.instance.slug = slugify(document_form.instance.title, allow_unicode=True)
            if document_form.instance.category.name == "공지":
                document_form.instance.doc_sort = 0
            document = document_form.save()
            return redirect(document)
    else:
        document_form = DocumentForm(default_category=category[0], super_user = suser)

    return render(request, 'board/document_create.html', {'form': document_form})

@login_required
def document_update(request, document_id):
    if request.method == "POST":
        document = get_object_or_404(Document, pk=document_id)
        document_form = DocumentForm(request.POST, request.FILES, instance=document)

        app_name = request.POST.get('app_name')
        app_image = request.POST.get('app_image')
        app_price = request.POST.get('app_price')
        app_link = request.POST.get('app_link')

        if document_form.is_valid():
            document_form.instance.app_name = app_name
            document_form.instance.app_image = app_image
            document_form.instance.app_price = app_price
            document_form.instance.app_link = app_link
            document = document_form.save()
            return redirect(document)
    else:
        document = get_object_or_404(Document, pk=document_id)
        document_form = DocumentForm(instance=document)

    return render(request, 'board/document_update.html', {'form': document_form})

@login_required
def document_delete(request, document_id):
    if request.method == "POST":
        document = get_object_or_404(Document, pk=document_id)
        document.delete()
        return redirect('document')
    else:
        document = get_object_or_404(Document, pk=document_id)

    return render(request, 'board/document_delete.html', {'object': document})

def comment_create(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    comment_form = CommentForm(request.POST)
    comment_form.instance.author_id = request.user.id
    comment_form.instance.document_id = document_id

    if comment_form.is_valid():
        comment_form.save()

    return redirect(document)

def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    document = get_object_or_404(Document, pk=comment.document.id)

    if request.user != comment.author and not request.user.is_staff:
        messages.warning(request, '수정할 권한이 없어요!')
        return redirect(document)

    if request.method == "POST":
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return redirect(document)
    else:
        comment_form = CommentForm(instance=comment)

    return render(request, 'board/comment/update.html', {'comment_form': comment_form})

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    document = get_object_or_404(Document, pk=comment.document.id)

    if request.user != comment.author and not request.user.is_staff:
        messages.warning(request, '삭제할 권한이 없어요!')
        return redirect(document)

    if request.method == "POST":
        comment.delete()
        return redirect(document)
    else:
        return render(request, 'board/comment/delete.html', {'comment': comment})

def steam_app(request):

    app_id = request.GET.get('search', 0)
    print(app_id)

    # req = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/?key=EFF28AA4D572334E5E2D0443A2A357E0')

    url = 'http://store.steampowered.com/api/appdetails?appids='+ app_id +'&cc=kr&key=EFF28AA4D572334E5E2D0443A2A357E0'

    req = requests.get(url)

    if req.status_code == requests.codes.ok:
        print("connect")

        data = json.loads(req.text)

        # print(data)

        app_name = data[app_id]['data']['name']
        app_image = data[app_id]['data']['header_image']
        if data[app_id]['data']['release_date']['coming_soon']:
            app_release_date = data[app_id]['data']['release_date']['date']+"(출시 예정)"
        else:
            app_release_date = data[app_id]['data']['release_date']['date']

        try:
            app_price = data[app_id]['data']['price_overview']['final_formatted']
        except:
            # print(detail_req.json()[app]['data']['is_free'])
            if data[app_id]['data']['is_free']:
                app_price = "무료"
            else:
                app_price = "출시 예정"

        app_link = "https://store.steampowered.com/app/" + app_id

        # print(app_name)
        # print(app_image)
        # print(app_price)
        # print(app_link)
        # print(app_release_date)

        app_data = {
            "name": app_name,
            "header_image": app_image,
            "final_formatted": app_price,
            "link": app_link,
            "release_date": app_release_date
        }

    else:
        print("disconnect")

    return JsonResponse(app_data)