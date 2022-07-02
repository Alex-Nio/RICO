import subprocess
import datetime
import webbrowser
import os
import sys
from threading import Thread
import time as TIME
import pyautogui
import requests
from bs4 import BeautifulSoup
from num2t4ru import num2text
from modules import keyboard_iterator as KB
from exelviewer import *
from modules import tts  # pylint: disable=ungrouped-imports
import config
from modules import num_checker  # pylint: disable=ungrouped-imports
from modules import time_declination
from modules.sound import Sound
import settings


# ? Менеджер команд
def execute_cmd(cmd: str, voice: str, new_data):
    # тут хранится вся голосовая команда с цифрой для количества повторений
    data_with_numbers = new_data

    try:
        #! Статус для Рико
        # ? Основные функции/Помощь
        if cmd == "help":
            text = "Я умею: ..."
            text += "произносить время ..."
            text += "управлять расположением ок+он ..."
            text += "открывать браузер ..."
            text += "закрывать вкладки в нужном количестве ..."
            text += "закрывать открытые о+кна ..."
            text += "открывать редактор кода ..."
            text += "переключать звук и сообщать погоду ..."
            text += "искать информацию в интернете ..."
            text += "открывать Телеграм ..."
            text += "запускать программы ..."
            text += "говорить что по распорядку дня ..."
            text += "для старта назови меня по  +имени и скажи команду ..."
            text += "для выхода скажи  Выход ..."
            text += "Пока это всё, что я умею, но мне нужно учиться"
            tts.va_speak(text)
        #! ОС Команды
        # ? Закрыть окно
        elif cmd == "escape_cmd":
            KB.keyboard_press_key("alt+f4")
            tts.va_speak("закрыла")
        # ? Время
        elif cmd == "time_cmd":
            now = datetime.datetime.now()
            text = (
                "Сей+час"
                + " "
                + num2text(now.hour)
                + " "
                + str(time_declination.show_hours(now.hour))
                + " "
                + num2text(now.minute)
                + " "
                + str(time_declination.show_minutes(now.minute))
            )
            tts.va_speak(text)
        # ? Окно налево
        elif cmd == "window_to_left":
            KB.keyboard_press_key("ctrl+win+x")
            tts.va_speak("готово")
        # ? Окно направо
        elif cmd == "window_to_right":
            KB.keyboard_press_key("ctrl+win+x")
            tts.va_speak("готово")
        # ? Фулскрин
        elif cmd == "window_full_screenOnn":
            KB.keyboard_press_key("win+up")
            tts.va_speak("готово")
        # ? Свернуть окно
        elif cmd == "window_full_screenOff":
            KB.keyboard_press_key("win+down")
            KB.keyboard_press_key("win+down")
            tts.va_speak("готово")
        #! Браузер
        # ? Открыть браузер
        elif cmd == "open_browser":
            webbrowser.open(settings.browser_start_page)
            tts.va_speak("открыла")
        # ? Открыть вк
        elif cmd == "open_vk":
            webbrowser.open(settings.vk_start_page)
            tts.va_speak("открыла")
        # ? Обновить страницу
        elif cmd == "page_upd_cmd":
            KB.keyboard_press_key("ctrl+f5")
            tts.va_speak("обновлено")
        #! Поиск Яндекс
        elif cmd == "search_cmd":
            # ? YA Search
            def search_init(voice: str):
                search_str = voice
                print(search_str + "поисковый запрос")

                return search_str

            # ? Фильтр поиска
            def search_filter(search_str: str, cmd: str):
                if cmd == "search_cmd":
                    # Убираем имя помошника
                    for x in config.VA_ALIAS:
                        search_str = search_str.replace(x, "").strip()
                        print(search_str + " Поисковая строка без имени помощника")

                    return search_str
                else:
                    print("Ошибка")

            # ? Подставляем запрос в урл
            def get_search(search_str):
                search_str = search_filter(search_str, cmd)

                url = "http://yandex.ru/yandsearch?text="

                print(url + str(search_str) + " " + " --> Сформированный URL")
                # ? Убираем поисковое слово из строки
                if "поиск" in search_str:
                    webbrowser.open(url + search_str.replace("поиск", ""))
                elif "найди" in search_str:
                    webbrowser.open(url + search_str.replace("найди", ""))
                elif "найти" in search_str:
                    webbrowser.open(url + search_str.replace("найти", ""))

                print(search_str + " Поисковая строка без ключевого слова")
                # webbrowser.open(url)
                requests.get(url + search_str)

            search_req = search_init(voice)
            tts.va_speak("нашла")
            print(str(search_req) + " Поисковый запрос")
            get_search(str(search_req))
        # ? Закрыть вкладку
        elif cmd == "close_current_page_cmd":
            #! Выполняем количество голосовых задач
            push_counter = num_checker.check_num(data_with_numbers)
            print(push_counter)
            KB.keyboard_press_val(push_counter, KB.keyboard_press_key)
            tts.va_speak("закрыла")
        # ? Новая вкладка
        elif cmd == "create_new_page_cmd":
            KB.keyboard_press_key("ctrl+t")
            tts.va_speak("готово")
        #! Программы
        # ? Напоминание
        elif cmd == "remind_cmd":
            remind_str = data_with_numbers
            remind_num = num_checker.check_num(data_with_numbers)
            remind_num = int(remind_num)
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
                            if x == 'напомни':
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
                    print(t_time)  # тут мы получили количество секунд

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
        # ? Запуск программ
        elif cmd == "work_cmd":
            subprocess.Popen(settings.zoom_path)
            subprocess.Popen(settings.telegram_path)
            subprocess.Popen(settings.horizon_path)
            tts.va_speak("запускаю программы ... Приятной работы")
        elif cmd == "schedule_cmd":
            subprocess.Popen(settings.schedule_path, shell=True)
            tts.va_speak("открыла")
        elif cmd == "calculator_cmd":
            subprocess.Popen(settings.calculator_path, shell=True)
            tts.va_speak("открыла")
        # ? Запуск редактора кода
        elif cmd == "vs_open":
            subprocess.Popen(settings.vs_code_path)
            tts.va_speak("редактор запущен")
        # ? Телеграм
        elif cmd == "telegram_cmd":
            subprocess.Popen(settings.telegram_path)
            tts.va_speak("открыла")
        #! Плеер
        # ? Музыка
        elif cmd == "play_music_cmd":
            music_dir = settings.music_dir
            songs = os.listdir(music_dir)
            print(str(len(songs)) + "---треков")
            count = 0
            for i in songs:
                count += 1
                print(f"{count}.{i}")

            os.startfile(os.path.join(music_dir, songs[0]))
            tts.va_speak("Музыка запущена")
        # ? Следующий трек >>
        elif cmd == "next_track_cmd":
            tts.va_speak("переключаю")
            pyautogui.press("nexttrack")
        # ? Предыдущий трек <<
        elif cmd == "last_track_cmd":
            tts.va_speak("переключаю")
            pyautogui.press("prevtrack")
        # ? Пауза плеера ||
        elif cmd == "mute_player_cmd":
            pyautogui.press("playpause")
            tts.va_speak("пауза выполнена")
        # ? Запуск плеера ||
        elif cmd == "player_play_cmd":
            tts.va_speak("запускаю")
            pyautogui.press("playpause")
        # ? Установить звук в %
        elif cmd == "volume_set_cmd":
            volume_сounter = num_checker.check_num(data_with_numbers)
            volume_сounter = int(volume_сounter)
            Sound.volume_set(volume_сounter)
        #! Динамики / Наушники
        elif cmd == "speakers_cmd":
            KB.keyboard_press_key("alt+c")
            tts.va_speak("динамики включены")
        elif cmd == "headphones_cmd":
            KB.keyboard_press_key("alt+v")
            tts.va_speak("наушники включены")
        #! Погода
        elif cmd == "weather_cmd":
            url = "https://pogoda1.ru/beloozersky/"  # url
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "lxml")
            data = soup.find("div", class_="weather-now-temp")
            weather_now_value = []  # type: list[str]

            # ? Берём данные о погоде
            def initiate_take_weather_data(data, weather_now_value):
                weather_now_value.append(data.text)
                return weather_now_value

            # ? Превращаем нужные данные в число
            def convert_weather_data(data):
                num = ""
                for i in data:
                    if i.isdigit():
                        num = num + i
                return int(num)

            weather_data = initiate_take_weather_data(data, weather_now_value)
            weather_data = str(weather_data)
            # TODO: написать условие для + и для -
            print(weather_data + " Текущая погода")
            current_weather = convert_weather_data(weather_data)
            current_weather = num2text(current_weather)
            result = f"В Белоозёрском сейчас: Плюс {current_weather} градусов."
            tts.va_speak(result)  # Произносим погоду
        #! Расписание
        elif cmd == "time_management_cmd":
            tts.va_speak("Открываю расписание... ...")
            occ_check(time_list_data, time, current_occ)
        # ? Закрыть программу RICO
        if cmd == "exit_cmd":
            tts.va_speak("закрываюсь")
            os._exit(1)
    # ? Обработка ошибки если не выполнен запуск программы по ключевым словам
    except NameError:
        tts.va_speak("Произошла ошибка во время выполнения команды")
