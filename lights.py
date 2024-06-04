def total_burning_hours(c1, b1):
    total_hours = 0
    current_lights = c1
    extinct_lights = 0

    if b1 <= 2:
        print("Error, infinity recursion")
        return 0

    while current_lights > 0:
        # Каждый огонек горит 2 часа
        total_hours += current_lights * 2
        extinct_lights += current_lights
        current_lights = 0

        # Из b1 потухших огоньков делаем 2 новых огонька
        if extinct_lights >= b1:
            new_lights = (extinct_lights // b1) * 2
            extinct_lights = extinct_lights % b1
            current_lights += new_lights
    # Разделим количество часов на изнчально количество огоньков, чтобы узнать среднее время горения одного огонька
    print(total_hours / c1, "hours")
    return 0


# Пример использования функции
c1 = 10  # начальное количество огоньков
b1 = 3  # необходимое количество потухших огоньков для создания 2 новых
# Вывод среднего времени горения одного огоька в часах
total_burning_hours(c1, b1)