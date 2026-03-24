# basic string manipulation
name = "karishma"
print(name.upper())
print(name.lower())
print(name.split())

# string slciing
name = "karishma"
print(name[0])
print(name[0:3])
print(name[-3])

# f strings
name = "karishma"
age = 22
print(f"My name is {name} and I am {age} years old.")

# problems related to strings
# palindrome
word = input("Enter a word: ")

if word == word[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")

# count the number of vowels in a string
text = input("Enter the text: ")
count = 0

for char in text:
    if char in "aeiouAEIOU":
        count += 1

print(count)

# revierse sentence and capitalize
sen = input(" enter the sentence")
words = sen.split()
reversed_words = words[::-1]
reversed_sentence = " ".join(reversed_words)
print(reversed_sentence.capitalize())


# practise problems 1 reverse a string (Easy)
text = "hello"
print(text[::-1])

# method 2 using a loop
text = "hello"
for i in range(0, 4):
    print(text.split(0))
    print(text[::-1])

# check palindorme
word = input("Enter a word: ")
if word == word[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")

text = input("Enter the text: ")
count = 0
for each in char in text:
    if char in text >= 0:
        count += 1
print(count)
