import re

set1 = set()
punctuation_marks_input = open("punctuation_marks.txt", "r")
punctuation_marks = punctuation_marks_input.read()


def word_files(words_path):
    words_txt = open(words_path, "r")
    words_check = words_txt.read()
    words_lower = words_check.lower()
    words_lower_split = words_lower.split("\n")
    return words_lower_split


def punctuation_replace(text):
    replacement = punctuation_marks
    for c in replacement:
        if c in text:
            text = text.replace(c, '')
    return text


def create_set_from_input(input_text):
    file_input = open(input_text, "r")
    data = file_input.read()
    data_lower = data.lower()
    new_data = punctuation_replace(data_lower)
    words = new_data.split()
    for y in words:
        set1.add((y, words.count(y)))
    return set1


prepositions_articles = word_files("prepositions_articles.txt")
adjectives = word_files("adjectives.txt")
adverbs = word_files("adverbs.txt")
nouns = word_files("nouns.txt")
pronouns_connectors = word_files("pronouns_connectors.txt")
verbs = word_files("verbs.txt")
main_list = create_set_from_input("file_1.txt")
main_list = list(main_list)
main_list.sort(key=lambda x: x[1], reverse=True)
main_list_1 = [num for num in main_list if num[0] not in prepositions_articles]
main_list_2 = [num for num in main_list_1 if num[0] not in adjectives]
main_list_3 = [num for num in main_list_2 if num[0] not in adverbs]
main_list_4 = [num for num in main_list_3 if num[0] not in nouns]
main_list_5 = [num for num in main_list_4 if num[0] not in pronouns_connectors]
main_list_6 = [num for num in main_list_5 if num[0] not in verbs]

list2 = []
list3 = []
list4 = []
list5 = []

for lo in main_list_6:
    list5.append(lo[0])

for t in main_list_6:
    if t[0].endswith('s'):
        list4.append(t[0])
        last_ch = len(t[0])
        remove_last = t[0][:last_ch-1]
        list2.append(remove_last)
        list3.append(t[1])

print(main_list_6)
main_list_7 = list(main_list_6)
list8 = set()

for o in main_list_7:
    if o[0] in list2:
        index_of_numbers_of_plural_words = list2.index(o[0])
        number_of_plural_words = list3[index_of_numbers_of_plural_words]
        new_number_of_words = o[1] + number_of_plural_words
        list8.add((o[0], new_number_of_words))
    else:
        list8.add(o)

list9 = list(list8)
list9.sort(key=lambda x: x[1], reverse=True)
list10=[]

for mo in list4:
    last_ch_1 = len(mo)
    remove_last_1 = mo[:last_ch_1 - 1]
    if remove_last_1 in list5:
        list10.append(mo)

main_list_8 = [num for num in list9 if num[0] not in list10]


for i in main_list_8:
    print("Word: "+str(i[0]))
    print("Number of occurrences: "+str(i[1]))

