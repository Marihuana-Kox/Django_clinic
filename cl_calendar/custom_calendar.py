from datetime import datetime as dt


class Custom_calendar(object):
    def __init__(self, cal):
        self.cal = cal

    def __str__(self):
        return "Результат такой - %s " % self.cal
