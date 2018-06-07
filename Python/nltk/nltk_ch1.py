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

# Create a tokenized sentence
sent1 = ['Call', 'me', 'Ishmael', '.']

# Check to see that the sentence was created correctly and that the functions are working as intended.
print(len(sent1))
print(lexical_diversity(sent1))

# Print to check that sentences have loaded.
print(sent2)
print(sent3)

# Create a new sentence and append two lists together.
words = ["Monty", "Python"] + ["and", "the", "Holy", "Grail"]
print(words)

# Append two lists together
words = sent4 + sent1
print(words)

# Append a word to an existing sentence
sent1.append("Some")
print(sent1)

# Working with indexes - Print the 173rd token in the given text
print(text4[173])

# Find the index in the given text where the given word is passed
print(text4.index("awaken"))

# Can use indexes to take segments, known as slices, out of a text document. Returns a list.
print(text5[16715:16735])
print(text6[1600:1625])

# Exploring indexes.
sent = ["word1", "word2", "word3", "word4", "word5",
        "word6", "word7", "word8", "word9", "word10"]

# Looking into how indexes are constructed.
print(sent[0])
print(sent[9])
print(sent[5:8])
print(sent[5])
print(sent[6])
print(sent[7])
print(sent[:3])

print(text2[141525:])

sent[0] = "First"
sent[9] = "Last"

print(len(sent))

print(type(sent))
sent[1:9] = ["Second", "Third"]
print(sent[1:9])
print(sent)

sent1 = ["Call", "me", "Ishmael", "."]

my_sent = ["Bravely", "bold", "Sir", "Robin", ".", "rode",
            "forth", "from", "Camelot"]

noun_phrase = my_sent[1:4]
print(noun_phrase)

wOrDs = sorted(noun_phrase)
print(wOrDs)

vocab = set(text1)
vocab_size = len(vocab)
print(vocab_size)

name = "Monty"
print(name[0])
print(name[:4])

print(name*2)
print(name + '!')

print(" ".join(["Monty", "Python"]))
print('Monty Python'.split())

saying = ["After", "all", "is", "said", "and", "done",
            "more", "is", "said", "than", "done"]
tokens = set(saying)
tokens = sorted(tokens)
print(tokens[-2:])

fdist1 = FreqDist(text1)
print(fdist1)
print(fdist1.most_common(50))
print(fdist1["whale"])

fdist1.plot(50, cumulative=True)

V = set(text1)
long_words = [w for w in V if len(w) > 15]
print(sorted(long_words))