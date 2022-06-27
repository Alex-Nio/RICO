import openpyxl
import datetime
import calendar
import tts
from num2t4ru import num2text


now = datetime.datetime.now()  # 2022-06-20 15:43:18.024803
current_occ = []  # Список занятий
days = {
    "Mon": ["C3", "C31"],
    "Tue": ["E3", "E31"],
    "Wed": ["G3", "G31"],
    "Thu": ["I3", "I31"],
    "Fri": ["K3", "K31"],
}

# Format date
def date_formatting(string):
    string = list(string)
    count = 0
    for letter in string:
        if letter == "-":
            string[count] = "."
        count += 1

    string = "".join(string)
    return string


time = now.time()
time = time.strftime("%H:%M")

mydate = date_formatting(str(now.date()))  # Текущая дата в нужном формате
currentDay = datetime.datetime.strptime(mydate, "%Y.%m.%d")  # Текущий день
currentDay = calendar.day_abbr[currentDay.date().weekday()]  # Получили день недели

book = openpyxl.open("E:\\Работа\\Статистика\\ГРАФИК.xlsx", read_only=True)
sheet = book.active

# ? Получаем список занятий из графика
for row in range(3, 31):
    val = sheet[row][0].value
    current_occ.append(val)

# ? Получаем ячейки в этом дне (Понедельник)
def time_filter(date, time, daysDict):
    now_day = date  # Mon
    now_time = time  # 16:37:19
    dayDict = daysDict
    for key, value in dayDict.items():
        if key == now_day:
            val_to_find = value  # "C3","C31"
    return val_to_find


# ? Результат time_filter
cells = time_filter(currentDay, time, days)

cells_start = cells[0]  # первая часть
cells_end = cells[1]  # вторая часть

# склеиваем и кладём в переменную
time_list_data = sheet[cells_start:cells_end]  # Ячейки в текущем дне недели

# ? Принимает Ячейки, текущее время, список занятий
def occ_check(timeData, nowTime, occList):
    count = 0
    box = []
    for i in timeData:
        count += 1
        # print(i[0].value[0:5])

        # ? EXEL 1 TIME. Диапазон 1
        hour = int(i[0].value[0:2])
        hour_sec = (hour * 60) * 60
        minutes = int(i[0].value[3:5])
        minutes_sec = minutes * 60
        # print(str(hour) + " часы до")
        # print(str(minutes) + " минуты до")

        # ? NOW TIME
        now_hour = int(nowTime[0:2])
        now_hour_sec = (now_hour * 60) * 60
        now_minutes = int(nowTime[3:5])
        now_minutes_sec = now_minutes * 60
        # print(str(now_hour) + " часы сейчас")
        # print(str(now_minutes) + " минуты сейчас")

        # ? EXEL 2 TIME. Диапазон 2
        exel_diaposone_hours = int(i[0].value[6:8])
        exel_diaposone_hours_sec = (exel_diaposone_hours * 60) * 60
        exel_diaposone_minutes = int(i[0].value[9:11])
        exel_diaposone_minutes_sec = exel_diaposone_minutes * 60
        # print(str(exel_diaposone_hours) + " часы после")
        # print(str(exel_diaposone_minutes) + " минуты после")

        exelTimeSec = hour_sec + minutes_sec
        exelDiapTimeSec = exel_diaposone_hours_sec + exel_diaposone_minutes_sec
        currentTimeSec = now_hour_sec + now_minutes_sec

        # ? Находим что у нас в расписании в диапазоне от количества сек --- до количества сек
        if exelTimeSec <= currentTimeSec <= exelDiapTimeSec:
            # print('Время в диапазоне!')
            # print(str(count+2) + " Ячейка")
            # print(occList[count-1])
            currentPoint = str(occList[count - 1])
            a = num2text(exel_diaposone_hours)
            b = num2text(exel_diaposone_minutes)

            # ? Падеж для часов
            c = list(a)
            cCount = 0
            for x in c:
                cCount += 1
                if x == "ь":
                    c[cCount - 1] = "и"

            c = "".join(c)

            # ? Падеж для минут
            d = list(b)
            dCount = 0
            for x in d:
                dCount += 1
                if x == "ь":
                    d[dCount - 1] = "и"

            d = "".join(d)
            # print(d) # результат

            # ? Результат
            result = f"Сейчас по плану: {currentPoint} до {c} часов {b} минут."
            tts.va_speak(result)
            break
        else:
            pass
            # print('Время НЕ в диапазоне!')

    print(nowTime + " Текущее время")


# occ_check(time_list_data, time, current_occ) # Запускается при команде из основного файла
