"""
Processing user requests and issuing a response
"""


from src import settings
from src import parser as p
from src.text_color import print_warning_text
from src import browser as br

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
        get  -p id, -u id
                        -p id - введет всю информацию  посте из последнй таблицы
                            пример get -p 2
                        -u id - выведет информацию о пользователе поста из последнй таблицы
                            пример get -u 5
                        
    """)

def update(argv):
    for i, v in enumerate(argv):
        if v == "-a":
            p.parse_main_topics()
            p.parse_sub_topics()
        elif v == "-m":
            p.parse_main_topics()
        elif v == "-s":
            p.parse_sub_topics()

def show(argv):
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
    for i, v in enumerate(argv):
        pass

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
            get(get_option(argv[index+1:]))
            