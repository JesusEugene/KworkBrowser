"""
Processing user requests and issuing a response
"""

from os import path

from src import settings
from src import parser as pa
from src.text_color import print_warning_text
from src import browser

def help():
    
    print("""\nСписок комманд:

        help - Показывает список команд.\n
        update -a, -m, -s, Обновляетc топики
                        -a Обновляет все топики
                        -m Обновляет главные топики
                        -s Обновляет саб топики\n
        show -l, id, отображает все посты id
                        -id - вывести посты определенного id
                            пример show -84
                        -l покажет пары id - название\n
        get  -p id
                        -p id - введет всю информацию  посте из последнй таблицы
                            пример get -p 2         
    """)

def update(argv):
    p = pa.Parser()
    for i, v in enumerate(argv):
        if v == "-a":
            p.parse_main_topics()
            p.parse_sub_topics()
        elif v == "-m":
            p.parse_main_topics()
        elif v == "-s":
            p.parse_sub_topics()

def show(argv):
    p = pa.Parser()
    br = browser.Browser()
    for i, v in enumerate(argv):
        if v == "-l":
            m = p.deserialization(settings.SAVE_NAMES["main_topics"])
            s = p.deserialization(settings.SAVE_NAMES["sub_topics"])
            print_warning_text("TOPICS")
            for key in m:
                print_warning_text("\t{1:4}{0:4}{2} ".format("-",key,m[key]))
                for k in s[key]:
                        print_warning_text("\t\t{1:4}{0:4}{2}".format("-",k,s[key][k]))
        elif v[1:].isdigit():
            br.show(int(v[1:]))
            

def get(argv):
    br = browser.Browser()
    last = ""
    with open(path.join(settings.DATA_DIR,settings.SAVE_NAMES["user"]),"r") as f:
        last = f.readlines()[-1][:-1]

    post = False
    for i, v in enumerate(argv):
        if v in ["-p"]:
            post = True
            user = False
            continue
        if post and v.isdigit():
            br.show_post(last,v)
        elif user and v.isdigit():
            br.show_user(last,v)
        else: 
            break


def get_option(argv):
    """
    Get all options in argv
    """
    options = []
    for s in argv:
        if not s.startswith("-"):
            break
        options.append(s)
    return options


def execute_from_command_line(argv):
    """ 
    execute_from_command_line(**argv)

    This function takes arguments and returns what was requested
    """
    tmp = 0
    for index, value in enumerate(argv):
        if value in ["help"]:
            help()
        elif value in ["update"]:
            update(get_option(argv[index+1:]))
        elif value in ["show"]:
            show(get_option(argv[index+1:]))
        elif value in ["get"]:
            get(argv[index+1:])
            