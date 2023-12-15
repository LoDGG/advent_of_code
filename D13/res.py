#Open Input.txt file
file = open("input.txt", "r")
input = []
pattern = []
#Read the file
for lines in file:
    if lines != "\n":
        
        
        pattern.append(lines.rstrip('\n'))
    else:
        input.append(pattern)
        print(pattern)
        pattern.clear()
        
#Horizontal Iteration :
for i in range(0,len(input)):
    for j in range(0,len(input[i])):
        


#Vertical Iteration :
for j in range(0,len(input[i])):
    for i in range(0,len(input)):
