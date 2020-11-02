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
        return self.text[num-1]

    def verse_from_to(self, frm, to):
        song = ''
        for i in range(to-1, frm):
            song += self.text[i]
            song += '\n\n'
        return song

    def all(self):
        return self.text