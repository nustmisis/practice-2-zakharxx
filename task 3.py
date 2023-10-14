# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:05:53 2023

@author: workk

Упражнение 61. Действительный номерной знак машины?
(Решено. 28 строк)
Допустим, в  нашей стране старый формат номерных знаков автомобилей состоял из трех заглавных букв, следом за которыми шли три цифры. 
После того как все возможные номера были использованы, формат был 
изменен на четыре цифры, предшествующие трем заглавным буквам.
Напишите программу, запрашивающую у пользователя номерной знак 
машины и оповещающую о том, для какого формата подходит данная последовательность символов: для старого или нового. Если введенная последовательность не соответствует ни одному из двух форматов, укажите 
это в сообщении
"""



'''
Запросим ввод номерного знака
Посчитаем и проверим на необходимое количество знаков номерного знака, после чего чекнем первые несколько символов на то, что это буквы, а следующие являюстя цифрами.
'''
# Запросим номерной знака у пользователя
license_plate = input("Введите номерной знак машины: ")

# Проверим длину введенной строки
if len(license_plate) == 6:
    # Совершим проверку первых трех символов (должны быть буквами) и последних трех символов (должны быть цифрами)
    if license_plate[:3].isalpha() and license_plate[3:].isdigit():
        print("Этот номерной знак соответствует старому формату.")
    else:
        print("Этот номерной знак не соответствует ни одному из форматов.")
elif len(license_plate) == 7:
    # Совершим проверку первых четырех символов (должны быть цифрами) и последних трех символов (должны быть буквами)
    if license_plate[:4].isdigit() and license_plate[4:].isalpha():
        print("Этот номерной знак соответствует новому формату.")
    else:
        print("Этот номерной знак не соответствует ни одному из форматов.")
else:
    print("Этот номерной знак не соответствует ни одному из форматов.")
