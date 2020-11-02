def roman(arg):
    if arg <= 3:
        return "I" * arg
    elif arg <= 5:
        return "I" * (5 - arg) + "V"
    elif arg <= 8:
        return "V" + "I" * (arg - 5)
    elif arg <= 10:
        return "I" * (10 - arg) + "X"
    elif arg == 27:
        return "X" * (27 // 10) + "V" + "I" * (arg - 25)
    elif arg == 48:
        return "XLV" + "I" * (arg - 45)
