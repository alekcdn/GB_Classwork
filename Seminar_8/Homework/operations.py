# -*- mode: python ; coding: utf-8 -*-

def open_base(file_name):  #Открытие базы данных
    file = open(file_name, "r", encoding="utf-8-sig")
    uni_base = file.readlines()
    return uni_base






