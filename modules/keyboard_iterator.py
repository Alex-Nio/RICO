import keyboard


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
