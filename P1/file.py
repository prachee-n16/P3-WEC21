f = open(r"WEC-21\P3-WEC21\P1\Test1.txt", "r")

WORDS = []
i = 0

for x in f:
    WORDS[i] = x
    i = i+1
    print(x)