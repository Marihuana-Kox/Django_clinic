from datetime import datetime as dt, timedelta
import datetime


def free_days_week(day, month, year, medical, work_time):
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
    now = dt.now()
    today = now.today().strftime('%-d-%m-%Y')
    timelist = []
    val = work_time.values_list('time_work', flat=True)
    for i in val[0].split(','):
        timelist.append(i.strip())

    
    next_time = start_time = dt.time(dt.strptime(timelist[0], '%H:%M'))
    end_time = dt.time(dt.strptime(timelist[1], '%H:%M'))

    # next_time = start_time
    times = []
    while next_time < end_time:
        times.append(next_time)
        next_time = dt.time(dt.strptime(str(next_time), '%H:%M:%S') + datetime.timedelta(hours=1, minutes=0))


    if today == str(day)+'-'+str(month)+'-'+str(year):
        return f"Вы выбрали текущий день"
    
    context = "<h5><b>Вы выбрали:</b> %s</h5>" % (medical)
    context += "<div class='record-window'>Ждем вас, %s  %s %s г.</div>" % (day, months[month], year)
    context += "<div class='record-window'>Выберите удобное время:  </div>"
    
    for t in times:
        time = t.strftime('%H:%M')
        context += "<div class='select-time'>{}</div>" . format(''.join(time))
    
    context += "<div class='info-label'></div>"
    return context
