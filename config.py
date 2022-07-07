VA_NAME = "Rapid information communicator optimizer-RICO v.3.0.0"
VA__SHORT_NAME = "Рико / RICO"

VA_VER = "3.0.0"

VA_TYPE = {
    "type_cmd": ("рик и напиши", "напиши", "напиши", "написать", "напечатать", "пиши", "напиш", "напишы"),
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
    #! Статус Рико
    # Остановка программы
    "exit_cmd": ("выход", "рико выход", "выйти", "вахт"),
    "help": (
        "Что ты умеешь?",
        "Твои функции",
        "Перечисли свои функции",
    ),  # Перечислить функции
    #! Команды для ОС
    "enter_cmd": ("энтер", "интер", "интэр", "ентер", "ынтер", "кндр"),
    "question_mark_cmd": ("знак вопроса", "вопросительный знак", "вопрос", "вопроса", "вопросы"),
    "text_delete_cmd": ("стереть всё", "удалить всё", "убрать всё", "всё стереть", "сотри весь текст", "сотри это"),
    "simbol_delete_cmd": ("сотри символ", "сотри символов", "сотри символы", "удали символы", "сотри символ"),
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
    "close_current_page_cmd": ("закрыть вкладку", "закрой эту вкладку", "убрать", "закрой вкладке"),
    "page_upd_cmd": (
        "обнови",
        "обнови страницу",
        "обновить",
    ),  # Обновить страницу в браузере
    "open_browser": ("браузер", "браузр"),  # Открыть браузер
    "search_cmd": ("поиск", "найди", "найти"),  # Поиск
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
    "remind_cmd": ("напомни", "напомнить", "напомни мне", "напоминание", "напоминать", "напомним", "мне"),
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
    #! Распорядок из Exel таблицы
    # "time_management_open_cmd": ('график', 'расписание', 'открыть расписание', 'открыть график'),
    "time_management_cmd": (
        "что по плану?",
        "что по графику?",
        "распорядок",
        "что по распорядку?",
        "Что по расписанию?",
        "сверь расписание",
    ),
    # ? Установить Звук в %
    "volume_set_cmd": (
        "звук процентов",
        "громкость",
        "установи громкость на",
        "громкость звука",
        "громкость процентов",
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
}
