
words = {}
text = str(input("Text: "))
split_text = text.split()
word_list = []
maximum_word_length = 0
for word in split_text:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
        word_list.append(word)
        if len(word) > maximum_word_length:
            maximum_word_length = len(word)
word_list.sort()
for item in word_list:
    print("{:{}} {}".format(item + ":", maximum_word_length + 1, words[item]))
