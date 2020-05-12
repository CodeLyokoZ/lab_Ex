def read_file(filename): #funtion for read file
    with open(filename, 'r') as file: # open file to read
        content = file.read().split('\n') # get content spliting lines
    buy_list = dict() # assign buy_list dictionary
    for i in content: # for each line in content
        i = i.split('\t') # split using tab
        try: # try to add items in dictionary
            buy_list[i[1]] += i[2].split(',') 
        except:
            buy_list[i[1]] = i[2].split(',')
    return buy_list # return buy list as dictionary
    
def save_file(filename, content): #funtion for save file
    with open(filename, 'w') as file: # open file to write
        address = list(content.keys()) # get address list
        address.sort() # sort address list
        for i in address: # for each address in list
            content[i] = list(set(content[i])) # remove same items in dictionary
            content[i].sort() # sort items
            out_str = "Residents in "+ i + " want to purchase\n" # add address to out string
            out_str += ", ".join(content[i]) + '\n\n' # join items using ','
            file.write(out_str) # write string
        
filename = input() # get file name in terminal
save_file('delivery_plan.txt', read_file(filename)) # save file
