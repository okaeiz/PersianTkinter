# -*- coding: utf-8 -*-


def fdigit_replacer(x):
    my_string = str(x)
    for i in my_string:
        if i == "0":
            my_string = my_string.replace(i, '۰')
        elif i == "1":
            my_string = my_string.replace(i, '۱')
        elif i == "2":
            my_string = my_string.replace(i, '۲')
        elif i == "3":
            my_string = my_string.replace(i, '۳')
        elif i == "4":
            my_string = my_string.replace(i, '۴')
        elif i == "5":
            my_string = my_string.replace(i, '۵')
        elif i == "6":
            my_string = my_string.replace(i, '۶')
        elif i == "7":
            my_string = my_string.replace(i, '۷')
        elif i == "8":
            my_string = my_string.replace(i, '۸')
        elif i == "9":
            my_string = my_string.replace(i, '۹')
    return(my_string)
