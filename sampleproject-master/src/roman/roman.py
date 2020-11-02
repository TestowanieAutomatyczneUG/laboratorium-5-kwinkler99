def roman(arg):
    if arg <= 3:
        return "I"*arg
    elif(arg <= 5):
        return "I"*(5-arg)+"V"