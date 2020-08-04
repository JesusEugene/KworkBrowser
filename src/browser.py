from os import path

from src import parser as pa
from src.text_color import print_bad_text, print_good_text, print_normal_text
from src.settings import DATA_DIR, SAVE_NAMES


COUNT_CHARS = 9+3+70+8+8+11+20+5+5-2

class Browser:

    def show(self, id):
        parser = pa.Parser()
        self.print_bot_line()
        print("│{5:3}│{0:70}│{1:8}│{2:8}│{3:11}│{4:20}│{6:5}│{7:5}│".format("Заголовок","Цена","Макс","Запросов","Время","ID",
                                                                            "Биржа","%")
                                                                            )
        id_ = 0
        ls = {}
        for d in parser.get_pages(id):
            for i in d:
                self.print_midle_line()
                tmp = parser.parse_post(i)
                ls[id_] = [tmp["topic"][1],tmp["stats"][0]]
                self.print_line(id_,tmp)
                id_+=1
        self.print_top_line()
        parser.serialization(ls,path.join(DATA_DIR,"{0}.json".format(str(id))))
        with open(path.join(DATA_DIR,SAVE_NAMES["user"]),"a") as f:
            f.write(str(id)+"\n")


    def print_line(self, id,topic):
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

    def show_post(self, id,pos):
        parser = pa.Parser()
        d = parser.deserialization(path.join(DATA_DIR,"{0}.json".format(str(id))))[pos][0]
        line = ""
        print(d)

    def show_user(self, id, pos):
        parser = pa.Parser()
        d = parser.deserialization(path.join(DATA_DIR,"{0}.json".format(str(id))))[pos][1]

    def print_bot_line(self):
        print("┍{0}┑".format("―"*(COUNT_CHARS)))

    def print_top_line(self):
        print("└{0}┘".format("―"*(COUNT_CHARS)))

    def print_midle_line(self):
        print("├{0}┤".format("―"*(COUNT_CHARS)))

if __name__ == "__main__":
    b =Browser()
    b.show(84)