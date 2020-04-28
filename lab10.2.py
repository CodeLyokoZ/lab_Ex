def read_file(filename): # funtion for read file
    file = open(filename, 'r') # open file read-only
    content = file.read().split('\n') # split content to lines
    m, n = list(map(int, content[0].split())) # get matrix dimention
    matrix = [list(map(int, content[i].split())) for i in range(1,m+1)] # create a matrix using content
    ptn_num = content[-1] # get pattern number
    file.close() # closing Opend file
    return ((m,n), matrix, ptn_num) # retuning values
    
def save_file(filename, content): # funtion for save file
    file = open(filename, 'w') # open file write-only
    file.write(content) # write the content
    file.close() # close the file
    return 0 # if program run sucessfully retrun 0

def ptn_search(matrix, ptn_number): # funtion for get pttarn number paths
    global row, col
    if ptn_number == "": # if serching for pattern end return True
        return True
    index_val = [[m,n] for m in range(len(matrix)) for n in range(len(matrix[m])) if matrix[m][n] == int(ptn_number[0])] # find the first of ptn_number positions
    
    if index_val == []: # if can't find a pttern number return False
        return False
    
    next_val = ptn_search(matrix, ptn_number[1:]) # use recursive methord for check next digit in matrix
    
    if next_val == True: # if pattern reach the end retuning paths list
        return [[i] for i in index_val]
    elif next_val == False: # if can't find possible paths for pattern returning False
        return False
        
    path_list = [[i] + j for i in index_val for k in posibility(i, row, col) for j in next_val if k == j[0]] # genarating possible paths
    return path_list # returning paths list
    
def remove_dub(array): #Funtion for remove looping paths
    for i in array.copy():
        for k in i:
            if i.count(k) != 1:
                array.remove(i)
                break
    return array
    
def posibility(index, r, c, dim = 1): # selecting possible mesh for path finding area accoding to index
    return [[index[0] + m, index[1] + n] for m in range(-dim, dim+1) for n in range(-dim, dim+1) if not(index[0] + m < 0 or index[1] + n < 0 or index[0] + m > r or index[1] + n > c or (m == 0 and n == 0)) ]    

filename = input() # get input file name from terminal 
user_input = read_file(filename) # read user file
row, col = user_input[0]
paths = ptn_search(user_input[1], user_input[2]) # get possible paths

if paths != False: # if any pattern found in matrix
    final_paths = remove_dub(paths) # remove looping paths
    final_paths.sort() # sorting paths
    content = str() # create empty string
    for i in final_paths:
        content += str(i) + '\n' # creating Final string
else: # if path couldn't found 
    content = "No occurrences found" #write in content paths couldn't found
    
save_file('result.txt', content) # save the final content
