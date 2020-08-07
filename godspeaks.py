import random

def main():
    with open('Happy.TXT') as f:
        godWords = f.read().splitlines()

    print(end="God says... ")

    #print random words from list godWords 31+1 times
    for x in range(0, 30):
        words = random.choice(godWords)
        print(words, end=" ")

    #print a random word from list godWords and append a period onto it
    words = random.choice(godWords)
    print(words + ".\n")

    input("Press enter to continue")

main()
