VA_NAME = "Rapid information communicator optimizer-RICO v.3.0.0"
VA__SHORT_NAME = "Рико / RICO"

VA_VER = "3.0.0"

VA_TYPE = {
    "type_cmd": (
        "напиши",
        "печать",
        "написать",
        "напечатать",
        "напечатай",
        "напечатаем",
        "напечатает",
        "пиши",
        "напиш",
        "напишы",
    ),
}

VA_CREATE = {
    "create_workflow": (
        "список дел",
        "в список дел",
        "добавь в список дел",
        "запиши в список дел",
        "напиши в список дел",
        "добавь в список дел на день",
        "добавь в список дел на вечер",
    ),
}

VA_REMID = {
    "remind_cmd": (
        "напомни",
        "напомни мне",
        "напомнить",
        "напоминание",
        "напоминать",
        "напомним",
    ),
}

VA_YASearch = {
    "search_cmd": ("поиск", "найди", "найти"),  # Поиск
}

VA_WIKI = {
    "wiki_cmd": ("что такое",),
}

VA_ALIAS = (
    "рико",
    "рик и",
    "и",
    "рика",
    "рик",
    "река",
    "арика",
    "норико",
    "века",
    "вика",
    "рейка",
    "марика",
)

VA_TBR = (
    "скажи",
    "покажи",
    "ответь",
    "произнеси",
    "расскажи",
    "сколько",
    "поставь",
    "нажми",
)

VA_CMD_LIST = {
    "joke_cmd": ("расскажи анекдот", "aнекдот", "шутка", "пошути", "анекдот"),
    #! Статус Рико
    # Остановка программы
    "exit_cmd": ("выход", "рико выход", "выйти", "вахт"),
    "help": (
        "Что ты умеешь?",
        "Твои функции",
        "Перечисли свои функции",
    ),  # Перечислить функции
    #! Команды для записи и озвучивания списка дел
    "check_workflow": (
        "озвучь список дел",
        "список дел",
        "список дел на день",
        "список дел на вечер",
        "озвучь список дел на день",
        "озвучь список дел на вечер",
    ),
    "open_workflow": (
        "открой список дел",
        "покажи список дел",
        "открой список дел на день",
        "покажи список дел на день",
        "открой список дел на вечер",
        "покажи список дел на вечер",
    ),
    #! Команды для голосового ввода текста
    "enter_cmd": ("энтер", "интер", "интэр", "ентер", "ынтер", "кндр"),
    "question_mark_cmd": (
        "знак вопроса",
        "вопросительный знак",
        "вопрос",
        "вопроса",
        "вопросы",
    ),
    "space_cmd": ("пробел", "поставь пробел"),
    "text_delete_cmd": (
        "стереть всё",
        "удалить всё",
        "убрать всё",
        "всё стереть",
        "сотри весь текст",
        "сотри это",
        "сотри всё",
    ),
    "simbol_delete_cmd": (
        "сотри символ",
        "сотри символов",
        "сотри символы",
        "удали символы",
        "сотри символ",
    ),
    #! Команды для ОС
    "escape_cmd": (
        "закрыть",
        "всё закрыть",
        "закрыть окно",
        "закрой это",
    ),  # Закрыть окно
    "time_cmd": ("время", "скажи время"),  # Сообщить текущее время
    # Перевод окна на левый экран
    "window_to_left": ("левый", "лево", "влево", "окно налево"),
    # Перевод окна на правый экран
    "window_to_right": ("правый", "право", "вправо", "окно направо"),
    "window_full_screenOnn": (
        "разверни",
        "развернуть",
        "развернуться",
        "фулскрин",
    ),  # Развернуть окно на фулскрин
    # Свернуть окно
    "window_full_screenOff": ("cверни", "cвернуть", "свернуться"),
    #! Браузер
    "close_current_page_cmd": (
        "закрыть вкладку",
        "закрой эту вкладку",
        "убрать",
        "закрой вкладке",
    ),
    "page_upd_cmd": (
        "обнови",
        "обнови страницу",
        "обновить",
    ),  # Обновить страницу в браузере
    "open_browser": ("браузер", "браузр"),  # Открыть браузер
    #! Погода
    "weather_cmd": ("скажи погоду", "погода"),
    "create_new_page_cmd": (
        "новую",
        "создай новую вкладку",
        "открой новую вкладку",
        "открой ещё одну вкладку",
    ),
    "open_vk": ("вконтакте", "вконтакте"),  # Открыть страницу вк
    #! Программы
    "work_cmd": ("начало работы", "работа", "работать"),
    "vs_open": ("открой редактор кода", "код", "запусти редактор кода"),
    "telegram_cmd": (
        "телеграм",
        "открой телеграм",
        "телеграма",
        "телега",
        "запусти телегу",
        "запусти телеграм",
    ),
    "schedule_cmd": (
        "открой график",
        "открой папку с графиком",
        "открой расписание",
        "покажи расписание",
        "покажи график",
    ),
    "calculator_cmd": ("открой калькулятор", "калькулятор", "открыть калькулятор"),
    #! Плеер
    "play_music_cmd": ("музыку", "включи музыку", "играть музыку"),
    "next_track_cmd": ("следующий трек", "переключи трек"),
    "last_track_cmd": (
        "трек назад",
        "прошлый трек",
        "предыдущий трек",
        "предидущий трек",
    ),
    "mute_player_cmd": (
        "звук стоп",
        "замьють",
        "мут",
        "замутай",
        "мьют",
        "пауза",
        "поставь на паузу",
    ),
    "player_play_cmd": ("звук включить", "размут", "воспроизводи", "воспроизведи"),
    #! Динамики/Наушники
    "headphones_cmd": (
        "наушники",
        "включи наушники",
        "переведи на наушники",
        "звук в наушники",
    ),
    "speakers_cmd": (
        "динамики",
        "включи динамики",
        "переведи на динамики",
        "звук в динамики",
    ),
    # ? Установить Звук в %
    "volume_set_cmd": (
        "звук процентов",
        "громкость",
        "установи громкость на",
        "громкость звука",
        "громкость процентов",
    ),
    #! Распорядок дня из Exel таблицы
    "time_management_cmd": (
        "что по плану?",
        "что по графику?",
        "распорядок",
        "что по распорядку?",
        "Что по расписанию?",
        "сверь расписание",
    ),
}

VA_BEH = {
    # TODO: Поведение
    "thanks_cmd": ("спасибо тебе", "спасибо"),
    "hello_cmd": (
        "привет",
        "прив",
        "приветище",
        "превет",
        "прэвет",
        "прывет",
        "прэветище",
        "приветик",
        "здравствуй",
        "здарова",
        "здорова",
    ),
    "status_check_cmd": ("ты здесь?", "ты тут?"),
    "praise_cmd": ("ты молодец", "умница", "ты умница", "молец", "молодца"),
    "rude": (
        "блять",
        "гавно",
        "жопа",
        "ну ёбаный в рот",
        "ёбаный в рот",
        "ёб твою",
        "пиздец",
        "какого хуя",
        "хуй",
        "чмо",
        "бля",
        "сука",
        "ебать",
        "ахуеть",
        "пизда",
        "ни хуя себе",
        "иди в баню",
    ),
}
