# Поведение *************************************

from modules import tts


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
