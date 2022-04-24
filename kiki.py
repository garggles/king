
longest_word = ''
file = open("Data")
words =file.read().split()
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print (longest_word)







#longest_word =max(words, key=len)
#print(longest_word)



