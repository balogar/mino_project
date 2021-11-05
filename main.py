set1 = set()
file_input = open("file_1.txt", "r")
data = file_input.read()
data_lower = data.lower()
punctuation_marks_input = open("punctuation_marks.txt", "r")
punctuation_marks = punctuation_marks_input.read()
prepositions_input = open("prepositions_articles.txt", "r")
prepositions = prepositions_input.read()
pronouns_input = open("pronouns_connectors.txt", "r")
pronouns = pronouns_input.read()
adjectives_input = open("adjectives.txt", "r")
adjectives = adjectives_input.read()
nouns_input = open("nouns.txt", "r")
nouns = nouns_input.read()
verbs_input = open("verbs.txt", "r")
verbs = verbs_input.read()
adverbs_input = open("adverbs.txt", "r")
adverbs = adverbs_input.read()

adjectives_split = adjectives.split("\n")



def word_files(input):
    pass


def punctuation_replace(text):
    replacement = punctuation_marks
    for c in replacement:
        if c in text:
            text = text.replace(c, '')
    return text


new_data = punctuation_replace(data_lower)
words = new_data.split()
number_of_words = len(words)


for i in words:
    if i not in adverbs:
        if i not in prepositions:
            if i not in pronouns:
                if i not in verbs:
                    if i not in nouns:
                        if i not in adjectives_split:
                            set1.add((i, words.count(i)))


list1 = list(set1)
sorted_list = list1.sort(key=lambda x:x[1], reverse=True)


print("Sentences in a file: " + "\n" + data)
print("Number of words in a file: " + str(number_of_words))


for i in list1:
    print("Word: "+str(i[0]))
    print("Number of occurrences: "+str(i[1]))


