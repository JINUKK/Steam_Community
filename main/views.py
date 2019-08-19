from django.shortcuts import render
from .parser_data import *
from .models import CrawlingData

def rank_list(request):
    upcoming_html_data = CrawlingData.objects.get(pk=1)
    special_new_html_data = CrawlingData.objects.get(pk=2)
    special_top_html_data = CrawlingData.objects.get(pk=3)
    new_releases_html_data = CrawlingData.objects.get(pk=4)
    top_sellers_html_data = CrawlingData.objects.get(pk=5)

    upcoming_list = upcoming_data_parser(upcoming_html_data.html_data)
    special_new_list = special_new_parser(special_new_html_data.html_data)
    special_top_list = special_top_parser(special_top_html_data.html_data)
    new_releases_list = new_releases_parser(new_releases_html_data.html_data)
    top_sellers_list = top_sellers_parser(top_sellers_html_data.html_data)

    return render(request, 'main/rank_list.html', {'upcoming':upcoming_list,
                                                   'special_new': special_new_list,
                                                   'special_top': special_top_list,
                                                   'new_releases': new_releases_list,
                                                   'top_sellers': top_sellers_list,})

def rank_pause(request):
    return render(request, 'main/rank_list.html')