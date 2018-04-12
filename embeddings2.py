with open('words.lst') as f:
    lines = f.readlines()
    words = []
    for line in lines:
        line = line.strip()
        words.append(line)
#print(words)
#print(len(words))#130000

with open('embeddings.txt') as f:
    lines = f.readlines()
    embeddings = []
    for line in lines:
        line = line.strip().split()
        embeddings.append(line)

print(len(embeddings[0]))
print(type(embeddings[0]))#<class 'list'>
print(type(embeddings[0][0]))#<class 'str'>

with open('embeddings.txt') as f:
    lines = f.readlines()
    embeddings = []
    for line in lines:
        embeddings.append(line)

with open('embeddings2.txt','w') as f:
    for i,word in enumerate(words):
        f.write(word+' ')
        f.write(embeddings[i])