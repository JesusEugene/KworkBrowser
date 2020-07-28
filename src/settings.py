"""
Settings for KworkBrowser
"""


import os


#BASE_DIR - базовый путь проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR,"src","data")

#DEBUG - вывод дебаг инфы
DEBUG = True

DEBUG_PHRASES = {
        "__init__" : "Debug: Import __init__ from",
        "serl" : "Debug: Data has been serialization to",
        "deserl" : "Debug: Data has been deserialization from",
}

HTTP_MAIN_PAGE = r"https://kwork.ru/projects"

SELECTS_PATH = {
        "main" : "div.js-category-container.projects-filter__select > select",
        "sub" : "div.js-sub-category-container.projects-filter__select.hidden"
}


SAVE_NAMES ={
        "main_topics" : "main_topics.json",
        "sub_topics" : "sub_topics.json",
}