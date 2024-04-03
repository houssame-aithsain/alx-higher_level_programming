#!usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Get elements from my_list_1 and my_list_2, or 0 if out of range
            num1 = my_list_1[i] if i < len(my_list_1) else 0
            num2 = my_list_2[i] if i < len(my_list_2) else 0

            # Perform division, handle exceptions
            try:
                result.append(num1 / num2)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            except TypeError:
                print("wrong type")
                result.append(0)

        except IndexError:
            print("out of range")
            result.append(0)

    return result
