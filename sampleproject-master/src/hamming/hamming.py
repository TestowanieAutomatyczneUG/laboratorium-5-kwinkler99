
class hamming:
    
    def distance(self, genA, genB):
        
        def check(letterOne, letterTwo):
            if letterOne == letterTwo:
                return 0
            else:
                return 1
            
        counter = 0
        if len(genA) == len(genB):
            for i in range(len(genA)):
                counter += check(genA[i], genB[i])

            return counter

        elif len(genA) > 1 and 1 < len(genB) != len(genA):
            raise ValueError("Error")

            


