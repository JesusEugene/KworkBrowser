import os
import json

from pyquery import PyQuery as pq

from src.settings import HTTP_MAIN_PAGE, SELECTS_PATH, DATA_DIR , SAVE_NAMES, DEBUG_PHRASES
from src.text_color import print_debug_text


def parse_main_topics():
    p = pq(HTTP_MAIN_PAGE)
    main_topics = p(SELECTS_PATH["main"]).children()
    print_debug_text("\nMain topics:")
    d = {}
    for i in main_topics:
        print_debug_text("\t"+i.attrib["value"]+" "+i.text)
        d[i.text] = i.attrib["value"]
    else:
        serialization(d,SAVE_NAMES["main_topics"])


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


def serialization(data,name):
    with open(os.path.join(DATA_DIR,name),"w") as f:
        json.dump(data, f)
    print_debug_text("\n"+DEBUG_PHRASES["serl"]+" "+os.path.join(DATA_DIR,name))


def deserialization(name):
    with open(os.path.join(DATA_DIR,name)) as f:
        return json.load(f)
    print_debug_text("\n"+DEBUG_PHRASES["deserl"]+" "+os.path.join(DATA_DIR,name))

if __name__ == "__main__":
    pass