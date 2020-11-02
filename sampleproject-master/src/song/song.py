class song:
    def __init__(self):
        self.text = ["On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
                     "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a "
                     "Pear Tree.", "On the third day of Christmas my true love gave to me: three French Hens, "
                     "two Turtle Doves, and a Partridge in a Pear Tree.",
                     "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, "
                     "two Turtle Doves, and a Partridge in a Pear Tree.",
                     "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, "
                     "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                     "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, "
                     "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                     "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, "
                     "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                     "and a Partridge in a Pear Tree.",
                     "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, "
                     "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French "
                     "Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                     "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, "
                     "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
                     "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                     "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies "
                     "Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
                     "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                     "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, "
                     "ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, "
                     "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                     "and a Partridge in a Pear Tree.",
                     "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, "
                     "eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, "
                     "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French "
                     "Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                     ]

    def one_verse(self, num):
        if isinstance(num, int) and 1 <= num <= 12:
            return self.text[num - 1]
        else:
            raise ValueError("Error")

    def verse_from_to(self, frm, to):
        if isinstance(frm, int) and 1 <= frm <= 12 and 1 <= to <= 12 and frm < to:
            text = ''
            for i in range(frm - 1, to):
                text += self.text[i]
                if i != to - 1:
                    text += '\n\n'
            return text
        else:
            raise ValueError("Error")

    def all(self):
        text = ''
        for i in range(len(self.text)):
            text += self.text[i]
            if i != len(self.text) - 1:
                text += '\n\n'
        return text
