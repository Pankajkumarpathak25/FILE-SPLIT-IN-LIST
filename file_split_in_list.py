
x = []
with open('install.txt','r') as f:
    for line in f:
        for word in line.split():
             
             x.append(word)
print x	





