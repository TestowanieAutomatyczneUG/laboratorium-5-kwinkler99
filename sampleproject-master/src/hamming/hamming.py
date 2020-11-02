
class hamming:
    def distance(self, genA, genB):
        if len(genA) <= 1 and len(genB) <= 1:
            if genA == genB:
                return 0
            else:
                return 1


