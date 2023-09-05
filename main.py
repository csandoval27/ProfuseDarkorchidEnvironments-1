# String Practice:

# Create a Python program that asks the user to input a sentence.
sentence = input("Write a sentence. ")
# Print the first and last letter of the sentence.
print(sentence[0])
print(sentence[-1])
# Convert the entire sentence to uppercase and print the result.
print(sentence.upper())
# Find and print a substring from the inputted sentence.
print(sentence[0:5])

# Replace a word in the sentence and print the updated sentence.
print(sentence.replace("python", "coding"))

# Input Practice:

# Create a Python program that asks the user for their name, age, and favorite movie.
name = input("What is your name? ")
age = input("What is your age? ")
movie = input("What is your favorite movie? ")
# Print a message back to the user with this information.
# Note: Make sure to convert the age to an integer.
print(
    f'your name is {name}, you are {age}, and your favorite movie is {movie} ')

# F-String Practice:

# Create a Python program that asks the user for three objects in the room.
object1 = input("What is an object in the room? ")
object2 = input("What is another object in the room? ")
object3 = input("What is a third object in the room? ")
# Create variables from these objects and insert those variables into an f-string sentence.
# Print the f-string sentence.
print(f'there is a {object1}, {object2}, and {object3} in the room')

# Advanced String Practice:

# Create a Python program that reverses the words in a sentence inputted by the user.
# For example, if the user inputs "Python is fun", the program should print "fun is Python".
# Advanced Input Practice:
# Python code
# To reverse words in a given string

# Create a Python program that asks the user for the name of their favorite book, movie, and song.
book = input("what is your favorite book?")
movie = input("What is your favorite movie? ")
song = input("What is your favorite song? ")

# Print a message that says, "Your favorite book is [Book], your favorite movie is [Movie], and your favorite song is [Song]."
print(
    f'Your favorite book is {book}, your favorite movie is {movie}, and your favorite song is {song}.'
)
# Advanced F-String Practice:

# Create a Python program that asks the user for their name, age, and the current year.
# Use f-strings to print a message like: "Hello [Your Name], you were born in [Current Year - Your Age]."
name = input("What is your name? ")
age = input("What is your age? ")
year = input("What year were you born in? ")
# Type Conversion Practice:
print(f'Hello {name}, you were born in {year} - {age}')
# Create a Python program that asks the user for two numbers.
number = input("Pick a number. ")
numberr = input("Pick another number. ")
# Print the sum, difference, product, and quotient of the two numbers.
# Note: Make sure to convert the input to integers before performing any calculations.
# sum = number + numberr
# print("Sum of", number, "and", numberr, "is", sum)

# difference = number - numberr
# print("Difference of", number, "and", numberr, "is", difference)

# quotient = number / numberr
# print("The answer for number/numberr : ")
# print(number / numberr)

# Summary Challenge:

# Find a summary of a movie online and create a variable called movie_summary and store the summary in this variable.
movie_summary = "Jaime Reyes suddenly finds himself in possession of an ancient relic of alien biotechnology called the Scarab. When the Scarab chooses Jaime to be its symbiotic host, he's bestowed with an incredible suit of armor that's capable of extraordinary and unpredictable powers, forever changing his destiny as he becomes the superhero Blue Beetle."
print(movie_summary)

# Print the length of the summary.
print(len(movie_summary))
# Uppercase the entire summary and print it.
print(movie_summary.upper())
# Replace a word in the summary and print the updated summary.
print(movie_summary.replace("Blue", "Red"))
# Print the last word of the summary.
print(movie_summary[334:342])
# Real Challenge:

# Create a Python program that asks the user for their first and last name, their age, and their favorite color.
# Using f-strings, print a message that says, "Hello [First Name] [Last Name], you are [Age] years old and your favorite color is [Favorite Color]."
