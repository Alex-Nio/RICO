# made by Alex.
#! ████─███─████─████────█─█────█───████───████
#! █──█──█──█──█─█──█────█─█───██───█──█───█──█
#! ████──█──█────█──█────█─█────█───█──█───█──█
#! █─█───█──█──█─█──█────███────█───█──█───█──█
#! █─█──███─████─████─────█──█──█─█─████─█─████

import config
import stt
import tts
from fuzzywuzzy import fuzz
from num2t4ru import num2text
from bs4 import BeautifulSoup
import sys
import webbrowser
import requests
import keyboard
import subprocess
import datetime
import random

print(f"{config.VA_NAME} (v{config.VA_VER}) начал свою работу ...")

#? Склонение часов
def pluralRusVariant(x):
	lastTwoDigits = x % 100
	tens = lastTwoDigits // 10
	if tens == 1:
		return 2
	ones = lastTwoDigits % 10
	if ones == 1:
		return 0
	if ones >= 2 and ones <= 4:
		return 1
	return 2

def showHours(hours):
	suffix = ["час", "часа", "часов"][pluralRusVariant(hours)]
	return "{0} {1}".format(hours, suffix)

#? Склонение минут
def conv(n): 
    es = ['а', 'ы', '']
    n = n % 100
    if n>=11 and n<=19:
        s=es[2] 
    else:
        i = n % 10
        if i == 1:
            s = es[0] 
        elif i in [2,3,4]:
            s = es[1] 
        else:
            s = es[2] 
    return s 

def showMinutes(minutes):
    return ('{} минут{}'.format(minutes, conv(minutes)))

#? Poisc 1.0
def search_init(voice: str):
	global search_str
	search_str = voice	

	return search_str

#? Распознование голоса
def va_respond(voice: str):
	print(voice)
	#!Отключено. обращаются к ассистенту
	if voice.startswith(config.VA_ALIAS):
		cmd = recognize_cmd(filter_cmd(voice)) #!Отключено.Фильтр.Если включаем нужен таб на строки ниже
		# cmd = recognize_cmd(voice)
		print("КОМАНДА---> " + " " + str(cmd['cmd']))

		if cmd['cmd'] not in config.VA_CMD_LIST.keys():
			print("Не распознала, повтори пожалуйста")		
		else:
			execute_cmd(cmd['cmd'], voice)

#? Распознователь голоса
def recognize_cmd(cmd: str):
	rc = {'cmd': '', 'percent': 0}
	for c, v in config.VA_CMD_LIST.items():

		for x in v:
			vrt = fuzz.ratio(cmd, x)
			if vrt > rc['percent']:
				rc['cmd'] = c
				rc['percent'] = vrt

	return rc

#!Выключен. Фильтр команд
def filter_cmd(raw_voice: str):
	cmd = raw_voice

	for x in config.VA_ALIAS:
		cmd = cmd.replace(x, "").strip()

	for x in config.VA_TBR:
		cmd = cmd.replace(x, "").strip()

	return cmd

#? Сон, Запуск переключение режимов
def set_sleep_status(int):
	global sleep
	sleep = bool
	
	if int == 0: 
		sleep = True
	elif int == 1:
		sleep = False

	return sleep

#? Фильтр поиска
def search_filter(search_str: str, cmd: str):
	if cmd == "search_cmd":
		for x in config.VA_ALIAS:
			search_str = search_str.replace(x, "").strip()
			print(search_str + "---2")
		for y in config.VA_CMD_LIST:
			print(search_str + "---search_str 1")
			search_str = search_str.replace(y, "").strip()

		return search_str
	else: print("Ошибка")

