def read_file(filename): # funtion for read file
    file = open(filename, 'r')
    content = list(map(int, file.read().split(',')))
    print(content)
    file.close()
    return content
    
def save_file(filename, content): # funtion for save file
    file = open(filename, 'w')
    file.write(content)
    file.close()
    return
    
def add_bst(i, index = 0): #funtion for add value to binary search tree
    
    l_nod = (index * 2 + 1) # left nod index value
    r_nod = (index * 2 + 2) # right nod index value
    
    if out_list[index] == 'null': # if position is empty assign nod value
        out_list[index] = i
    else:
        if i < out_list[index]: # check wether child value less than pareant value
            add_bst(i, l_nod) # it true then send to value to left sub tree
        else:
            add_bst(i, r_nod) # it false then send to value to rigth sub tree
           
filename = input() # get file name from terminal
main_list = read_file(filename) # get user file content as list

list_len = len(main_list) # Get length of list
out_list = ['null' for _ in range(2**(list_len//2))] # create a empty value complete tree for store value using list

for i in main_list: # get each values in list
    add_bst(i) # send values to tree for assign it to propper nod

for _ in range(1, len(out_list)): # check each element in tree
    if out_list[-1] == 'null': # check if unwanted leaf in tree
        out_list.pop() # pop those unwanted leaf
    else:
        break # if finifh the pop for unwanted leaf break poping leaf
content = ' '.join(list(map(str, out_list))) # create out string for output
save_file('result.txt', content) # save the content
