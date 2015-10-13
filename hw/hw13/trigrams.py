import random

file = open('sherlock.txt', 'r')
lines = file.readlines()

words = []
trigrams = {}

start = "returning from"

for i in lines:
    words += i.split()

for i in (range(len(words) - 2)):
    phrase = words[i] + " " + words[i + 1]

    if (phrase in trigrams):
        trigrams[phrase].append(words[i + 2])
    else:
        trigrams[phrase] = [words[i + 2]]

end = True

word_1 = start.split()[1]
word_2 = start.split()[0]
new = start
j = 0

while end:
    j = j + 1
    phrase = word_2 + " " + word_1
    if (phrase in trigrams.keys()):
        numb_of_words = len(trigrams[phrase]) - 1
        i = random.randint(0, numb_of_words)
        list_words = trigrams[phrase]
        new_word = list_words[i]
        new = new + " " + new_word
        word_2 = word_1
        word_1 = new_word
    else:
        end = False

print(new)
file.close()