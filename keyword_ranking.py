import string

text = open('b.txt', 'r')
text = text.read()

words = []
dictionary = {}


def removePunctuation(st):
    for c in string.punctuation:
        st = st.replace(c, '')
    return st


def lowerSplit(st):
    st = st.lower()
    st = st.split()
    return st


def countWord(word, st):
    count = st.count(word)
    return count


def nonRepeats(wordList):
    global words
    for i in range(0, len(wordList)):
        if wordList[i] not in words:
            words.append(wordList[i])
    return words


text = removePunctuation(text)
text = lowerSplit(text)
words = nonRepeats(text)

print(len(text))
print(len(nonRepeats(text)))

for i in range(0, len(words)):
    dictionary[words[i]] = countWord(words[i], text)

rankedList = sorted(dictionary, key=dictionary.get, reverse=True)
print(len(rankedList))

for i in range(0, len(rankedList)):
    print(rankedList[i] + ' repeats ' + str(dictionary[rankedList[i]]) + ' times')