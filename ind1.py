#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Вариант 1. Написать программу, которая считывает из текстового файла три предложения и выводит их
# в обратном порядке
if __name__ == '__main__':
    with open('ind1.txt', 'r') as f:
        text = f.read()
        text = text.replace("!", ".")
        text = text.replace("?", ".")
        sentence = text.split(".")
        reverse_sentence = '. '.join(reversed(sentence))
        print(reverse_sentence)