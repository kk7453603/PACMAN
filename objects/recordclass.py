# В этих  массивах должны попарно находится значения, т.е. [[name,score,time]...]
class RecordCounter:
    def __init__(self, msvalues):
        self.ms = msvalues

    def clear_table(self):
        if len(self.ms) > 10:
            for i in range(10,len(self.ms)):
                self.ms.remove(self.ms[i])

    def sort_scores(self):
        self.ms.sort(key=lambda el: el[1], reverse=True)
        self.clear_table()
        return self.ms

    def make_file(self):
        self.sort_scores()
        with open("highscore_table.txt", "w") as wr:
            for i in range(10):
                wr.write("Имя: {} Очки: {} Время: {}".format(self.ms[i][0], self.ms[i][1], self.ms[i][2]))



    def ret_data(self):
        #
        self.sort_scores()
        sl={"names":[i[0] for i in self.ms],"scores":[i[1] for i in self.ms],"times":[i[2] for i in self.ms]}
        return sl

