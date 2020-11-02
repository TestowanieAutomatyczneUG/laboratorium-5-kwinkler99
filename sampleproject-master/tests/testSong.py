import unittest
from song.song import song


class SongTest(unittest.TestCase):
    def test_first_verse_(self):
        self.assertEqual(self.temp.one_verse(1),
                         "On the first day of Christmas my true love gave to me: a Partridge in a Pear "
                         "Tree.")

    def test_second_verse(self):
        self.assertEqual(self.temp.one_verse(2),
                         "On the second day of Christmas my true love gave to me: two Turtle Doves, "
                         "and a Partridge in a Pear Tree.")

    def test_third_verse(self):
        self.assertEqual(self.temp.one_verse(3),
                         "On the third day of Christmas my true love gave to me: three French Hens, "
                         "two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_fourth_verse(self):
        self.assertEqual(self.temp.one_verse(4),
                         "On the fourth day of Christmas my true love gave to me: four Calling Birds, "
                         "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_fifth_verse(self):
        self.assertEqual(self.temp.one_verse(5),
                         "On the fifth day of Christmas my true love gave to me: five Gold Rings, "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a"
                         " Pear Tree.")

    def test_sixth_verse(self):
        self.assertEqual(self.temp.one_verse(6),
                         "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, "
                         "five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                         "and a Partridge in a Pear Tree.")

    def test_seventh_verse(self):
        self.assertEqual(self.temp.one_verse(7), "On the seventh day of Christmas my true love gave to me: seven "
                                                 "Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, "
                                                 "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_eight_verse(self):
        self.assertEqual(self.temp.one_verse(8), "On the eighth day of Christmas my true love gave to me: eight "
                                                 "Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
                                                 "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a "
                                                 "Pear Tree.")

    def test_ninth_verse(self):
        self.assertEqual(self.temp.one_verse(9),
                         "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, "
                         "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, "
                         "five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                         "and a Partridge in a Pear Tree.")

    def test_tenth_verse(self):
        self.assertEqual(self.temp.one_verse(10),
                         "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, "
                         "nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, "
                         "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, "
                         "two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_eleventh_verse(self):
        self.assertEqual(self.temp.one_verse(11),
                         "On the eleventh day of Christmas my true love gave to me: eleven Pipers "
                         "Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, "
                         "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling "
                         "Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_twelfth_verse(self):
        self.assertEqual(self.temp.one_verse(12),
                         "On the twelfth day of Christmas my true love gave to me: twelve Drummers "
                         "Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, "
                         "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, "
                         "five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                         "and a Partridge in a Pear Tree.")

    def test_song(self):
        self.assertEqual(self.temp.verse_from_to(1, 12),
                         "On the first day of Christmas my true love gave to me: a Partridge in a "
                         "Pear Tree.\n\nOn the second day of Christmas my true love gave to me: two "
                         "Turtle Doves, and a Partridge in a Pear Tree.\n\nOn the third day of "
                         "Christmas my true love gave to me: three French Hens, two Turtle Doves, "
                         "and a Partridge in a Pear Tree.\n\nOn the fourth day of Christmas my true "
                         "love gave to me: four Calling Birds, three French Hens, two Turtle Doves, "
                         "and a Partridge in a Pear Tree.\n\nOn the fifth day of Christmas my true "
                         "love gave to me: five Gold Rings, four Calling Birds, three French Hens, "
                         "two Turtle Doves, and a Partridge in a Pear Tree.\n\nOn the sixth day of "
                         "Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge "
                         "in a Pear Tree.\n\nOn the seventh day of Christmas my true love gave to "
                         "me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge "
                         "in a Pear Tree.\n\nOn the eighth day of Christmas my true love gave to "
                         "me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, "
                         "five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                         "and a Partridge in a Pear Tree.\n\nOn the ninth day of Christmas my true "
                         "love gave to me: nine Ladies Dancing, eight Maids-a-Milking, "
                         "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling "
                         "Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear "
                         "Tree.\n\nOn the tenth day of Christmas my true love gave to me: ten "
                         "Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, "
                         "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling "
                         "Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear "
                         "Tree.\n\nOn the eleventh day of Christmas my true love gave to me: eleven "
                         "Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, "
                         "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, "
                         "five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                         "and a Partridge in a Pear Tree.\n\nOn the twelfth day of Christmas my "
                         "true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, "
                         "ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, "
                         "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling "
                         "Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear "
                         "Tree.")


    # Utility functions
    def setUp(self):
        self.temp = song()
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")
