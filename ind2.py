#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариаент 18
# Из лабораторной работы 8 необходимо дополнительно
# реализовать сохранение и чтение данных из файла формата JSON.
# Необходимо проследить за тем, чтобы файлы генерируемый этой
# программой не попадали в репозиторий лабораторной работы.

import sys
import json

if __name__ == '__main__':
    # Список работников.
    market = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные .
            shop = input("Название магазина? ")
            product = input("Название товара? ")
            price = float(input("Стоимость товара в руб.? "))

            # Создать словарь.
            markets = {
                'shop': shop,
                'product': product,
                'price': price,
            }

            # Добавить словарь в список.
            market.append(markets)
            # Отсортировать список в случае необходимости.
            if len(market) > 1:
                market.sort(key=lambda item: item.get('shop', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                    "No",
                    "Магазин",
                    "Товар",
                    "Стоимость в руб."
                )
            )
            print(line)

            # Вывести данные о всех товарах.
            for idx, markets in enumerate(market, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                        idx,
                        markets.get('shop', ''),
                        markets.get('product', ''),
                        markets.get('price', 0)
                    )
                )

            print(line)


        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            sel = (parts[1])

            count = 0
            for markets in market:
                if markets.get('shop') == sel:

                    count += 1
                    print(
                        '{:>4}: {}'.format(count, markets.get('shop', ''))
                    )
                    print('Название товара:', markets.get('product', ''))
                    print('Стоимость в руб.:', markets.get('price', ''))

            # Если счетчик равен 0, то продукт не найден.
            if count == 0:
                print("Товар не найден.")

        elif command.startswith('load '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)

            # Прочитать данные из файла JSON.
            with open(parts[1], 'r') as f:
                market = json.load(f)

        elif command.startswith('save '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)

            # Сохранить данные в файл JSON.
            with open(parts[1], 'w') as f:
                json.dump(market, f)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить продукт;")
            print("list - вывести список продуктов;")
            print("load <имя файла> - загрузить данные из файла;")
            print("save <имя файла> - сохранить данные в файл;")
            print("select <товар> - информация о товаре;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)