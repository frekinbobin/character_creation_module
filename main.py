# character_creation_module/main.py

from random import randint

# Новый импорт.
from graphic_arts.start_game_banner import graphic_arts
# импортируем функцию run_screensaver.
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class):
    """Docstring1."""
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон противнику {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс урон противнику {5 + randint(-3, -1)}')
    return char_name


def defence(char_name, char_class):
    """Docstring2."""
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return char_name


def special(char_name, char_class):
    """Docstring3."""
    if char_class == 'warrior':
        return (f'{char_name} применил умение «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return f'{char_name} применил умение «Защита {10 + 30}»'
    return char_name


def start_training(char_name, char_class):
    """Docstring4."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника,\n'
          ' defence — чтобы блокировать атаку противника или special \n'
          '— чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    """Docstring5."""
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, за которого \n'
                           'хочешь играть: Воитель — warrior, \n'
                           'Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. Сильный, \n'
                  'выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. Обладает \n'
                  'высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. Черпает \n'
                  'силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор,\n'
                               ' или любую другую кнопку, чтобы \n'
                               'выбрать другого персонажа ').lower()
    return char_class


def main() -> None:
    """Docstring6."""
    if __name__ =='__main__':
        print('Приветствую тебя, искатель приключений!')
        print('Прежде чем начать игру...')
        char_name = input('...назови себя: ')
        print(f'Здравствуй, {char_name}! '
              'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
        print('Ты можешь выбрать один из трёх путей силы:')
        print('Воитель, Маг, Лекарь')
        char_class = choice_char_class()
        print(start_training(char_name, char_class))

main()