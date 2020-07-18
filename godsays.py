import random, sys

def main():
    words = []
    sys.stdout.write("God says: ")
    with open('english.txt') as f:
        godWords = f.read().splitlines()
    for x in range(0, 31):
        words = random.choice(godWords)
        sys.stdout.write(words)
        sys.stdout.write(" ")
    sys.stdout.write(".")

main()
