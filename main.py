set1 = set()
file = open("file.txt", "r")
data = file.read()
new_data = data.replace('.', '')
new_data_2 = new_data.replace(',', '')
data_lower = new_data_2.lower()
words = data_lower.split()
number_of_words = len(words)

for i in words:
    set1.add((i, words.count(i)))


list1 = list(set1)
sorted_list = list1.sort(key=lambda x:x[1], reverse=True)
print("Sentences in a file: " + "\n" + data)
print("Number of words in a file: " + str(number_of_words))

for i in list1:
    print("Word: "+str(i[0]))
    print("Number of occurrences: "+str(i[1]))



