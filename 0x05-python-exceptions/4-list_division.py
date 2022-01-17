#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    c = list_length
    i = 0
    result = []
    while c != 0:
        try:
            result += [my_list_1[i] / my_list_2[i]]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            c -= 1
            i += 1
    return result
