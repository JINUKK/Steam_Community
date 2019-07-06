from django.shortcuts import render
from .parser_data import *

def rank_list(request):
    upcoming_text = open('./static/crawling_data/upcoming_crawling_data.txt', 'r')
    special_new_text = open('./static/crawling_data/special_new_crawling_data.txt', 'r')
    special_top_text = open('./static/crawling_data/special_top_crawling_data.txt', 'r')
    new_releases_text = open('./static/crawling_data/new_releases_crawling_data.txt', 'r')
    top_sellers_text = open('./static/crawling_data/top_seller_crawling_data.txt', 'r')

    upcoming_data = upcoming_text.read()
    special_new_data = special_new_text.read()
    special_top_data = special_top_text.read()
    new_releases_data = new_releases_text.read()
    top_sellers_data = top_sellers_text.read()

    upcoming_list = upcoming_data_parser(upcoming_data)
    special_new_list = special_new_parser(special_new_data)
    special_top_list = special_top_parser(special_top_data)
    new_releases_list = new_releases_parser(new_releases_data)
    top_sellers_list = top_sellers_parser(top_sellers_data)

    upcoming_text.close()
    special_new_text.close()
    special_top_text.close()
    new_releases_text.close()
    top_sellers_text.close()

    return render(request, 'main/rank_list.html', {'upcoming':upcoming_list,
                                                   'special_new': special_new_list,
                                                   'special_top': special_top_list,
                                                   'new_releases': new_releases_list,
                                                   'top_sellers': top_sellers_list,})

def rank_pause(request):
    return render(request, 'main/rank_list.html')