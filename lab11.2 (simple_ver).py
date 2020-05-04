def read_file(filename): #funtion for read file content
    with open(filename, 'r') as file:
        return file.read().split()
        
def save_file(filename, content): #funtion for save file content
    with open(filename, 'w') as file:
        file.write(str(content))
    
def posible_sub_seq(min_dim): #funtion for get possible pattern for 2nd power
    return [2**i for i in range(min_dim) if not(2**i > min_dim)][::-1]
    
def cal_square(square_list, prev_val = 0): # funtion for calculate number of sub square can marked in mesh
    posible_sq = row//square_list[0] * col//square_list[0] # get all possible square count
    
    if square_list[1:] == []: # if next suare is empty
        return posible_sq - prev_val * 4 # return posiible square count
    else:
        return cal_square(square_list[1:], posible_sq) + posible_sq - prev_val * 4 # return posiible square count
        
input_filename = input("Input file: ") # get input file name

col, row = list(map(int, read_file(input_filename))) # split it to col & row

min_seq = cal_square(posible_sub_seq(min(col, row))) # get minimum squre marking of mesh

save_file('result.txt', min_seq) # save min value of marked squres count to file
