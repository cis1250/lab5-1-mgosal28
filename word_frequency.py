#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re
import string

# This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    """Prompt user until they enter a valid sentence."""
    while True:
        sentence = input("Enter a sentence: ").strip()
        if is_sentence(sentence):
            return sentence
        else:
            print("Invalid sentence. It must start with a capital letter, end with '.', '!' or '?', and contain words.")

def calculate_frequencies(sentence):
    """Calculate word frequencies in the sentence."""
    words = []
    frequencies = []

    # Remove the trailing punctuation (., !, or ?)
    sentence = sentence[:-1]

    # Split into words
    split_words = sentence.split()

    for word in split_words:
        # Remove punctuation around the word and convert to lowercase
        cleaned_word = word.strip(string.punctuation).lower()

        if cleaned_word in words:
            index = words.index(cleaned_word)
            frequencies[index] += 1
        else:
            words.append(cleaned_word)
            frequencies.append(1)

    return words, frequencies

def print_frequencies(words, frequencies):
    """Print each word with its frequency."""
    print("\nWord frequencies:")
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")

def main():
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)
    
    main()
