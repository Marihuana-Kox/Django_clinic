from datetime import datetime as dt
import calendar


def calendar_best(year, month, week_work):
    months = {
        1: "Январь",
        2: "Февраль",
        3: "Март",
        4: "Апрель",
        5: "Май",
        6: "Июнь",
        7: "Июль",
        8: "Август",
        9: "Сентябрь",
        10: "Октябрь",
        11: "Ноябрь",
        12: "Декабрь",
    }

    weekdays = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс", ]

    month = int(month)
    year = int(year)
    day_week = dt(year, month, 21).weekday()

    now = dt.now()
    today_month = int(now.strftime('%m'))

    happy_day = int(now.today().isoweekday())

    last_year = year
    next_year = year

    if month == 12:
        next_month = 1
        next_year + 1
        last_month = 11
        last_year - 1
    elif month == 1:
        next_month = 2
        last_month = 12
    else:
        next_month = month + 1
        last_month = month - 1

    no_working = []

    for val in week_work.values('week_day'):
        no_working.append(int(*val.values()) - 1)

    today_year = now.strftime('%Y')
    today = now.today().strftime('%-d')

    cal = calendar.monthcalendar(year, month)
    viewcall = "<div class='block-select-month'>"
    viewcall += "<div class='time-style style-arr arr-left'>"
    # viewcall += "<a href='/records/month/{0}-{1}/'" . format(
    viewcall += "<a class='arr' name='{0}-{1}'" . format(
        last_year - 1 if last_month == 12 else last_year, last_month)
    viewcall += "><< {0} {1}</a>" . format(
        months[last_month], last_year - 1 if last_month == 12 else last_year)
    viewcall += "</div>"
    viewcall += "<div class='time-style style-arr top-date'>"
    viewcall += "<H4 class='get-last-month' id='{0}'>{1}</H4>" . format(
        month, months[month])
    viewcall += "<H6 class='get-last-year'>{0}</H6>" . format(year)
    viewcall += "</div>"
    viewcall += "<div class='time-style style-arr arr-right'>"
    # viewcall += "<a href='/records/month/{0}-{1}/'" . format(
    viewcall += "<a class='arr' name='{0}-{1}'" . format(
        next_year + 1 if next_month == 1 else next_year, next_month)
    viewcall += ">{0} {1} >></a>" . format(
        months[next_month], next_year + 1 if next_month == 1 else next_year)
    viewcall += "</div></div>"
    viewcall += "<div class='col-12 time-style'>"
    viewcall += "<div class='row'>"
    for wd in weekdays:
        viewcall += "<div class='col-days-week'>{0}</div>" . format(wd)

    for weeks in cal:
        for days in weeks:
            if days == 0:
                viewcall += "<div class='col-days-none'></div>"
            else:
                """Выбираем сегодняшний день"""
                if days == int(today) and month == today_month and year == int(today_year):
                    """Проверяем, не попадает ли он в выходной"""
                    if dt(year, month, days).weekday() not in no_working:
                        viewcall += "<div class='col-days-today happy' id='undefined'>{0}</div>" . format(
                            days)
                    else:
                        """Подсвечиваем сегодняшний день"""
                        viewcall += "<div class='col-days-today btn btn-primary' id='{0}'>{1}</div>" . format(
                            now.strftime("%d-%m-%Y"), days)
                else:
                    """Выбираем выходные дни"""
                    if dt(year, month, days).weekday() not in no_working:
                        viewcall += "<div class='col-days happy' id='undefined'>{0}</div>" . format(
                            days)
                    else:
                        viewcall += "<div class='col-days btn btn-primary' id='{0}-{1}-{2}'>{3}</div>" . format(
                            days, month, year, days)
    viewcall += "<div class='col-12 button-style get-today'>Сегодня</div>"
    viewcall += "</div></div>"

    return viewcall
