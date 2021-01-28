#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Использовать словарь, содержащий следующие ключи: название пункта назначения; номер
# поезда; время отправления. Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
# быть упорядочены по номерам поездов;
# вывод на экран информации о поезде, номер которого введен с клавиатуры; если таких поездов нет,
# выдать на дисплей соответствующее сообщение.
# Выполнить индивидуальное задание 2 лабораторной работы 13, добавив возможность работы с
# исключениями и логгирование.


from dataclasses import dataclass, field
import logging
import sys
from typing import List
import xml.etree.ElementTree as ET


class IllegalTimeError(Exception):
    def __init__(self, time, message="Запрещенное время : "):
        self.time = time
        self.message = message
        super(IllegalTimeError, self).__init__(message)

    def __str__(self):
        return f
        "{self.time} -> {self.message}"


class UnknownCommandError(Exception):
    def __init__(self, command, message="Unknown command"):
        self.command = command
        self.message = message
        super(UnknownCommandError, self).__init__(message)

    def __str__(self):
        return f
        "{self.command} -> {self.message}"

@dataclass(frozen=True)
class poez:
    name: str
    num: str
    time: str


@dataclass
class Staff:
    poezd: List[poez] = field(default_factory=lambda: [])

    def add(self, name, num, time):
        self.poezd.append(
            poez(
                name=name,
                num=num,
                time=time
            )
        )

        self.poezd.sort(key=lambda poez: poez.num)

    def __str__(self):
        # Заголовок таблицы.
        table = []
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 17
        )
        table.append(line)
        table.append(
            '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
                "№",
                "Пункт назначения",
                "Номер поезда",
                "Время отправления"
            )
        )
        table.append(line)


        for idx, poez in enumerate(self.poezd, 1):
            table.append(
                '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                    idx,
                    poez.name,
                    poez.num,
                    poez.time
                )
            )

        table.append(line)

        return '\n'.join(table)

    def select(self):

        parts = command.split(' ', maxsplit=2)

        times = int(parts[1])

        c = 0

        for poez1 in self.trains:
            if poez1.time == times:
                c += 1
                print('Номер поезда:', poez1.num)
                print('Пункт назначения:', poez1.name)
                print('Время отправления:', poez1.time)

        if c == 0:
            print("Таких поездов нет!")

    def load(self, filename):
        with open(filename, 'r', encoding='utf8') as fin:
            xml = fin.read()
        parser = ET.XMLParser(encoding="utf8")
        tree = ET.fromstring(xml, parser=parser)
        self.poezd = []

        for poez_element in tree:
            name, num, time = None, None, None

            for element in poez_element:
                if element.tag == 'name':
                    name = element.text
                elif element.tag == 'num':
                    num = element.text
                elif element.tag == 'time':
                    time = element.text

                if name is not None and num is not None \
                        and time is not None:
                    self.poezd.append(
                        poez(
                            name=name,
                            num=time,
                            time=time
                        )
                    )

    def save(self, filename):
        root = ET.Element('poezd')
        for poez in self.poezd:
            poez_element = ET.Element('poez')

            name_element = ET.SubElement(poez_element, 'name')
            name_element.text = poez.name

            num_element = ET.SubElement(poez_element, 'num')
            num_element.text = poez.num

            time_element = ET.SubElement(poez_element, 'time')
            time_element.text = str(poez.time)

            root.append(poez_element)

        tree = ET.ElementTree(root)
        with open(filename, 'wb') as fout:
            tree.write(fout, encoding='utf8', xml_declaration=True)


if __name__ == '__main__':
    poezd = []
    staff = Staff()

    while True:

        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':

            name = input("Название пункта назначения: ")
            num = input("Номер поезда: ")
            time = input("Время отправления: ")

            staff.add(name, num, time)
            logging.info(
            f"Добавлено название: {name}, "
            f"Добавлен номер: {num}, "
            f"Добавлено время {time}. "
            )

        elif command == 'list':
            print(staff)
            logging.info("Отображен список поездов.")

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)

            numbers = int(parts[1])

            c = 0

            for poez1 in poezd:
                if poez1.num == numbers:
                    c += 1
                    print('Номер поезда:', poez1.num)
                    print('Пункт назначения:', poez1.name)
                    print('Время отправления:', poez1.time)

            if c == 0:
                print("Таких поездов нет!")

        elif command.startswith('load '):

            parts = command.split(' ', maxsplit=1)
            staff.load(parts[1])
            logging.info(f"Загружены данные из файла {parts[1]}.")

        elif command.startswith('save '):

            parts = command.split(' ', maxsplit=1)
            staff.save(parts[1])
            logging.info(f"Сохранены данные в файл {parts[1]}.")

        elif command == 'help':

            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <номер поезда> - запросить информацию о выбранном времени;")
            print("help - отобразить справку;")
            print("load <имя файла> - загрузить данные из файла;")
            print("save <имя файла> - сохранить данные в файл;")
            print("exit - завершить работу с программой.")
        else:
            raise UnknownCommandError(command)

        except Exception as exc:
        logging.error(f
        "Ошибка: {exc}")
        print(exc, file=sys.stderr)
        
