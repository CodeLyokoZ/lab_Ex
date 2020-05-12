def read_file(filename): # funtion for read file
    global GPA_list # get global GPA_list
    pref = dict() # create a dictionary to store data
    
    with open(filename, 'r') as file: # open a file with read permissions
        content = file.read().split('\n') # split the lines
    
    
    for i in content: # in each line
        i = i.split() # split it using space
        GPA = i[1] # get GPA
        
        try: # try to add user data using GPA as a Key
            pref[GPA] +=  [[i[0]] + list_sort([(k.split(':')[1],k.split(':')[0]) for k in i[2:]])]
        except:
            pref[GPA] =  [[i[0]] + list_sort([(k.split(':')[1],k.split(':')[0]) for k in i[2:]])]
            
    GPA_list = list(pref.keys()) # add GPA to global list
    GPA_list.sort(reverse = True) # sort the GPA values
    
    return pref # return data dictionary

def save_file(filename, content): # funtion for save file
    with open(filename, 'w') as file: # open a file with writing permissions
        file.write("Cut-off GPA = " + content[-1][0] + '\n') # write headding to file
    
        for i in content: # for each index
            file.write(i[1] + '\n') # write reach index in to file
    
def list_sort(li): # funtion for list sort & return a list
    li.sort()
    return li
    
def sec_sort(li): # funtion for retrun second value in list
    return li[1]
    
def select(sub): # funtion for return selected index & GPA for specefic subject
    cap = {'BM': 15, 'CH': 100, 'CE': 100, 'CS': 125, 'EE': 100, 'EN': 100, 'ME': 100, 'MT': 50} # each subject capacity values
    selected_dict = dict() # create a dictionary to store selected students
    
    for i in GPA_list: # each GPA
        for k in per[i]: # in each persons's data
            for j in range(1,len(k)): # each selection oder
                try: # try to assign them to a subject
                    if len(selected_dict[k[j][1]]) < cap[k[j][1]]: # if capacity values is not exceed
                        selected_dict[k[j][1]] += [[i, k[0]]] # add them
                        break
                except:
                    selected_dict[k[j][1]] = [[i, k[0]]]
                    break
                
    sub_selected = selected_dict[sub] # get selected index list requested subject
    sub_selected.sort(key = sec_sort) # sort it using index
    sub_selected.sort(reverse = True) # sort it using GPA
    
    return sub_selected # return it
                
GPA_list = list() # create a GPA list
per = read_file('preferences.txt') # Get students details
sub = input() # get user requested subject code name
save_file('selected.txt', select(sub)) # save file
