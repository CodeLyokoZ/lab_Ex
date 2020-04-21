def read_file(filename): # funtion for read file
    file = open(filename, 'r')
    content = file.read().split('\n')
    content = [i.split() for i in content]
    file.close()
    return content
    
def save_file(filename, out_cont): # funtion for save file
    file = open(filename, 'w')
    file.write(str(out_cont))
    file.close()
    return

def create_bord(n, m): # funtion for create n X m chess bord 
    bord = [["_" for _ in range(n)] for _ in range(m)]
    return bord

def mark_pos(n,m,val,bord): # funtion for mark position in chess board
    bord[m][n] = val
    return bord

def pos_convert(val,bord): # funtion for convert position valies to list index
    bord_dem = len(bord)
    m = bord_dem - int(val[1])
    n = (ord(val[0])- ord('a'))
    return (n, m)

def atack_pos(n, m, val, bord): # funtion for check attakin possitions
    bord_dem = len(bord)
    if val == 'R': # check if attacking pies is Ruk
        for i in range(bord_dem):
            if bord[m][i] == 'C': # check atakking position horizontally
                return True
                break
            if bord[i][n] == 'C': # check atakking position Vertically
                return True
    
    elif val == 'B': # check if attacking pies is Bishop
        for i in range(bord_dem):
            try:
                if bord[m - i][n - i] == 'C': # check atakking position diaganally
                    return True
            except:
                pass
            try:
                if bord[m + i][n + i] == 'C': 
                    return True
            except:
                pass
            try:
                if bord[m - i][n + i] == 'C': # check atakking position reverse diaganally
                    return True
            except:
                pass
            try:
                if bord[m + i][n - i] == 'C':
                    return True
            except:
                pass
            
    elif val == 'Q': # check if attacking pies is Quine
        if atack_pos(n, m, 'R', bord): # check queen attack like Ruk
            return True
        elif atack_pos(n, m, 'B', bord): # check queen attack like Bishop
            return True
    return False # return attack is Unsuccesful
        
n = 8 # bord dimention
chess_bord = create_bord(n, n) # create a chess bord
attaking = str() # sucsessfully attaking pieses storing variable

filename = input("Input : ") # get input filename from terminal

user_file = read_file(filename) # read user input file content

check_pos = user_file[0][0] # get attacking position
other_pos = user_file[1] # get other pieses positions

pos =  pos_convert(check_pos, chess_bord) # convert attacking postion to list index

mark_pos(pos[0],  pos[1], 'C', chess_bord) # mark attacking position

for i in other_pos: # cheak pieses can attack the attacking position
    pos =  pos_convert(i[1:], chess_bord) # convert pies postion to list index
    mark_pos(pos[0],  pos[1], i[0], chess_bord) # mark pies position
    
    if atack_pos(pos[0],  pos[1], i[0], chess_bord): # check wether attack was succesfull
        attaking += i + ' '

save_file('result.txt', attaking[:-1]) # save succesfully attacked pieses
