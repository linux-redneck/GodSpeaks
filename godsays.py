import random, sys

def main():
    sys.stdout.write("===================SPEAK TO GOD===================\n")
    with open('english.txt') as f:
        godWords = f.read().splitlines()
    word = []
    for x in range(0, 31):
        word = random.choice(godWords)
        sys.stdout.write(word)
        sys.stdout.write(" ")
    sys.stdout.write(".")

main()
