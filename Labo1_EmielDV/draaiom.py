zin = input("Geef een zin in:\n")

def omdraaien(input):
    splitWords = input.split(" ")
    splitWords = splitWords[::-1]

    output =' '.join(splitWords)

    return output

print("\n" + str(omdraaien(zin)) + "\n")