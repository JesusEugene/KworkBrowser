"""
Settings for KworkBrowser
"""


import os


#BASE_DIR - базовый путь проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#DATA_DIR - путь для даты
DATA_DIR = os.path.join(BASE_DIR,"src","data")

#HTTP_MAIN_PAGE - ссылка на страницу для парса
HTTP_MAIN_PAGE = r"https://kwork.ru/projects"


#DEBUG - вывод дебаг инфы
DEBUG = False

#DEBUG_PHRASES - список дефолтных фраз для удобного дебага
DEBUG_PHRASES = {
        "__init__" : "Debug: Import __init__ from ",
        "serl" : "Debug: Data has been serialization to ",
        "deserl" : "Debug: Data has been deserialization from ",
        "get_page" : "Debug: The page was received at ",
        "get_posts" : "Debug: The page was parsed, url page ",
}

#SELECTS_PATH - имена для парса
SELECTS_PATH = {
        "main" : "div.js-category-container.projects-filter__select > select",
        "sub" : "div.js-sub-category-container.projects-filter__select.hidden",
        "base_post" : "",
}

#SAVE_NAMES - именя для сейва
SAVE_NAMES ={
        "main_topics" : "main_topics.json",
        "sub_topics" : "sub_topics.json",
}