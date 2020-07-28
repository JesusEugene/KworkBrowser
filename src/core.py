"""
Processing user requests and issuing a response
"""


from src import settings
from src import parser as p
from src.text_color import print_warning_text

def help():
    
    print("""\nСписок комманд:
        help - Показывает список команд.
        update -a, -m, -s, Обновляет информацию про топики, указывается только 1 аргумент
                        -a Обновляет все топики
                        -m Обновляет главные топики
                        -s Обновляет саб топики
    """)

def update(argv):
    for i, v in enumerate(argv):
        if v == "-a":
            p.parse_main_topics()
            break
        elif v == "-m":
            p.parse_main_topics()
            p.parse_sub_topics()
            break
        elif v == "-s":
            p.parse_sub_topics()
            break
    else:
        print_warning_text("Аргументы не указанны или указанны неверно")

def execute_from_command_line(argv):
    """
    execute_from_command_line(**argv)

    This function takes arguments and returns what was requested
    """
    tmp = 0;
    for index, value in enumerate(argv):
        if value in ["help"]:
            help()
        elif value in ["update"]:
            update(argv[index:])
