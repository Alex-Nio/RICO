# made by Alex.
#! ████─███─████─████────█─█──█────█───████
#! █──█──█──█──█─█──█────█─█─██───██───█──█
#! ████──█──█────█──█────█─█──█────█───█──█
#! █─█───█──█──█─█──█────███──█────█───█──█
#! █─█──███─████─████─────█───█─█──█─█─████

import webbrowser
import openpyxl
from timeManagement import *
from ru_word2number import w2n
from num2t4ru import num2text, decimal2text
import pyautogui

# import random
import datetime
import subprocess
import keyboard
import requests
import config
import stt
import tts
from fuzzywuzzy import fuzz
from num2t4ru import num2text
from bs4 import BeautifulSoup
import os
import sys
from sound import Sound  # будем использовать статические функции класса Sound


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


#! Geetings Block

print(f"{config.VA_NAME} (v{config.VA_VER}) начал свою работу ...")
# tts.va_speak("Привет! Я Р+и+ко. Твой голосовой асистент. Запуск выполнен.Что сделать?")

#! End of Geetings Block

# ? Склонение часов


def plural_rus_variant(x):
    last_two_digits = x % 100
    tens = last_two_digits // 10
    if tens == 1:
        return 2
    ones = last_two_digits % 10
    if ones == 1:
        return 0
    if ones >= 2 and ones <= 4:
        return 1
    return 2


def show_hours(hours):
    suffix = ["час", "часа", "часов"][plural_rus_variant(hours)]
    return "{0} {1}".format(hours, suffix)


# ? Склонение минут
def conv(n):
    es = ["а", "ы", ""]
    n = n % 100
    if n >= 11 and n <= 19:
        s = es[2]
    else:
        i = n % 10
        if i == 1:
            s = es[0]
        elif i in [2, 3, 4]:
            s = es[1]
        else:
            s = es[2]
    return s


def show_minutes(minutes):
    return "{} минут{}".format(minutes, conv(minutes))


# ? Распознование голоса
def va_respond(voice: str):
    print(voice)  # строка
    # print(type(voice.split())) # слово
    data = voice.split()
    # ? Преобразуем буквы в строке в цифры и возвращаем новый список:
    new_data = value_checker(data)

    cmd = recognize_cmd(filter_cmd(voice))  # ! Фильтр.

    # ? Логгер команд
    print("КОМАНДА---> " + " " + str(cmd["cmd"]))
    print("ПРОЦЕНТ СОВПАДЕНИЙ---> " + " " + str(cmd["percent"]))

    #! Обращение к Рико
    if voice.startswith(config.VA_ALIAS):
        cmd = recognize_cmd(filter_cmd(voice))  # ! Фильтр.

        # ? Логгер команд
        print("КОМАНДА---> " + " " + str(cmd["cmd"]))
        print("ПРОЦЕНТ СОВПАДЕНИЙ---> " + " " + str(cmd["percent"]))

        if (
            cmd["cmd"] not in config.VA_CMD_LIST.keys()
            and cmd["cmd"] not in config.VA_BEH.keys()
        ):
            print("Не распознала, повтори пожалуйста")
            tts.va_speak("Не распознала, повтори пожалуйста")
        elif cmd["cmd"] in config.VA_BEH.keys():
            execute_beh_cmd(cmd["cmd"])
        elif cmd["cmd"] in config.VA_CMD_LIST.keys():
            execute_cmd(cmd["cmd"], voice, new_data)


# ? Распознователь голоса
def recognize_cmd(cmd: str):
    rc = {"cmd": "", "percent": 0}

    for c, v in config.VA_CMD_LIST.items():
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc["percent"]:
                rc["cmd"] = c
                rc["percent"] = vrt

    for c, v in config.VA_BEH.items():
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc["percent"]:
                rc["cmd"] = c
                rc["percent"] = vrt

    return rc


#! Фильтр команд из конфига
def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd


