def check_int_if_even(number: int) -> bool:

    last_digit = str(number)[-1:]
    number_dic = {
        "0": True,
        "1": False,
        "2": True,
        "3": False,
        "4": True,
        "5": False,
        "6": True,
        "7": False,
        "8": True,
        "9": False
    }

    return number_dic[last_digit]

print(check_int_if_even(322))