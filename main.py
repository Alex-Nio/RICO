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
import os
import sys

def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
	return os.path.join(base_path, relative_path)

import webbrowser
import requests
import keyboard
import subprocess
import datetime
import random
import pyautogui
from num2t4ru import num2text, decimal2text

#! Geetings Block

print(f"{config.VA_NAME} (v{config.VA_VER}) начал свою работу ...")
# tts.va_speak("Привет! Я Р+и+ко. Для старта выполни запуск")

#! End of Geetings Block

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

#? Анализируем список на наличие цифр
def numbers_analizer(data:list):
	li = data
	print(str(li) + "---DATA")
	count = 0
	for i in li:
		count = count+1
		try:
			# print(str(i) + "---слово---" + str(count) + "---Позиция в строке")
			try:
				# Преобразуем слово в цифру
				li[count-1] = config.words[i]
				data = li
			except KeyError:
				try:
					print(config.words[count-count%10] + config.words[count%10].lower())
				except KeyError:
					pass # Number out of range error
			except IndexError:
				pass
		except TypeError:
			pass
	return data

#? Распознование голоса
def va_respond(voice: str):
	print(voice) # строка
	# print(type(voice.split())) # слово
	data = voice.split()
	#? Преобразуем буквы в строке в цифры и возвращаем новый список:
	new_data = numbers_analizer(data)

	#! Обращение к Рико
	if voice.startswith(config.VA_ALIAS):
		cmd = recognize_cmd(filter_cmd(voice)) #! Фильтр.Если включаем нужен таб на строки ниже
		# cmd = recognize_cmd(voice)
		#? Логгер команд
		print("КОМАНДА---> " + " " + str(cmd['cmd']))

		if cmd['cmd'] not in config.VA_CMD_LIST.keys():
			print("Не распознала, повтори пожалуйста")		
		else:
			execute_cmd(cmd['cmd'], voice, new_data)

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

#! Фильтр команд из конфига
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
	print(str(int) + "---NUMBER")
	if int == 0: 
		sleep = True
	elif int == 1:
		sleep = False
	elif int == 3:
		execute_cmd(cmd('sleep_cmd'), None)

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

#? Проверка есть ли цифры в голосовом запросе
def check_num(list):
	li = list
	li = str(li)
	print(li + "----текущий список в проверке на числа")
	for n in li:
		if n.isdigit():
			keyboard_press(n)

#? Инициируем нужное количество нажатий клавиатуры
def keyboard_press(i):
	i = int(i)
	print(type(i))
	count = i
	while count != 0:
		keyboard.press("ctrl+w")
		keyboard.release("ctrl+w")
		count -= 1
		print(str(count) + "COUNT After")

