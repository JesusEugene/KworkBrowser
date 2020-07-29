from src import parser
from src.text_color import print_bad_text, print_good_text, print_normal_text


COUNT_CHARS = 9+3+70+8+8+11+20+5+5-2
def show(id):
    print_bot_line()
    print("│{5:3}│{0:70}│{1:8}│{2:8}│{3:11}│{4:20}│{6:5}│{7:5}│".format("Заголовок","Цена","Макс","Запросов","Время","ID",
                                                                        "Биржа","%")
                                                                        )
    p = [i for i in parser.get_pages(id)]
    id = 0
    for d in p:
        for i in d:
            print_midle_line()
            print_line(id,parser.parse_post(i))
            id+=1
    print_top_line()

def print_line(id,topic):
    line = "│{5:3}│{0:70}│{1:8}│{2:8}│{3:11}│{4:20}│{6:5}│{7:5}│".format(topic["topic"][0], topic["price"][0],
                                                        topic["price"][1], topic["info"][1], topic["info"][0],
                                                        id, topic["stats"][1], topic["stats"][2] )

    test =topic["stats"][2][:-1]
    if test.isdigit() and int(test) < 25:
        print_bad_text(line)
    elif test.isdigit() and int(test) > 60:
         print_good_text(line)
    else:
        print_normal_text(line)
    

def print_bot_line():
    print("┍{0}┑".format("―"*(COUNT_CHARS)))

def print_top_line():
    print("└{0}┘".format("―"*(COUNT_CHARS)))

def print_midle_line():
    print("├{0}┤".format("―"*(COUNT_CHARS)))

if __name__ == "__main__":
    show(84)