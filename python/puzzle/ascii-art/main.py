def lPos(letter):
    pos = ord(letter.upper()) - 65
    if not 0 <= pos <= 25:
        pos = 26
    return pos


width = int(input())
height = int(input())
text = input()

for i in range(height):
    row = input()
    line = "".join(
        row[width * lPos(letter): width * (lPos(letter) + 1)]
        for letter in text
    )
    print(line)
