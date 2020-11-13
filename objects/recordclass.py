# В этих  массивах должны попарно находится значения, т.е. [[name,score,time]...]
class RecordCounter:
    def __init__(self, msvalues):
        ms = msvalues

    def sort_scores(self):
        self.ms.sort(key=lambda el: el[1], reverse=True)
        return self.ms

