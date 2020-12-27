from datetime import datetime as dt


def free_days_week(day, month, year, medical, work_time):
    now = dt.now()
    today = now.today().strftime('%-d-%m-%Y')
    dayslist = []
    val = work_time.values_list('time_work', flat=True)
    for i in val[0].split(','):
        dayslist.append(int(i.strip()))

    working = [d for d in range(dayslist[0], dayslist[1])]
    if today == str(day)+'-'+str(month)+'-'+str(year):
        return f"Вы выбрали текущий день"
    context = f"Вы выбрали: {medical}. Ждем вас {year}-{month}-{day}, выберите удобное время {working}"
    return  context
