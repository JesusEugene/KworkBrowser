import os
import json

from pyquery import PyQuery as pq

from src.settings import HTTP_MAIN_PAGE, SELECTS_PATH, DATA_DIR , SAVE_NAMES, DEBUG_PHRASES
from src.text_color import print_debug_text, print_warning_text


def parse_main_topics():
    p = pq(HTTP_MAIN_PAGE)
    main_topics = p(SELECTS_PATH["main"]).children()
    print_debug_text("\nMain topics:")
    d = {}
    for i in main_topics:
        print_debug_text("\t"+i.attrib["value"]+" "+i.text)
        if i.attrib["value"].isdigit():
            d[i.attrib["value"]] = i.text
    else:
        serialization(d,SAVE_NAMES["main_topics"])
        print_warning_text("main topics has been update")



def parse_sub_topics():
    p = pq(HTTP_MAIN_PAGE)
    sub_topics = p(SELECTS_PATH["sub"]).children()
    print_debug_text("\nSub topics:")
    d = {}
    for topic in sub_topics:
        for sub in topic:
            print_debug_text(topic.attrib["data-category-id"])
            tmp_d = {}
            for s in sub[1:]:
                print_debug_text("\t"+s.text)
                tmp_d[s.attrib["value"] ] = s.text
            else:
                d[topic.attrib["data-category-id"]] =tmp_d
    else:
        serialization(d,SAVE_NAMES["sub_topics"])
        print_warning_text("sub topics has been update")

    
def parse_post(child):
    """
    Parse one post and return {}
    """
    topic = [
        child('div.wants-card__header-title.first-letter.breakwords > a')[0].text.strip(),
        child('div.wants-card__header-title.first-letter.breakwords > a')[0].attrib["href"]
    ] #


    price =[child("div > span.fs12")[0].tail.replace(" ","")]#
    tml = child("div.wants-card__description-higher-price > span.nowrap")
    if len(tml) == 2:
        price.append(tml[0].text[2:].replace(" ",""))
    else:
        price.append(price[0])

    tmp =  child("div.ta-right > div.query-item__info.mb10.ta-left")[0].text.split("\xa0\xa0\xa0")#
    info = [
        tmp[0].split(":")[1].strip(),
        tmp[1].split("\xa0")[1].strip()
    ]
    
    tmp = child("div.mb10.want-payer-statistic.d-flex > div > div.dib.v-align-t >br")[0].tail.replace("\t","").replace("\n","").split(" ")
    if len(tmp) == 1:
        tmp.append("None")
    stats = [
        child("div.mb10.want-payer-statistic.d-flex > div > div:nth-child(1) > div > a")[0].text.strip(),
        child("div.mb10.want-payer-statistic.d-flex > div > div.dib.v-align-t")[0].text.split(":")[1].replace("\t","").replace("\n","").strip(),
        tmp[1],
        
    ]#
    return {
        "topic" : topic,
        "price" : price,
        "info" : info,
        "stats" : stats,
    }

def parse_full_post(url):
    pass


def get_posts(page):
    """
    Parse all posts on the page
        Return []
    """
    print_debug_text(DEBUG_PHRASES["get_posts"]+page.base_url)
    items = page("div.wants-content > div").children()
    childrens = []
    for i in items:
        if(i.attrib["class"].startswith("card want-card")):
            childrens.append(items("div."+i.attrib["class"].replace(" ",".")))
    else:
        return childrens


def get_page(id,num):
    """
    Return page by ID and number
    """
    https = HTTP_MAIN_PAGE+"?c={0}&page={1}".format(id,num)
    print_debug_text(DEBUG_PHRASES["get_page"]+https)
    p = pq(https)
    return p


def get_pages(id):
    """
    Return all pages on id as Enumerator
    """
    p =pq(HTTP_MAIN_PAGE+"?c{0}".format(id)) #стартовая страница

    counter_page = 1
    while True:
        page = get_posts(get_page(id,counter_page))
        if page:
            counter_page+=1
            yield page
        else:
            break



def serialization(data,name):
    with open(os.path.join(DATA_DIR,name),"w") as f:
        json.dump(data, f)
    print_debug_text("\n"+DEBUG_PHRASES["serl"]+os.path.join(DATA_DIR,name))


def deserialization(name):
    with open(os.path.join(DATA_DIR,name)) as f:
        return json.load(f)
    print_debug_text("\n"+DEBUG_PHRASES["deserl"]+os.path.join(DATA_DIR,name))

if __name__ == "__main__":
    pass