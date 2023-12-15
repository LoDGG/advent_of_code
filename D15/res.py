
file = open("./D15/input.txt", "r")

# Pasrse file into list of words (each word is sperated by a comma)
words = file.read().split(",")


parsed = []
for word in words:
    for i in range(len(word)):
        if word[i] == '=' or word[i] == '-':
            label = word[:i]
            op = word[i]
            value = word[i+1:]
            parsed.append([label, op, value])

def hash(str):
    curr:int = 0 
    for c in str:
        c = int(ord(c))

        curr+=c
        curr*=17
        curr%=256
        
    return curr


def sum(l):
    s=0
    for word in l:
       s+=hash(word)
    return s

changed = False
boxes = [[] for _ in range(256)]
for word in parsed:
    if word[1] == '=':
        for lens in boxes[hash(word[0])]:
            if lens[0] == word[0]:
                lens[1] = word[2]
                changed = True
                break
            
            
        if not changed : 
            boxes[hash(word[0])].append([word[0], word[2]])
    
    
    elif word[1] == '-':
        for lens in boxes[hash(word[0])]:
            if lens[0] == word[0]:
                boxes[hash(word[0])].remove(lens)
    changed = False
    print("After word : ", word)
    print("Box ", hash(word[0]) , ":" , boxes[hash(word[0])])
    print()


res=0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
           res+=(i+1)*(j+1)*int(boxes[i][j][1])
print(res) 
#print(hash("cm"))
#print(sum(words)) 