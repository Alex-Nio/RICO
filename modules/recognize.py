from ru_word2number import w2n
from fuzzywuzzy import fuzz
import config
from modules import tts
from modules import all_commands
from modules import beh_commands
from modules import type_commands
from modules import reminder
from modules import num_checker


# ? Распознователь голоса
def recognize_cmd(cmd: str):
    rc = {"cmd": "", "percent": 60}  # pylint: disable=invalid-name

    for c, v in config.VA_TYPE.items():  # pylint: disable=invalid-name
        for x in v:  # pylint: disable=invalid-name
            vrt = fuzz.partial_ratio(cmd, x)
            # vrt = fuzz.ratio(cmd, x)
            if vrt > rc["percent"]:
                rc["cmd"] = c
                rc["percent"] = vrt

    for c, v in config.VA_REMID.items():  # pylint: disable=invalid-name
        for x in v:  # pylint: disable=invalid-name
            vrt = fuzz.partial_ratio(cmd, x)
            # vrt = fuzz.ratio(cmd, x)
            if vrt > rc["percent"]:
                rc["cmd"] = c
                rc["percent"] = vrt

    for c, v in config.VA_CMD_LIST.items():  # pylint: disable=invalid-name
        for x in v:  # pylint: disable=invalid-name
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc["percent"]:
                rc["cmd"] = c
                rc["percent"] = vrt

    for c, v in config.VA_BEH.items():  # pylint: disable=invalid-name
        for x in v:  # pylint: disable=invalid-name
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc["percent"]:
                rc["cmd"] = c
                rc["percent"] = vrt

    if rc['cmd'] != '':
        print(f'{rc} : Процент распознования' + "\n")

    return rc


# ? Анализируем список на наличие цифр
def value_checker(arr):
    # print(str(arr) + " Value checker entry")

    count = 0
    for i in arr:
        try:
            if arr[count] == "одну" or arr[count] == "эту" or arr[count] == "одно":
                arr[count] = "один"
            elif arr[count] == "две" or arr[count] == "дверь":
                arr[count] = "две"

            number_in_data = w2n.word_to_num(str(arr[count]))
            arr[count] = number_in_data  # возвращаем цифру
        except ValueError:
            pass
        except IndexError:
            pass
        except TypeError:
            pass
        count += 1

    return arr


#! Фильтр команд из конфига
def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for type_alias in config.VA_TYPE:
        cmd = cmd.replace(type_alias, "").strip()

    for type_alias in config.VA_REMID:
        cmd = cmd.replace(type_alias, "").strip()

    for alias_name in config.VA_ALIAS:
        cmd = cmd.replace(alias_name, "").strip()

    for tbr_name in config.VA_TBR:
        cmd = cmd.replace(tbr_name, "").strip()

    return cmd


# ? Распознование голоса
def va_respond(voice: str):
    if voice != '':
        print("Входящая строка: " + f'{voice}')  # строка

    data = voice.split()
    # ? Преобразуем буквы в строке в цифры и возвращаем новый список:
    new_data = value_checker(data)

    counter = num_checker.check_num(new_data)
    counter = int(counter)

    cmd = recognize_cmd(filter_cmd(voice))  # ! Фильтр.

    # ? Логгер команд
    if cmd["cmd"] != '':
        print("КОМАНДА---> " + " " + str(cmd["cmd"]))
        # print("ПРОЦЕНТ СОВПАДЕНИЙ---> " + " " + str(cmd["percent"]))

    #! Обращение к Рико
    if voice.startswith(config.VA_ALIAS):
        cmd = recognize_cmd(filter_cmd(voice))  # ! Фильтр.

        # ? Логгер команд
        # print("КОМАНДА---> " + " " + str(cmd["cmd"]))
        # print("ПРОЦЕНТ СОВПАДЕНИЙ---> " + " " + str(cmd["percent"]))

        a = cmd["cmd"] not in config.VA_TYPE
        b = cmd["cmd"] not in config.VA_CMD_LIST
        c = cmd["cmd"] not in config.VA_BEH
        d = cmd["cmd"] not in config.VA_REMID

        if (a and b and c and d):
            tts.va_speak("Не распознала, повтори пожалуйста")
        elif cmd["cmd"] in config.VA_TYPE:
            type_commands.execute_type_cmd(
                cmd["cmd"], voice, new_data, counter)
        elif cmd["cmd"] in config.VA_REMID:
            reminder.execute_reminder_cmd(
                cmd["cmd"], voice, new_data, counter)
        elif cmd["cmd"] in config.VA_BEH:
            beh_commands.execute_beh_cmd(cmd["cmd"])
        elif cmd["cmd"] in config.VA_CMD_LIST:
            all_commands.execute_cmd(cmd["cmd"], voice, new_data, counter)
