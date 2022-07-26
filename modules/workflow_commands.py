from modules import tts  # pylint: disable=ungrouped-imports
from modules import workflow_functions as wf

# ? Напоминание
def execute_workflow_cmd(cmd: str, voice: str, new_data, counter):
    try:
        if cmd == "create_workflow":
            print("Команда create_workflow выполнена успешно!")
            wf.myfunc()
    # ? Обработка ошибки если не выполнен запуск программы по ключевым словам
    except NameError:
        tts.va_speak("Произошла ошибка во время выполнения команды")
