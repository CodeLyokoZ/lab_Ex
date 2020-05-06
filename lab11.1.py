def read_file(filename): # funtion for read file
    with open(filename,'r') as file:
        content = file.read().split('\n')
        content = [i.split(',')for i in content]
        contact_history = dict()
        for i in content:
            try:
                contact_history[i[2]] += [i[:2]]
            except:
                contact_history[i[2]] = [i[:2]]
        return contact_history
        
def save_file(filename, content): # funtion for write file
    with open(filename, 'w') as file:
        file.write(content)

def date_change(c_date, val): # date calculator
    months_day = {'1':31, '2':30, '3':31, '4':30, '5':31, '6':30, '7':31, '8':31, '9':30, '10':31, '11':30, '12':31}
    dd, mm, yy = list(map(int, c_date.split('-')))
    if val > 0:
        if dd + val > months_day[str(mm)]:
            dd += (val - months_day[str(mm)])
            mm += 1
        else:
            dd += val
    elif val < 0:
        if dd + val > 0:
            dd += val
        else:
            mm -= 1
            dd += (months_day[str(mm)] + val)

    return "{:2.0f}".format(dd).replace(" ", "0") + '-' + "{:2.0f}".format(mm).replace(" ", "0") + '-' + str(yy)
    
def get_contact(id_no, date): # funtion for get quarantine id numbers in contact list
    global qua_list
    qua_list += [id_no]
    while True:
        try:
            for i in contact_history[date]:
                for k in i:
                    if k not in qua_list and id_no in i:
                        get_contact(k, date)
        except:
            pass
        date = date_change(date, 1)
        if date == found_date:
            break

contact_history = read_file('contact_history.txt') # get contact history

id_no, found_date = input().strip().split() # get id no & found date

qua_list = list() # create quarantine id list

get_contact(id_no, date_change(found_date, -14)) # run funtion for filter that contact persons id no

qua_list.remove(id_no)
qua_list.sort() # sort it

out_content = 'Following persons in the contact cluster of ' + id_no + ' should self-isolate\n' # add headline to string
for i in qua_list: # add quarantine id no to string
    out_content += i + '\n'
save_file('quarantine.txt', out_content) # save output
