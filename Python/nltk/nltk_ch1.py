from nltk.book import *

# concordance shows every occurance of the word passed to the function as well as some context.
text1.concordance("monstrous")

# Other examples
text6.concordance("knights")
text6.concordance("bravely")

# Similar looks at what other words in addition to the word passed to the function appear in a
# similar range of contexts.
text1.similar("monstrous")
text2.similar("monstrous")

# The term common_contexts look at what contexts are shared by similar words.
text2.common_contexts(["monstrous", "very"])

# Other examples
text6.similar("knights")
text6.common_contexts(["knights", "castle"])
text6.common_contexts(["knights", "bosom"])
#text6.similar("bravely")

# dispersion_plot looks at where in the text a certain word appears
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

# Other examples
text3.dispersion_plot(["Adam", "Eve", "God"])

# Under what sort of contexts does the word God appear in the Book of Genesis. 
text3.concordance("God")
text3.similar("God")
text3.common_contexts(["God", "thee"])

# What is the length of the Book of Genesis from start to finish?
print(len(text3))

# List all unique words in a given text
print(sorted(set(text3)))

# How many unique words and/or tokens?
print('How many unique tokens?')
print(len(set(text3)))

# Measure of lexical diversity
# Term one, number of unique words or tokens 
# Term two, length of text
print("Lexical Diversity")
print(len(set(text3)) / len(text3))

# Count the number of times a given word passed to this function appears in a given text document.
print("Number of times 'smote' appears in this document.")
print(text3.count("smote"))

def lexical_diversity(text):
    """
    Takes in text, returns number of unique tokens / total tokens
    """
    return len(set(text)) / len(text)

def percentage(count, total):
    """
    takes in count, and total returns percentage
    """
    return 100 * count / total

# Examples of using the function
print(lexical_diversity(text3))
print(lexical_diversity(text5))

print(percentage(4, 5))
print(percentage(text4.count('a'), len(text4)))

sent1 = ['Call', 'me', 'Ishmael', '.']

print(len(sent1))

print(lexical_diversity(sent1))