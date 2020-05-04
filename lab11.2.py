def read_file(filename): #funtion for read file content
    with open(filename, 'r') as file:
        return file.read().split()
        
def save_file(filename, content): #funtion for save file content
    with open(filename, 'w') as file:
        file.write(str(content))
        
def create_mesh(col, row): #funtion for create mesh
    matrix = [['_' for _ in range(col)] for _ in range(row)]
    return matrix
    
def posible_sub_seq(min_dim): #funtion for get possible pattern for 2nd power
    return [2**i for i in range(min_dim) if not(2**i > min_dim)][::-1]

def square_mark(mesh, index, number): # funtion for marking square in mesh
    marking_mesh = mesh.copy() # get copy of main mesh
    
    for i in range(index[0], index[0] + int(float(number))): # get currunt row index
        for k in range(index[1], index[1] + int(float(number))): # get currunt col index
            if marking_mesh[i][k] == '_': # if position empty
                marking_mesh[i][k] = number # mark the squre
            else:
                return False # if alrady fill it return false

    return marking_mesh # if successfully marked then return marked mesh
    
def cal_square(mesh, square_list): # funtion for calculate number of sub square can marked in mesh
    marked_squre = square_list[0] # get marked square dimention
    count = 0 # set marked count is 0
    
    for i in range(0,row, marked_squre): # get row index for start position
        if i + marked_squre > row: # if squre is out in mesh continue
            continue
        
        for k in range(0,col, marked_squre): # get col index for start position
            if k + marked_squre > col: # if squre is out in mesh continue
                continue
            number = str(marked_squre) + '.' + str(count) # create squre idintification value
            temp_mesh = square_mark(mesh, [i, k], number) # save marked mesh in temparory
            if temp_mesh != False: # if not false to mark in mesh
                mesh = temp_mesh # assign temp mesh to currunt mesh
                count += 1 # count the marking
    
    if square_list[1:] == []: # if aleady marked every sub squre in mesh
        global final_mesh # set lobal final mesh
        final_mesh == mesh # assign currunt mesh to final mesh
        return count # return currunt counting value
    else:
        next_count = cal_square(mesh, square_list[1:]) # if not finish marking squres in mesh use recursive it to mark it.
        return next_count + count # return total conut of marking of squres

input_filename = input("Input file: ") # get input file name

col, row = list(map(int, read_file(input_filename))) # split it to col & row

final_mesh = create_mesh(col, row) # create a final mesh
min_seq = cal_square(final_mesh, posible_sub_seq(min(col, row))) # get minimum squre marking of mesh

save_file('result.txt', min_seq) # save min value of marked squres count to file
