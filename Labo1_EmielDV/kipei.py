from random import randint

print("\n\033[1;36;40mLINGO-BINGO Welkom bij het kip en eieren spel!")
print("\nIk genereer een cijfer tussen 1000 en 10000 en u moet dit cijfer raden.")
print("\nVoor elk cijfer dat u correct en op de juiste plaats heeft geraden krijgt u een 'kip'.\nVoor elk cijfer dat correct geraden is maar op de verkeerde plaats, krijgt u een 'ei'")


randomNumber = randint(1000, 10000)
print(randomNumber)

geradenNummer = int(input("\n\033[1;33;40mGeef een viercijferig nummer in:\n\033[1;32;40m>>>"))

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
    
    print("\n\033[1;33;40mU heeft " + str(chickens) + " kippen!")
    print("U heeft " + str(eggs) + " eieren!")

    geradenNummer = int(input("\033[1;32;40m>>> "))
    pogingen += 1


print("\nProficiat! U heeft er " + str(pogingen) + " pogingen over gedaan.\n")