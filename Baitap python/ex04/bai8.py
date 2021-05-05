from collections import Counter
textfile=open("bai8.txt")
lines=textfile.readline()
#s="this is a test this is"
words=lines.split()
print(words)

two_grams = zip(words, words[1:])
counts = Counter(two_grams)
print(counts.most_common())
