#!/usr/bin/env python3
# Created by Marc Coffi
# Created in June 2022
# This program takes a sentence and
# display the words making up the sentence individually


import random

# Defining the function that calculates the average
def split_text(sentence):
    list_of_words = sentence.split(" ")

    for word in list_of_words:
        print(word)


def main():
    # Get user input
    user_input = input("Enter a sentence: ")

    # Calling the function
    split_text(user_input)


if __name__ == "__main__":
    main()
