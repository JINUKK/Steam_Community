from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import json

class NewGameInfo:
    def __init__(self, rank, link, img, discount_pct, original_price, final_price, name, tags):
        self.rank = rank
        self.link = link
        self.img = img
        self.discount_pct = discount_pct
        self.original_price = original_price
        self.final_price = final_price
        self.name = name
        self.tags = tags

class TopGameInfo:
    def __init__(self, rank, link, img, discount_pct, original_price, final_price, name, score, score_description):
        self.rank = rank
        self.link = link
        self.img = img
        self.discount_pct = discount_pct
        self.original_price = original_price
        self.final_price = final_price
        self.name = name
        self.score = score
        self.score_description = score_description

def rank_list(request):

    # 특별 할인 신제품 및 인기 제품 url
    special_new_url = "https://store.steampowered.com/specials#p=0&tab=NewReleases"
    special_top_url = "https://store.steampowered.com/specials#p=0&tab=TopSellers"

    # 인기 신제품 url
    newreleases_url = "https://store.steampowered.com/explore/new/"

    # 최고 인기 제품 url
    topsellers_url = "https://store.steampowered.com/search/?filter=topsellers"

    # 출시 예정 url
    upcoming_url = "https://store.steampowered.com/explore/upcoming/"

    custom_headers = {
        'Cookie': 'browserid=1308770386950708019; timezoneOffset=32400,0; _ga=GA1.2.991804284.1557365099; _gid=GA1.2.2097468064.1559719869; steamMachineAuth76561198081249015=F9ED950D4DF26C518DE81517E9C6B09AB448D306; steamCountry=KR%7Ceba6dbf163f68c6771ab7fd26a3e7588; sessionid=4587ebb1c606a3e6d10e0deb; recentapps=%7B%22779340%22%3A1559895726%2C%22801220%22%3A1559891524%2C%22641320%22%3A1559890557%2C%22629760%22%3A1559888598%2C%22620980%22%3A1559888593%2C%22435150%22%3A1559888582%2C%22752590%22%3A1559872077%2C%22726110%22%3A1559839922%2C%22648800%22%3A1559839708%2C%22995840%22%3A1559838749%7D; Steam_Language=koreana',
    }

    special_new_req = requests.get(special_new_url, headers=custom_headers)
    special_top_req = requests.get(special_top_url, headers=custom_headers)
    newreleases_req = requests.get(newreleases_url, headers=custom_headers)
    topsellers_req = requests.get(topsellers_url, headers=custom_headers)
    upcoming_req = requests.get(upcoming_url, headers=custom_headers)

    if special_new_req.status_code == requests.codes.ok:
        print("special discount new rank connect")

        special_new_html = BeautifulSoup(special_new_req.text, "html.parser")
        special_new_items = special_new_html.select('div#tab_content_NewReleases > div#NewReleasesTable > div#NewReleasesRows > a.tab_item')
        special_new_list = []

        for idx, item in enumerate(special_new_items[:5]):
            rank = idx + 1
            link = item.get('href')
            img = item.select_one('div.tab_item_cap > img.tab_item_cap_img').get('src')
            discount_pct = item.select_one('div.discount_block > div.discount_pct').text
            original_price = item.select_one('div.discount_block > div.discount_prices > div.discount_original_price').text
            final_price = item.select_one('div.discount_block > div.discount_prices > div.discount_final_price').text
            name = item.select_one('div.tab_item_content > div.tab_item_name').text
            tags = item.select_one('div.tab_item_content > div.tab_item_details > div.tab_item_top_tags').text
            game_info = NewGameInfo(rank, link, img, discount_pct, original_price, final_price, name, tags)
            special_new_list.append(game_info)
    else:
        print("special discount new rank disconnect")

    if special_top_req.status_code == requests.codes.ok:
        print("special discount top rank connect")

        special_top_html = BeautifulSoup(special_top_req.text, "html.parser")
        special_top_items = special_top_html.select('div#tab_content_TopSellers > div#TopSellersTable > div#TopSellersRows > a.tab_item')
        special_top_list = []

        for idx, item in enumerate(special_top_items[:5]):
            rank = idx + 1
            link = item.get('href')
            img = item.select_one('div.tab_item_cap > img.tab_item_cap_img').get('src')
            discount_pct = item.select_one('div.discount_block > div.discount_pct').text
            original_price = item.select_one('div.discount_block > div.discount_prices > div.discount_original_price').text
            final_price = item.select_one('div.discount_block > div.discount_prices > div.discount_final_price').text
            name = item.select_one('div.tab_item_content > div.tab_item_name').text
            tags = item.select_one('div.tab_item_content > div.tab_item_details > div.tab_item_top_tags').text
            game_info = NewGameInfo(rank, link, img, discount_pct, original_price, final_price, name, tags)
            special_top_list.append(game_info)
    else:
        print("special discount top rank disconnect")

    if newreleases_req.status_code == requests.codes.ok:
        print("newreleases rank connect")

        newreleases_html = BeautifulSoup(newreleases_req.text, "html.parser")
        newreleases_items = newreleases_html.select('div.home_tabs_content > div.tab_content > a.tab_item')
        newreleases_list = []

        for idx, item in enumerate(newreleases_items[:5]):
            rank = idx + 1
            link = item.get('href')
            img = item.select_one('div.tab_item_cap > img.tab_item_cap_img').get('src')

            is_not_nonetype = item.select_one('div.discount_block > div.discount_prices > div.discount_original_price')
            if is_not_nonetype:
                discount_pct = item.select_one('div.discount_block > div.discount_pct').text
                original_price = item.select_one(
                    'div.discount_block > div.discount_prices > div.discount_original_price').text
            else:
                discount_pct = ''
                original_price = ''

            final_price = item.select_one('div.discount_block > div.discount_prices > div.discount_final_price').text
            name = item.select_one('div.tab_item_content > div.tab_item_name').text
            tags = item.select_one('div.tab_item_content > div.tab_item_details > div.tab_item_top_tags').text
            game_info = NewGameInfo(rank, link, img, discount_pct, original_price, final_price, name, tags)
            newreleases_list.append(game_info)
    else:
        print("newreleases rank disconnect")

    if topsellers_req.status_code == requests.codes.ok:
        print("topsellers_list rank connect")

        topsellers_html = BeautifulSoup(topsellers_req.text, "html.parser")
        topsellers_items = topsellers_html.select('div#search_result_container > div > a.search_result_row')
        topsellers_list = []

        for idx, item in enumerate(topsellers_items[:5]):
            rank = idx + 1
            link = item.get('href')
            img = item.select_one('div.search_capsule > img').get('src')
            discount_pct = item.select_one(
                'div.responsive_search_name_combined > div.search_price_discount_combined > div.search_discount').text.strip()

            is_not_nonetype = item.select_one(
                'div.responsive_search_name_combined > div.search_price_discount_combined > div.search_price > span')
            if is_not_nonetype:
                original_price = item.select_one(
                    'div.responsive_search_name_combined > div.search_price_discount_combined > div.search_price > span').text
                final_price = item.select_one(
                    'div.responsive_search_name_combined > div.search_price_discount_combined > div.search_price').text.replace(
                    original_price, '').strip()
            else:
                original_price = ''
                final_price = item.select_one(
                    'div.responsive_search_name_combined > div.search_price_discount_combined > div.search_price').text.strip()

            name = item.select_one('div.responsive_search_name_combined > div.search_name').text.strip()

            is_not_score_nonetype = item.select_one(
                'div.responsive_search_name_combined > div.search_reviewscore > span.search_review_summary')

            if is_not_score_nonetype:
                score_text = item.select_one(
                    'div.responsive_search_name_combined > div.search_reviewscore > span.search_review_summary').get(
                    'data-tooltip-html').split('<br>')
                score = score_text[0]
                score_description = score_text[1]
            else:
                score = '평가 없음'
                score_description = '이 제품에는 아직 평가가 없습니다.'

            game_info = TopGameInfo(rank, link, img, discount_pct, original_price, final_price, name, score, score_description)
            topsellers_list.append(game_info)

    else:
        print("topsellers_list rank disconnect")

    if upcoming_req.status_code == requests.codes.ok:
        print("upcoming rank connect")

        upcoming_html = BeautifulSoup(upcoming_req.text, "html.parser")
        upcoming_items = upcoming_html.select('div.home_tabs_content > div.tab_content > a.tab_item')
        upcoming_list = []

        for idx, item in enumerate(upcoming_items[:5]):
            rank = idx + 1
            link = item.get('href')
            img = item.select_one('div.tab_item_cap > img.tab_item_cap_img').get('src')
            discount_pct = ''
            original_price = ''
            final_price = ''
            name = item.select_one('div.tab_item_content > div.tab_item_name').text
            tags = item.select_one('div.tab_item_content > div.tab_item_details > div.tab_item_top_tags').text
            game_info = NewGameInfo(rank, link, img, discount_pct, original_price, final_price, name, tags)
            upcoming_list.append(game_info)
    else:
        print("upcoming rank disconnect")

    return render(request, 'main/rank_list.html', {'special_new': special_new_list,
                                                   'special_top': special_top_list,
                                                   'newreleases': newreleases_list,
                                                   'topsellers': topsellers_list,
                                                   'upcoming':upcoming_list})
