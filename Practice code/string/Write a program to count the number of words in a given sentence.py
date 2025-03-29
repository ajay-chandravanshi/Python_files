# Q . Write a program to count the number of words in a given sentence.
#  
sentence = input("Enter a sentence: ")  # Taking input from the user
word_count = len(sentence.split())  # Splitting the sentence into words and counting them
print("Number of words:", word_count)  # Printing the result
