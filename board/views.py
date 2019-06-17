from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Category, Document
from .forms import DocumentForm
from django.utils.text import slugify

from django.contrib.auth.decorators import login_required

class DocumentList(ListView):
    model = Document
    template_name = 'board/document_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'slug' in self.kwargs:
            category = Category.objects.filter(slug=self.kwargs['slug'])
            categories = category[0].sub_categories.all()
            if category.exists():
                queryset = queryset.filter(category__in=categories).order_by('-id')
            else:
                queryset = queryset.none()
        return queryset

def documentList(request, category_slug):
    print(category_slug)
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

    return render(request, 'board/document_list.html', {'object_list': documents,
                                                        'current_category': category[0],
                                                        'sub_categories': categories,
                                                        'total_category': categories[0].parent_category})

class DocumentDetail(DetailView):
    model = Document
    template_name = 'board/document_detail.html'

def documentDetail(request, document_slug):
    document = get_object_or_404(Document, slug=document_slug)

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
    return render(request, 'board/document_detail.html', {'object': document})

class DocumentCreate(CreateView):
    model = Document
    template_name = 'board/document_create.html'
    form_class = DocumentForm

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        form.instance.slug = slugify(form.instance.title, allow_unicode=True)
        return super().form_valid(form)

@login_required
def documentCreate(request, current_category_slug):
    category = Category.objects.filter(slug=current_category_slug)
    if request.method == "POST":
        document_form = DocumentForm(request.POST, request.FILES)
        # print(document_form.instance.title)
        if document_form.is_valid():
            # print(document_form.instance.title)
            document_form.instance.author_id = request.user.id
            document_form.instance.slug = slugify(document_form.instance.title, allow_unicode=True)
            document = document_form.save()
            return redirect(document)
    else:
        document_form = DocumentForm(default_category=category[0])

    return render(request, 'board/document_create.html', {'form': document_form})

@login_required
def document_update(request, document_id):
    if request.method == "POST":
        document = get_object_or_404(Document, pk=document_id)
        document_form = DocumentForm(request.POST, request.FILES, instance=document)

        if document_form.is_valid():
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