import requests
from bs4 import BeautifulSoup
from steam_api_key import my_key
import os
from config.settings import BASE_DIR

def upcoming_data():
    url = "https://store.steampowered.com/explore/upcoming/key=" + my_key
    custom_headers = {
        'Cookie': 'Steam_Language=koreana',
    }
    req = requests.get(url, headers=custom_headers)

    if req.status_code == requests.codes.ok:
        print("upcoming data connect")
        text_file = open(os.path.join(BASE_DIR, 'static/crawling_data/upcoming_crawling_data.txt'), 'w')
        text_file.write(req.text)
        text_file.close()

    else:
        print("upcoming data disconnect")

def special_new_data():
    url = "https://store.steampowered.com/specials#p=0&tab=NewReleases&key=" + my_key
    custom_headers = {
        'Cookie': 'Steam_Language=koreana',
    }
    req = requests.get(url, headers=custom_headers)

    if req.status_code == requests.codes.ok:
        print("special new data connect")
        text_file = open(os.path.join(BASE_DIR, 'static/crawling_data/special_new_crawling_data.txt'), 'w')
        text_file.write(req.text)
        text_file.close()

    else:
        print("special new data disconnect")

def special_top_data():
    url = "https://store.steampowered.com/specials#p=0&tab=TopSellers&key=" + my_key
    custom_headers = {
        'Cookie': 'Steam_Language=koreana',
    }
    req = requests.get(url, headers=custom_headers)

    if req.status_code == requests.codes.ok:
        print("special top data connect")
        text_file = open(os.path.join(BASE_DIR, 'static/crawling_data/special_top_crawling_data.txt'), 'w')
        text_file.write(req.text)
        text_file.close()

    else:
        print("special top data disconnect")

def new_releases_data():
    url = "https://store.steampowered.com/explore/new/key=" + my_key
    custom_headers = {
        'Cookie': 'Steam_Language=koreana',
    }
    req = requests.get(url, headers=custom_headers)

    if req.status_code == requests.codes.ok:
        print("new releases data connect")
        text_file = open(os.path.join(BASE_DIR, 'static/crawling_data/new_releases_crawling_data.txt'), 'w')
        text_file.write(req.text)
        text_file.close()

    else:
        print("new releases data disconnect")

def top_sellers_data():

    url = "https://store.steampowered.com/search/?filter=topsellers&key=" + my_key
    custom_headers = {
        'Cookie': 'Steam_Language=koreana',
    }
    req = requests.get(url, headers=custom_headers)

    if req.status_code == requests.codes.ok:
        print("top sellers data connect")
        text_file = open(os.path.join(BASE_DIR, 'static/crawling_data/top_seller_crawling_data.txt'), 'w')
        text_file.write(req.text)
        text_file.close()

    else:
        print("top sellers data disconnect")

if __name__ == "__main__":
    upcoming_data()
    special_new_data()
    special_top_data()
    new_releases_data()
    top_sellers_data()
    print("Crawling data Update complete!")