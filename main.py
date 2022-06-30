# made by Alex.
#! ███████████████████████████████████████████████
#! █────█───█────█────████─█─███───███────███────█
#! █─██─██─██─██─█─██─████─█─█████─███─██─███─██─█
#! █────██─██─████─██─████─█─███───███─██─███─██─█
#! █─█─███─██─██─█─██─████───█████─███─██─███─██─█
#! █─█─██───█────█────█████─██─█───█─█────█─█────█
#! ███████████████████████████████████████████████


# =================================================================
# =================================================================
# ============ NEW IMPORTS
# =================================================================
# =================================================================

import os
import sys
from threading import Thread
from psgtray import SystemTray
import PySimpleGUI as sg
import config
from modules import tts
from modules import stt
from modules import recognize


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


#! TRAY:
def tray():
    menu = ['', ['Открыть', 'Выход']]
    tooltip = 'Tooltip'
    default_text = '███████████████████████████████████████████████\n█────█───█────█────████─█─███───███────███────█\n█─██─██─██─██─█─██─████─█─█████─███─██─███─██─█\n█────██─██─████─██─████─█─███───███─██─███─██─█\n█─█─███─██─██─█─██─████───█████─███─██─███─██─█\n█─█─██───█────█────█████─██─█───█─█────█─█────█\n███████████████████████████████████████████████'

    layout = [
        [sg.Multiline(size=(120, 10), justification='center', font='Ubuntu', reroute_stdout=False,
                      reroute_cprint=False, write_only=True, key='-OUT-',
                      default_text=f'{default_text}',
                      background_color='#2d3436', text_color='#6c5ce7',
                      no_scrollbar=True)],
        [sg.B('Скрыть окно'), sg.Button('Выход')]]

    window = sg.Window('RICO v 3.0.0', layout, finalize=False,
                       enable_close_attempted_event=True, icon="icon.ico", background_color='#81ecec', margins=(20, 20))

    tray = SystemTray(menu, single_click_events=False, window=window,
                      tooltip=tooltip, icon="icon.ico")

    tray.show_message('Рико запук выполнен', 'Приятного пользования!')

    sg.cprint(sg.get_versions())

    # window.hide()
    tray.show_icon()
    while True:
        event, values = window.read()

        if event == tray.key:
            sg.cprint(f'System Tray Event = ',
                      values[event], c='white on red')
            # use the System Tray's event as if was from the window
            event = values[event]

        if event in (sg.WIN_CLOSED, 'Выход'):
            off = False
            break

        # ? Debugger
        # tray.show_message(title=event, message=values)
        # sg.cprint(event, values)

        if event in ('Открыть'):
            window.un_hide()
            window.bring_to_front()

        if event in ('Показать окно', sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED):
            window.un_hide()
            window.bring_to_front()
        elif event in ('Скрыть окно', sg.WIN_CLOSE_ATTEMPTED_EVENT):
            window.hide()
            tray.show_icon()

    tray.close()
    window.close()

    while True:
        if off is True:
            tts.va_speak("закрываюсь")
            os._exit()


if __name__ == '__main__':
    Thread(target=tray).start()

    #! Geetings Block

    print(f"{config.VA__SHORT_NAME} (v{config.VA_VER}) начал свою работу ...")
    # tts.va_speak("Привет! Я Р+и+ко. Твой голосовой асистент. Запуск выполнен.Что сделать?")

    #! End of Geetings Block

    # начать прослушивание команд
    stt.va_listen(recognize.va_respond)