def execute_cmd(cmd: str, voice: str):
	try:
		#? Просыпаемся
		if cmd == 'wake_cmd':
			set_sleep_status(1)
			tts.va_speak("Запуск выполнен.Что сделать?")
		#? Пауза
		elif sleep == False and cmd == 'sleep_cmd':
			set_sleep_status(0)
			tts.va_speak("хорошо, жду")
		#? Закрыть программу
		elif cmd == 'exit_cmd':
			tts.va_speak("закрываюсь")
			sys.exit()
		#? Основные функции
		if sleep == False and cmd == 'help':
			text = "Я умею: ..."
			text += "произносить время ..."
			text += "управлять расположением ок+он ..."
			text += "открывать браузер ..."
			text += "закрывать вкладки и о+кна ..."
			text += "открывать редактор кода ..."
			text += "искать через Яндекс  поиск ..."
			text += "открывать Телеграм ..."
			text += "запускать программы ..."
			text += "для старта скажи-  Рико  запуск ..."
			text += "для выхода скажи  Выход ..."
			text += "Пока это всё, что я умею, но мне нужно учиться"
			tts.va_speak(text)
			pass
		#? Открыть вк
		elif sleep == False and cmd == 'open_vk':
			webbrowser.open('https://vk.com/eterfox')
			tts.va_speak("открыла")
		#? Открыть браузер
		elif sleep == False and cmd == 'open_browser':
			webbrowser.open('https://yandex.ru')
			tts.va_speak("открыла")
		#? Время
		elif sleep == False and cmd == 'time_cmd':
			now = datetime.datetime.now()
			text = "Сей+час" + " " + num2text(now.hour) + " " + str(showHours(now.hour)) + " " + num2text(now.minute) + " " + str(showMinutes(now.minute))
			tts.va_speak(text)
		#? Окно налево
		elif sleep == False and cmd == 'window_to_left':
			keyboard.press("ctrl+win+x")
			keyboard.release("ctrl+win+x")
			tts.va_speak("готово")
		#? Окно направо
		elif sleep == False and cmd == 'window_to_right':
			keyboard.press("ctrl+win+x")
			keyboard.release("ctrl+win+x")
			tts.va_speak("готово")
		#? Фулскрин
		elif sleep == False and cmd == 'window_full_screenOnn':
			keyboard.press("win+up")
			keyboard.release("win+up")
			tts.va_speak("готово")
		#? Свернуть окно
		elif sleep == False and cmd == 'window_full_screenOff':
			keyboard.press("win+down")
			keyboard.release("win+down")
			keyboard.press("win+down")
			keyboard.release("win+down")
			tts.va_speak("готово")
		#? Поиск Яндекс
		elif sleep == False and cmd == 'search_cmd':
			def get_search(search_str):
				search_str = search_filter(search_str, cmd)

				url = 'http://yandex.ru/yandsearch?text='
				print(url + str(search_str))

				if "поиск" in search_str:
					webbrowser.open(url + search_str.replace("поиск", ""))
				elif "найди" in search_str:
					webbrowser.open(url + search_str.replace("найди", ""))
				elif "найти" in search_str:
					webbrowser.open(url + search_str.replace("найти", ""))

				requests.get(url + search_str)

			cmd_search = search_init(voice)
			get_search(str(cmd_search))
			tts.va_speak("нашла")
		#? Закрыть вкладку
		elif sleep == False and cmd == 'close_current_page_cmd':
			keyboard.press("ctrl+w")
			keyboard.release("ctrl+w")
			tts.va_speak("закрыла")
		#? Новая вкладка
		elif sleep == False and cmd == 'create_new_page_cmd':
			keyboard.press("ctrl+t")
			keyboard.release("ctrl+t")
			tts.va_speak("готово")
		#? Запуск редактора кода
		elif sleep == False and cmd == 'vs_open':
			subprocess.Popen(r'D:\Programs\Microsoft VS Code\Code.exe')
			tts.va_speak("редактор запущен")
		#? Запуск приложений
		elif sleep == False and cmd == 'work_cmd':
			subprocess.Popen(r'C:\Users\Nio\AppData\Roaming\Zoom\bin\Zoom_launcher.exe')
			subprocess.Popen(r'D:\Programs\Telegram Desktop\Telegram.exe')
			subprocess.Popen(r'C:\Program Files (x86)\VMware\VMware Horizon View Client\vmware-view.exe')
			tts.va_speak("запускаю программы ... Приятной работы")
		#? Закрыть окно
		elif sleep == False and cmd == 'escape_cmd':
			keyboard.press("alt+f4")
			keyboard.release("alt+f4")
			tts.va_speak("закрыла")
		#? Телеграм
		elif sleep == False and cmd == 'telegram_cmd':
			subprocess.Popen(r'D:\Programs\Telegram Desktop\Telegram.exe')
			tts.va_speak("открыла")
	#? Обработка ошибки если не выполнен запуск программы по ключевым словам
	except NameError:
		tts.va_speak("Сперва нужно выполнить запуск")

# начать прослушивание команд
stt.va_listen(va_respond)