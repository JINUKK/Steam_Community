from .models import CrawlingData
import requests
from steam_api_key import my_key

def upcoming_data():
    url = "https://store.steampowered.com/explore/upcoming/key=" + my_key
    custom_headers = {
        'Cookie': 'Steam_Language=koreana',
    }
    req = requests.get(url, headers=custom_headers)

    if req.status_code == requests.codes.ok:
        upcoming_db_data = CrawlingData.objects.get(pk=1)
        upcoming_db_data.html_data = req.text
        upcoming_db_data.save()


    else:
        print("upcoming data status code :" + str(req.status_code))

def special_new_data():
    url = "https://store.steampowered.com/specials#p=0&tab=NewReleases&key=" + my_key
    custom_headers = {
        'Cookie': 'Steam_Language=koreana',
    }
    req = requests.get(url, headers=custom_headers)

    if req.status_code == requests.codes.ok:
        special_new_db_data = CrawlingData.objects.get(pk=2)
        special_new_db_data.html_data = req.text
        special_new_db_data.save()

    else:
        print("special new data status code : " + str(req.status_code))

def special_top_data():
    url = "https://store.steampowered.com/specials#p=0&tab=TopSellers&key=" + my_key
    custom_headers = {
        'Cookie': 'Steam_Language=koreana',
    }
    req = requests.get(url, headers=custom_headers)

    if req.status_code == requests.codes.ok:
        special_top_db_data = CrawlingData.objects.get(pk=3)
        special_top_db_data.html_data = req.text
        special_top_db_data.save()

    else:
        print("special top data status code : " + str(req.status_code))

def new_releases_data():
    url = "https://store.steampowered.com/explore/new/key=" + my_key
    custom_headers = {
        'Cookie': 'Steam_Language=koreana',
    }
    req = requests.get(url, headers=custom_headers)

    if req.status_code == requests.codes.ok:
        new_releases_db_data = CrawlingData.objects.get(pk=4)
        new_releases_db_data.html_data = req.text
        new_releases_db_data.save()

    else:
        print("new releases data status code : " + str(req.status_code))

def top_sellers_data():

    url = "https://store.steampowered.com/search/?filter=topsellers&key=" + my_key
    custom_headers = {
        'Cookie': 'Steam_Language=koreana',
    }
    req = requests.get(url, headers=custom_headers)

    if req.status_code == requests.codes.ok:
        top_sellers_db_data = CrawlingData.objects.get(pk=5)
        top_sellers_db_data.html_data = req.text
        top_sellers_db_data.save()

    else:
        print("top sellers data status code : " + str(req.status_code))