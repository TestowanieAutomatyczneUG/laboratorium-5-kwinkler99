def roman(arg):
    if arg <= 3:
        return "I"*arg
    elif arg <= 5:
        return "I"*(5-arg)+"V"
    elif arg <= 8:
        return "V"+"I"*(arg-5)
    else:
        return "I"*(10-arg)+"X"