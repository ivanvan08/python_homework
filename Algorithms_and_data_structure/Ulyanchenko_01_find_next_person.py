"""
created on: 18/01/2026
created by: @author: Ulyanchenko Ivan
"""
from typing import Optional

PERSON_LIST = [
    'Андрієнко Олег Сергійович',
    'Безуглий Іван Петрович',
    'Бондаренко Віталій Миколайович',
    'Веремій Роман Олександрович',
    'Гаврилюк Михайло Петрович',
    'Гончарук Богдан Віталійович',
    'Даниленко Степан Ігорович',
    'Дорошенко Богдан Андрійович',
    'Журавель Артем Євгенович',
    'Журавель Олексій Дмитрович',
    'Захарченко Анатолій Вікторович',
    'Зінченко Володимир Павлович',
    'Зінченко Петро Олексійович',
    'Кириленко Микита Юрійович',
    'Климчук Назар Анатолійович',
    'Коваленко Олександр Сергійович',
    'Кравченко Юрій Вікторович',
    'Леоненко Станіслав Дмитрович',
    'Лисенко Вадим Євгенович',
    'Литвин Сергій Борисович',
    'Марченко Ростислав Васильович',
    'Матвієнко Владислав Олексійович',
    'Мельник Василь Павлович',
    'Мороз Валентин Олександрович',
    'Нестеренко Євген Олексійович',
    'Нікітенко Юрій Вікторович',
    'Олійник Артем Леонідович',
    'Опанасюк Андрій Григорович',
    'Павленко Олександр Романович',
    'Петренко Андрій Володимирович',
    'Поліщук Сергій Іванович',
    'Пономаренко Тимофій Ігорович',
    'Романенко Ігор Анатолійович',
    'Руденко Дмитро Васильович',
    'Рябченко Денис Григорович',
    'Савченко Арсеній Романович',
    'Семенюк Антон Григорович',
    'Сидоренко Максим Ігорович',
    'Сєдов Богдан Миколайович',
    'Тарасенко Богуслав Миколайович',
    'Ткаченко Олег Романович',
    'Ткачук Віталій Іванович',
    'Ульянченко Вадим Олегович',
    'Усенко Вячеслав Павлович',
    'Федоренко Олексій Борисович',
    'Фесенко Єгор Петрович',
    'Філіпенко Назарій Володимирович',
    'Харченко Ілля Андрійович',
    'Ходаківський Максим Андрійович',
    'Хоменко Володимир Петрович',
    'Цапенко Іван Володимирович',
    'Цимбалюк Едуард Олегович',
    'Чорненко Тарас Вікторович',
    'Шаповал Олександр Михайлович',
    'Шевченко Дмитро Олегович',
    'Юрченко Кирило Леонідович',
    'Яковенко Валерій Артемович',
    'Ярошенко Владислав Іванович',
]


def binary_search(data, target, low, high):
    mid = (low + high) // 2
    while low <= high:
        if data[mid] == target:
            if mid < len(data) - 1:
                return data[mid + 1]
            return None
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


def find_next_person(name: str) -> Optional[str]:
    """
    TODO: I chose to use binary search, couse I found out how to use it in 3SUM task. I think that this task may work
    TODO: faster if we'll use dict with key of ПІБ and value of next person (speed must be O(1)). Also I could use some
    TODO: mods for binary search, like interpolation. We have 33 letters and if code ll have second letter, it will
    TODO: create a proportion (2 to 33 apon searchable index to len(data) - 1) and start main cycle from guessed index.
    TODO: So, my binary search uses - data (list in which we contain names to search), target (name which we comparing
    TODO: to find next one), low and high (fist and last index of data to search from and to, now, when I'm thinking
    TODO: about this, I shouldn't relly add low, couse in this particular task we anyway should check out all).
    TODO: Calculating middle value. In infinite loop if current name (in first run middle) equal name we have and if
    TODO: this name index smaller than last index of our list (so next name exists) - it return next name. If there no
    TODO: next name or there are no name in list - return None (as in struction). Other part - default binary search
    TODO: skript. If the word has lower latter order in alphabet meaning compare to ours - we'll not consider the
    TODO: first part of the list (in fist run, and the first part of the part that left after few cycles after the first
    TODO: run) and ll made one more run. And if word has higher letter - we'll not consider the second part (everything
    TODO: else will be like in situation with lower latter order). Then I just call function inside find_next_person and
    TODO: return the result

    TODO: In my method it'll be O(log n) and with interpolation mode - idn (faster, but i dont know the functioo). Im
    TODO: too brain-dead to find it out rn, but will now it before next class
    :param name: name of the person
    :return: name of the person next of the provided person in the PERSON_LIST.
    If there is no next person, the function returns None
    """
    # TODO: implement this function - done
    return binary_search(PERSON_LIST, name, 0, len(PERSON_LIST) - 1)


if __name__ == '__main__':
    # test cases
    name = find_next_person('Руденко Дмитро Васильович')
    assert name == 'Рябченко Денис Григорович'

    name = find_next_person('Зінченко Петро Олексійович')
    assert name == 'Кириленко Микита Юрійович'

    name = find_next_person('Андрієнко Олег Сергійович')
    assert name == 'Безуглий Іван Петрович'

    name = find_next_person('Ярошенко Владислав Іванович')
    assert name is None

    name = find_next_person('Невідома Людина')
    assert name is None

    print('All tests passed successfully')
