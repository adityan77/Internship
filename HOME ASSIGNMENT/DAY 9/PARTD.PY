# 🔹 Part D: Advanced Applications
# 11.	Word Frequency Counter
# •	Input a sentence from the user.
# •	Count how many times each word occurs using a dictionary.
# 12.	Character Frequency
# •	Input a string.
# •	Count how many times each character occurs.
# 13.	Grades Lookup
# •	Create a dictionary where keys are roll numbers and values are student names.
# •	Ask user for a roll number and print the corresponding name.
# ________________________________________

# 14.	Nested Dictionary
# •	Create a nested dictionary:
# student = {
#     	"name": "Ravi",
#     	"marks": {
#         	"math": 88,
#         	"science": 92
#     	}
# }
# •	Access "science" marks from the nested dictionary.
# 15.	Dictionary from Two Lists
# •	Given:
# keys = ["name", "age", "city"]
# values = ["Sam", 30, "Delhi"]
# •	Combine into a dictionary using a loop or zip().

sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = {}
char_count={}
for word in words:
    if word in word_count:
        word_count[word] += 1 
    else:
        word_count[word] = 1

print("Word Frequency:", word_count)

