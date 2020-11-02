def roman(arg):
    int_val = [
            90, 50, 40,
            10, 9, 5, 4,
            1
            ]
    rom = [
        "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    rom_val = ''
    i = 0
    if arg < 100:
        while arg > 0:
            for _ in range(arg // int_val[i]):
                rom_val += rom[i]
                arg -= int_val[i]
            i += 1
        return rom_val