# ? Анализируем список на наличие цифр
def value_checker(list):
    print(str(list) + " Value checker entry")
    count = 0
    for i in list:
        try:
            if list[count] == "одну" or list[count] == "эту" or list[count] == "одно":
                list[count] = "один"
            elif list[count] == "две" or list[count] == "дверь":
                list[count] = "две"

            numberInData = w2n.word_to_num(str(list[count]))
            list[count] = numberInData  # возвращаем цифру
        except ValueError:
            pass
        except IndexError:
            pass
        except TypeError:
            pass
        count += 1

    print(str(list) + " Value checker returned list")
    return list


# ? Проверка есть ли цифры в голосовом запросе
def check_num(list):
    data_to_check = list
    data_to_check = str(data_to_check)
    print(data_to_check + "----текущий список в проверке на числа")
    data_with_numbers = value_checker(data_to_check)
    print(str(data_with_numbers) + "----res")
    num = ""
    for i in data_with_numbers:
        if (
            i.isdigit() == True
        ):  # TODO: Тут нужно добавить если следующая буква-цифра т.е. i + 1 ? Сложить цифры
            num = num + i  # Вычисляем количество нажатий

    print(str(num) + "------Число которое передаётся в функцию")
    return num


# ? Вычисляем нужное количество нажатий клавиатуры
def keyboard_press_val(i, fun):
    try:
        print(str(i) + "-----число которое принимает функция")
        i = int(i)
        print(i)
        [fun("ctrl+w") for x in range(i)]
    except ValueError:
        fun("ctrl+w")


# ? Нажимаем нужную клавишу
def keyboard_press_key(key):
    print(key + " нажатие клавиш")
    keyboard.press_and_release(key)


