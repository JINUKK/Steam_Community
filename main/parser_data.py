from bs4 import BeautifulSoup

class AppInfo:
    def __init__(self, rank='', link='', img='', discount_pct='', original_price='',
                 final_price='', name='', tags='', score='', score_description=''):
        self.rank = rank
        self.link = link
        self.img = img
        self.discount_pct = discount_pct
        self.original_price = original_price
        self.final_price = final_price
        self.name = name
        self.tags = tags
        self.score = score
        self.score_description = score_description

def upcoming_data_parser(html_data):
    html = BeautifulSoup(html_data, "html.parser")
    items = html.select('div.store_horizontal_autoslider > a')
    data_list = []

    for item in items[:8]:
        link = item.get('href')
        img = item.select_one('div.capsule.headerv5 > img').get('src')
        app_info = AppInfo('', link, img)
        data_list.append(app_info)

    return data_list

def special_new_parser(html_data):
    html = BeautifulSoup(html_data, "html.parser")
    items = html.select('div#tab_content_NewReleases > div#NewReleasesTable > div#NewReleasesRows > a.tab_item')
    data_list = []

    for idx, item in enumerate(items[:5]):
        rank = idx + 1
        link = item.get('href')
        img = item.select_one('div.tab_item_cap > img.tab_item_cap_img').get('src')
        discount_pct = item.select_one('div.discount_block > div.discount_pct').text
        original_price = item.select_one('div.discount_block > div.discount_prices > div.discount_original_price').text
        final_price = item.select_one('div.discount_block > div.discount_prices > div.discount_final_price').text
        name = item.select_one('div.tab_item_content > div.tab_item_name').text
        tags = item.select_one('div.tab_item_content > div.tab_item_details > div.tab_item_top_tags').text
        app_info = AppInfo(rank, link, img, discount_pct, original_price, final_price, name, tags)
        data_list.append(app_info)

    return data_list

def special_top_parser(html_data):
    html = BeautifulSoup(html_data, "html.parser")
    items = html.select('div#tab_content_TopSellers > div#TopSellersTable > div#TopSellersRows > a.tab_item')
    data_list = []

    for idx, item in enumerate(items[:5]):
        rank = idx + 1
        link = item.get('href')
        img = item.select_one('div.tab_item_cap > img.tab_item_cap_img').get('src')
        if item.select_one('div.discount_block > div.discount_pct'):
            discount_pct = item.select_one('div.discount_block > div.discount_pct').text
            original_price = item.select_one(
                'div.discount_block > div.discount_prices > div.discount_original_price').text
        else:
            discount_pct = ""
            original_price = ""
        final_price = item.select_one('div.discount_block > div.discount_prices > div.discount_final_price').text
        name = item.select_one('div.tab_item_content > div.tab_item_name').text
        tags = item.select_one('div.tab_item_content > div.tab_item_details > div.tab_item_top_tags').text
        app_info = AppInfo(rank, link, img, discount_pct, original_price, final_price, name, tags)
        data_list.append(app_info)

    return data_list

def new_releases_parser(html_data):
    html = BeautifulSoup(html_data, "html.parser")
    items = html.select('div.home_tabs_content > div.tab_content > a.tab_item')
    data_list = []

    for idx, item in enumerate(items[:5]):
        rank = idx + 1
        link = item.get('href')
        img = item.select_one('div.tab_item_cap > img.tab_item_cap_img').get('src')

        exist_discount = item.select_one('div.discount_block > div.discount_prices > div.discount_original_price')
        if exist_discount:
            discount_pct = item.select_one('div.discount_block > div.discount_pct').text
            original_price = exist_discount.text
        else:
            discount_pct = ''
            original_price = ''

        final_price = item.select_one('div.discount_block > div.discount_prices > div.discount_final_price').text
        name = item.select_one('div.tab_item_content > div.tab_item_name').text
        tags = item.select_one('div.tab_item_content > div.tab_item_details > div.tab_item_top_tags').text
        app_info = AppInfo(rank, link, img, discount_pct, original_price, final_price, name, tags)
        data_list.append(app_info)

    return data_list

def top_sellers_parser(html_data):
    html = BeautifulSoup(html_data, "html.parser")
    items = html.select('div#search_result_container > div > a.search_result_row')
    data_list = []

    for idx, item in enumerate(items[:5]):
        rank = idx + 1
        link = item.get('href')
        img = item.select_one('div.search_capsule > img').get('src')
        discount_pct = item.select_one(
            'div.responsive_search_name_combined > div.search_price_discount_combined > div.search_discount').text.strip()

        exist_discount = item.select_one(
            'div.responsive_search_name_combined > div.search_price_discount_combined > div.search_price > span')
        if exist_discount:
            original_price = exist_discount.text
            final_price = item.select_one(
                'div.responsive_search_name_combined > div.search_price_discount_combined > div.search_price').text.replace(
                original_price, '').strip()
        else:
            original_price = ''
            final_price = item.select_one(
                'div.responsive_search_name_combined > div.search_price_discount_combined > div.search_price').text.strip()

        name = item.select_one('div.responsive_search_name_combined > div.search_name').text.strip()

        exist_score = item.select_one(
            'div.responsive_search_name_combined > div.search_reviewscore > span.search_review_summary')

        if exist_score:
            score_text = exist_score.get('data-tooltip-html').split('<br>')
            score = score_text[0]
            score_description = score_text[1]
        else:
            score = '평가 없음'
            score_description = '이 제품에는 아직 평가가 없습니다.'

        app_info = AppInfo(rank, link, img, discount_pct, original_price, final_price, name, '', score, score_description)
        data_list.append(app_info)

    return data_list

