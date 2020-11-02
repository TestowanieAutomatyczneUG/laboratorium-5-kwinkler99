
class hamming:
    def distance(self, genA, genB):
        if genA == "" and  genB == "":
            return 0
        elif len(genA) == 1 and len(genB) == 1:
            return 0