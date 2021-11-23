#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sentense = input("Введите предложение: ").replace(' ', '')

for i in range(len(sentense)):
    if i % 2 != 0 and sentense[i].lower() == 'и':
        print(sentense[i])







