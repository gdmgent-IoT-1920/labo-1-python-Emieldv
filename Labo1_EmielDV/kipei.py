from random import randint

print("LINGO-BINGO Welkom bij het kip en eieren spel!")

randomNumber = randint(1000, 9999)
# print(randomNumber)

geradenNummer = int(input("Geef een viercijferig nummer in:\n"))

pogingen = 1

def returnMatches(a,b):
       return list(set(a) & set(b))

while geradenNummer != randomNumber:
    randomArray = [int(x) for x in str(randomNumber)]
    geradenArray = [int(y) for y in str(geradenNummer)]

    chickens = len([i for i, j in zip(randomArray, geradenArray) if i == j])
    eggs = len(returnMatches(randomArray,geradenArray)) - chickens


    if eggs < 0:
        eggs = 0
    
    print("U heeft " + str(chickens) + " kippen!")
    print("U heeft " + str(eggs) + " eieren!")

    geradenNummer = int(input())
    pogingen += 1


print("\nProficiat! U heeft er " + str(pogingen) + " pogingen over gedaan.\n")