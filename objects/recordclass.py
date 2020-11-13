# В этих  массивах должны попарно находится значения, т.е. [[name,score,time]...]
class RecordCounter:
    def __init__(self, msvalues):
        ms = msvalues

    def sort_scores(self):
        self.ms.sort(key=lambda el: el[1], reverse=True)
        return self.ms

    def make_file(self):
        with open("highscore_table.txt", "w") as wr:
            for i in range(10):
                wr.write("Имя: {} Очки: {} Время: {}".format(self.ms[i][0], self.ms[i][1], self.ms[i][2]))

    def write_table(self):
        pass