#? Менеджер команд
def execute_cmd(cmd: str, voice: str, new_data):
	new = new_data # тут хранится вся голосовая команда с цифрой для количества повторений
	try:
		#! Статус для Рико
		#? Просыпаемся
		if cmd == 'wake_cmd':
			set_sleep_status(1)
			tts.va_speak("Запуск выполнен.Что сделать?")
		#? Ожидание/режим сна
		elif sleep == False and cmd == 'sleep_cmd':
			set_sleep_status(0)
			tts.va_speak("хорошо, жду")
		#? Закрыть программу RICO
		elif cmd == 'exit_cmd':
			tts.va_speak("закрываюсь")
			sys.exit()
		#? Основные функции/Помощь
		if sleep == False and cmd == 'help':
			text = "Я умею: ..."
			text += "произносить время ..."
			text += "управлять расположением ок+он ..."
			text += "открывать браузер ..."
			text += "закрывать вкладки в нужном количестве ..."
			text += "закрывать открытые о+кна ..."
			text += "открывать редактор кода ..."
			text += "переключать звук и сообщать погоду ..."
			text += "искать через Яндекс  поиск ..."
			text += "открывать Телеграм ..."
			text += "запускать программы ..."
			text += "для старта скажи-  Рико  запуск ..."
			text += "для выхода скажи  Выход ..."
			text += "Пока это всё, что я умею, но мне нужно учиться"
			tts.va_speak(text)
			pass
		#? Сброс режима ожидания
		if cmd == 'status_check_cmd':
			set_sleep_status(1)
			tts.va_speak("Да да! я здесь!")
		#! ОС Команды
		#? Закрыть окно
		elif sleep == False and cmd == 'escape_cmd':
			keyboard.press("alt+f4")
			keyboard.release("alt+f4")
			tts.va_speak("закрыла")
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
		#! Браузер
		#? Открыть браузер
		elif sleep == False and cmd == 'open_browser':
			webbrowser.open('https://yandex.ru')
			tts.va_speak("открыла")
		#? Открыть вк
		elif sleep == False and cmd == 'open_vk':
			webbrowser.open('https://vk.com/eterfox')
			tts.va_speak("открыла")
		#? Обновить страницу
		elif sleep == False and cmd == 'page_upd_cmd':
			keyboard.press("ctrl+f5")
			keyboard.release("ctrl+f5")
			tts.va_speak("обновлено")
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
			#! Выполняем количество голосовых задач
			check_num(new)
			tts.va_speak("закрыла")
		#? Новая вкладка
		elif sleep == False and cmd == 'create_new_page_cmd':
			keyboard.press("ctrl+t")
			keyboard.release("ctrl+t")
			tts.va_speak("готово")
		#! Программы
		#? Запуск программ
		elif sleep == False and cmd == 'work_cmd':
			subprocess.Popen(r'C:\Users\Nio\AppData\Roaming\Zoom\bin\Zoom_launcher.exe')
			subprocess.Popen(r'D:\Programs\Telegram Desktop\Telegram.exe')
			subprocess.Popen(r'C:\Program Files (x86)\VMware\VMware Horizon View Client\vmware-view.exe')
			tts.va_speak("запускаю программы ... Приятной работы")
		#? Запуск редактора кода
		elif sleep == False and cmd == 'vs_open':
			subprocess.Popen(r'D:\Programs\Microsoft VS Code\Code.exe')
			tts.va_speak("редактор запущен")
		#? Телеграм
		elif sleep == False and cmd == 'telegram_cmd':
			subprocess.Popen(r'D:\Programs\Telegram Desktop\Telegram.exe')
			tts.va_speak("открыла")
		#! Плеер
		#? Музыка
		elif sleep == False and cmd == 'play_music_cmd':
			music_dir = (r'C:\Users\Nio\Music\YEUZ, Paul Sabin - Stalk (Original Series Soundtrack)')
			songs = os.listdir(music_dir)
			print(str(len(songs)) + "---треков")
			count = 0
			for i in songs:
				count += 1
				print(f'{count}.{i}')

			os.startfile(os.path.join(music_dir, songs[0]))
			tts.va_speak("Музыка запущена")
		#? Следующий трек >>
		elif sleep == False and cmd == 'next_track_cmd':
			pyautogui.press('nexttrack')
			tts.va_speak("переключаю")
		#? Предыдущий трек <<
		elif sleep == False and cmd == 'last_track_cmd':
			pyautogui.press('prevtrack')
			tts.va_speak("переключаю")
		#? Пауза плеера ||
		elif sleep == False and cmd == 'mute_player_cmd':
			pyautogui.press('playpause')
			tts.va_speak("пауза выполнена")
		#? Запуск плеера ||
		elif sleep == False and cmd == 'player_play_cmd':
			pyautogui.press('playpause')
			tts.va_speak("запускаю")
		#! Динамики / Наушники
		elif sleep == False and cmd == 'speakers_cmd':
			keyboard.press("alt+c")
			keyboard.release("alt+c")
			tts.va_speak("динамики включены")
		elif sleep == False and cmd == 'headphones_cmd':
			keyboard.press("alt+v")
			keyboard.release("alt+v")
			tts.va_speak("наушники включены")
		elif sleep == False and cmd == 'weather_cmd':
			url = 'https://pogoda1.ru/beloozersky/' # url
			response = requests.get(url)
			soup = BeautifulSoup(response.text, 'lxml')
			data = soup.find_all('div', class_='weather-now-temp')
			weatherNowValue = []

			#? Берём данные о погоде
			def initiate_take_weatherData(data, weatherNowValue):
				print(data)
				for i in range(0, len(data)):
					weatherNowValue.append(data[i].text)
					return weatherNowValue

			#? Превращаем нужные данные в число
			def convert_weatherData(data):
				num = ""
				for i in data:
					if i.isdigit():
						num = num + i
				return int(num)

			weatherDATA = initiate_take_weatherData(data, weatherNowValue)
			weatherDATA = str(weatherDATA)
			currentWeather = convert_weatherData(weatherDATA)
			currentWeather = num2text(currentWeather)
			result = f"В Белоозёрском сейчас: Плюс {currentWeather} градусов."
			tts.va_speak(result) # Произносим погоду
			#! END
	#? Обработка ошибки если не выполнен запуск программы по ключевым словам
	except NameError:
		tts.va_speak("Сперва нужно выполнить запуск")





# начать прослушивание команд
stt.va_listen(va_respond)