# ? Менеджер команд
def execute_cmd(cmd: str, voice: str, new_data):
    # тут хранится вся голосовая команда с цифрой для количества повторений
    data_with_numbers = new_data
    try:
        #! Статус для Рико
        # ? Закрыть программу RICO
        if cmd == "exit_cmd":
            tts.va_speak("закрываюсь")
            sys.exit()
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
            keyboard_press_key("alt+f4")
            tts.va_speak("закрыла")
        # ? Время
        elif cmd == "time_cmd":
            now = datetime.datetime.now()
            text = (
                "Сей+час"
                + " "
                + num2text(now.hour)
                + " "
                + str(show_hours(now.hour))
                + " "
                + num2text(now.minute)
                + " "
                + str(show_minutes(now.minute))
            )
            tts.va_speak(text)
        # ? Окно налево
        elif cmd == "window_to_left":
            keyboard_press_key("ctrl+win+x")
            tts.va_speak("готово")
        # ? Окно направо
        elif cmd == "window_to_right":
            keyboard_press_key("ctrl+win+x")
            tts.va_speak("готово")
        # ? Фулскрин
        elif cmd == "window_full_screenOnn":
            keyboard_press_key("win+up")
            tts.va_speak("готово")
        # ? Свернуть окно
        elif cmd == "window_full_screenOff":
            keyboard_press_key("win+down")
            keyboard_press_key("win+down")
            tts.va_speak("готово")
        #! Браузер
        # ? Открыть браузер
        elif cmd == "open_browser":
            webbrowser.open("https://yandex.ru")
            tts.va_speak("открыла")
        # ? Открыть вк
        elif cmd == "open_vk":
            webbrowser.open("https://vk.com/eterfox")
            tts.va_speak("открыла")
        # ? Обновить страницу
        elif cmd == "page_upd_cmd":
            keyboard_press_key("ctrl+f5")
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
            push_counter = check_num(data_with_numbers)
            print(push_counter)
            keyboard_press_val(push_counter, keyboard_press_key)
            tts.va_speak("закрыла")
        # ? Новая вкладка
        elif cmd == "create_new_page_cmd":
            keyboard.press("ctrl+t")
            keyboard.release("ctrl+t")
            tts.va_speak("готово")
        #! Программы
        # ? Запуск программ
        elif cmd == "work_cmd":
            subprocess.Popen(
                r"C:\Users\Nio\AppData\Roaming\Zoom\bin\Zoom_launcher.exe")
            subprocess.Popen(r"D:\Programs\Telegram Desktop\Telegram.exe")
            subprocess.Popen(
                r"C:\Program Files (x86)\VMware\VMware Horizon View Client\vmware-view.exe"
            )
            tts.va_speak("запускаю программы ... Приятной работы")
        elif cmd == "schedule_cmd":
            subprocess.Popen(r"E:\Работа\Статистика\ГРАФИК.xlsx", shell=True)
            tts.va_speak("открыла")
        elif cmd == "calculator_cmd":
            subprocess.Popen(r"C:\Windows\system32\win32calc.exe", shell=True)
            tts.va_speak("открыла")
        # ? Запуск редактора кода
        elif cmd == "vs_open":
            subprocess.Popen(r"D:\Programs\Microsoft VS Code\Code.exe")
            tts.va_speak("редактор запущен")
        # ? Телеграм
        elif cmd == "telegram_cmd":
            subprocess.Popen(r"D:\Programs\Telegram Desktop\Telegram.exe")
            tts.va_speak("открыла")
        #! Плеер
        # ? Музыка
        elif cmd == "play_music_cmd":
            music_dir = r"C:\Users\Nio\Music\YEUZ, Paul Sabin - Stalk (Original Series Soundtrack)"
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
            pyautogui.press("nexttrack")
            tts.va_speak("переключаю")
        # ? Предыдущий трек <<
        elif cmd == "last_track_cmd":
            pyautogui.press("prevtrack")
            tts.va_speak("переключаю")
        # ? Пауза плеера ||
        elif cmd == "mute_player_cmd":
            pyautogui.press("playpause")
            tts.va_speak("пауза выполнена")
        # ? Запуск плеера ||
        elif cmd == "player_play_cmd":
            pyautogui.press("playpause")
            tts.va_speak("запускаю")
        # ? Звук
        elif cmd == "volume_set_cmd":
            volume_сounter = check_num(data_with_numbers)
            volume_сounter = int(volume_сounter)
            Sound.volume_set(volume_сounter)
        #! Динамики / Наушники
        elif cmd == "speakers_cmd":
            keyboard_press_key("alt+c")
            tts.va_speak("динамики включены")
        elif cmd == "headphones_cmd":
            keyboard_press_key("alt+v")
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
            current_weather = convert_weather_data(weather_data)
            current_weather = num2text(current_weather)
            result = f"В Белоозёрском сейчас: Плюс {current_weather} градусов."
            tts.va_speak(result)  # Произносим погоду
        #! Расписание
        elif cmd == "time_management_cmd":
            tts.va_speak("Открываю расписание... ...")
            occ_check(time_list_data, time, current_occ)
    # ? Обработка ошибки если не выполнен запуск программы по ключевым словам
    except NameError:
        tts.va_speak("Произошла ошибка во время выполнения команды")


#! TESTS:

# *****************************************************
# *****************************************************
# *****************************************************
# TODO: Поведение ************************************* # pylint: disable=no-name-in-module
# *****************************************************
# *****************************************************
# *****************************************************


def execute_beh_cmd(cmd: str):
    try:
        # ? Благодарность
        if cmd == "thanks_cmd":
            tts.va_speak("Пожалуйста!")
        # ? Проверка
        elif cmd == "hello_cmd":
            tts.va_speak("Привет!")
        elif cmd == "status_check_cmd":
            tts.va_speak("Да да! я здесь!")
        elif cmd == "praise_cmd":
            tts.va_speak("Спасибо! Стараюсь!")
    # ? Обработка ошибки если не выполнен запуск программы по ключевым словам
    except NameError:
        tts.va_speak("Произошла ошибка во время выполнения команды")


# начать прослушивание команд
stt.va_listen(va_respond)
