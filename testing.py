import string
import stdiomask

# x = input("Enter your name: ")
# print(x)


# alphabet = set(string.ascii_uppercase)
# print(alphabet)


word = "bed"   
someList = []
used_letters = set("esd")


for letter in word:
    if letter in used_letters:
        someList.append(letter)

    else:
        someList.append('_')

print(someList)
str = ' '.join(someList)         # join elements without space
print(str.upper())



