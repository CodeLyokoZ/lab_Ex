def read_file(filename): # funtion for read file
    with open(filename, 'r') as file: # open a file with read permisson
        content = file.read().split('\n') # get each lines
    return content # retrun content
    
def save_file(filename, content): # funtion for write file
    with open(filename, 'w') as file: # open a file with write permission
        file.write("Number of spot changes: " + str(content[0]) + '\n') # write first line
        file.write("Number of inserts: " + str(content[1]) + '\n') # write second line 
    
def get_mutation(ancestor, child): # funtion for get mutation insertation & spot change
    if ancestor == child: # if ancestor equal to child
        return [[0, 0, 1]] # nothing have to change
        
    if len(ancestor) == 1: # if ancector's last letter
        deffer = len(child) - len(ancestor) # get deffernt between ancector & child length
        if deffer < 0: # if differnt is minus 
            return [[0, 0, 0]] # return impossibility
        elif deffer > 0: # if deferent is positive
            if ancestor[0] == child[0]: # ancector & child first lettor is equal
                return [[0, deffer, 1]] # retern as 0 insersation & value of differnt is spot changes
            else:
                return [[1, deffer - 1, 1]] # # retern as 1 insersation & value of (differnt - 1) is spot changes
        else : # if defernt is 0
            return [[1, 0, 1]] # return one insersation
            
    mute = [] # create mutation value list    
    if ancestor[0] == child[0]: # ancector & child first lettor is equal
        mute += [i for i in get_mutation(ancestor[1:], child[1:]) if i[2] == 1] # get inserstion & spot changes using recursively
    else:
        mute += [[i[0] + 1, i[1], 1] for i in get_mutation(ancestor[1:], child[1:]) if i[2] == 1] # get inserstion & spot changes using recursively

        if len(ancestor) != len(child): # if length not equal
            mute += [[i[0], i[1] + 1, 1] for i in get_mutation(ancestor, child[1:]) if i[2] == 1]

    return mute # return final mutation list

ancestor, child = read_file(input()) # get ancestor & child values
save_file('result.txt', min(get_mutation(ancestor, child))) # save posible value
