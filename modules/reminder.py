from modules import tts  # pylint: disable=ungrouped-imports
from threading import Thread
import time as TIME
from num2t4ru import num2text
import config


# ? Напоминание
def execute_reminder_cmd(cmd: str, voice: str, new_data, counter):
    try:
        if cmd == "remind_cmd":
            remind_str = new_data
            remind_num = counter
            # список ['рик', 'и', 'напомни', 'мне', 'закрыть', 'окно', 'через', 15, 'минут']
            print(str(remind_str) + "---data")
            print(str(remind_num) + "---remind number")  # число

            def reminder(data, remind_num):  # data=строка с цифрами
                while True:
                    # Вычисляем количество минут
                    def calc_total_time(i, flag):
                        if flag == 1:
                            total_time = (i * 60) * 60
                        elif flag == 2:
                            total_time = i * 60
                        elif flag == 3:
                            total_time = i
                        return total_time

                    # Фильтруем напоминание
                    def filtration(data):
                        for x in data:
                            if x in config.VA_ALIAS:
                                data.remove(x)
                        for x in data:
                            if x == 'напомни' or x == 'напомнил':
                                data.remove(x)
                        for x in data:
                            if x == 'мне':
                                data.remove(x)
                        for x in data:
                            if x == 'и':
                                data.remove(x)
                        for x in data:
                            if type(x) == int:
                                data.remove(x)
                        return data

                    data = filtration(data)

                    # Проверяем вид времени

                    def total_time_calculation(data, remind_num):
                        for item in data:
                            if item in ("час", "часа"):
                                r_time_hours = 1
                                t_time = calc_total_time(
                                    remind_num, r_time_hours)
                            elif item in ("минут", "минуты"):
                                r_time_minutes = 2
                                t_time = calc_total_time(
                                    remind_num, r_time_minutes)
                            elif item in ("секунд", "секунды"):
                                r_time_sec = 3
                                t_time = calc_total_time(
                                    remind_num, r_time_sec)
                        return t_time

                    t_time = total_time_calculation(data, remind_num)

                    data = data[0:-2]
                    data = " ".join(data)
                    # тут мы получили количество секунд
                    print(str(data) + " last operation")
                    # print(t_time)  # тут мы получили количество секунд

                    tts.va_speak('Хорошо, запомнила')
                    sleep_rec(t_time, data)

            def sleep_rec(t_time, data):
                # Запуск таймера напоминания в потоке
                local_time = t_time
                TIME.sleep(local_time)
                t_time = num2text(t_time)
                tts.va_speak(
                    f'Напоминаю, нужно {data}, прошло {t_time} секунд')

            #! Тут производим передачу даты и запуск
            # # Создаём новый поток
            th = Thread(target=reminder, daemon=True,
                        args=(remind_str, remind_num,))
            th.start()
     # ? Обработка ошибки если не выполнен запуск программы по ключевым словам
    except NameError:
        tts.va_speak("Произошла ошибка во время выполнения команды")
