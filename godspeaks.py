import random, sys

def main():
    words = []

    with open('english.txt') as f:
        godWords = f.read().splitlines()

    while True: 
        print("Insert 1 to quit")
        print("Insert any other number to continue.\n")
        try:
            userInput = int(input("(> "))
        except ValueError:
            print("Try again")
            main()
        if (userInput == 1):
            quit()
        else:
            sys.stdout.write("God says: ")
            for x in range(0, 31):
                words = random.choice(godWords)
                sys.stdout.write(words)
                sys.stdout.write(" ")

            sys.stdout.write(".\n\n")

main()
