#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = [0] * list_length
    for i in range(list_length):
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            result_list[i] = num1 / num2
        except ZeroDivisionError:
            print("division by 0")
            result_list[i] = 0
        except TypeError:
            print("wrong type")
            result_list[i] = 0
        except IndexError:
            print("out of range")
            result_list[i] = 0
        finally:
            pass
        return result_list