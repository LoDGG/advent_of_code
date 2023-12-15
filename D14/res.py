#Open Input.txt file
file = open("input.txt", "r")
input = []
map = []
#Read the file
for lines in file:
    map.append(list(lines.rstrip('\n')))

def display(map) : 
    for m in map:
        print(''.join([str(i) for i in m]))
        

#Vertical Iteration :
def North_tilt(map):
    i=0
    for j in range(0,len(map[i])):
        empty = -1
        for i in range(0,len(map)):

            if empty == -1 and map[i][j] == '.' :
                empty = i
            if map[i][j] == '#' :
                empty = -1
            elif map[i][j] == 'O' and empty != -1 :

                map[i][j] = '.'
                map[empty][j]='O'
                empty += 1
            '''
            while ( map[b][j] == 'O' and b > 0 and b < len(map)) :

                if map[b-1][j] == '.' :
                    map[b-1][j] = "O"
                    map[b][j] = '.'
                b -= 1
            '''
def South_tilt(map):
    i=0
    for j in range(0,len(map[i])):
        for i in range(len(map)-1,-1,-1):
            b = i
            while b < len(map)-1 and b >= 0 and map[b][j] == 'O' :

                if map[b+1][j] == '.' :
                    map[b+1][j] = "O"
                    map[b][j] = '.'
                b += 1

def East_tilt(map):
    for i in range(0,len(map)):
        for j in range(len(map[i])-1,-1,-1):
            b = j
            while b < len(map[i])-1 and b >= 0 and map[i][b] == 'O' :

                if map[i][b+1] == '.' :
                    map[i][b+1] = "O"
                    map[i][b] = '.'
                b += 1


def West_tilt(map):
    for i in range(0,len(map)):
        for j in range(0,len(map[i])):
            b = j
            while ( map[i][b] == 'O' and b > 0 and b < len(map[i])) :

                if map[i][b-1] == '.' :
                    map[i][b-1] = "O"
                    map[i][b] = '.'
                b -= 1

                    

def load(map):
    load = 0
    for i in range(0,len(map)):
        for j in range(0,len(map[i])):
            if map[i][j] == 'O':   
                load += len(map)-i
    return load

def cycle(map,n):
    tries = []
    for i in range(1,n+1):
        print(i)


        old = []
        for lines in map:
            old.append(lines.copy())    
        
        tries.append(old)


        North_tilt(map)

        West_tilt(map)

        South_tilt(map)
 
        East_tilt(map)

        for olds in range(0,len(tries)) :
            if tries[olds] == map :
                print("try no : ",olds,"is equal to new")
                display(tries[olds])

                print("new ", i, ":")
                display(map)
                return i
    
       
    return i 
        

print()
#North_tilt(map)
print(cycle(map,120))
#print(cycle(map,1000000000%1228))
#print((1000000000)%(1228-209))
#print(1228-209)


print((1000000000-94)%(138-94)+94)

print()
print(load(map))