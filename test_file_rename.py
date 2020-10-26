## Created 20/10/2020
## Note - this script only works if the files meet the following format:
## disk 1 has no identifier - tracks are just numbered 01, 02, 03 etc
## disc 2, 3 etc have identifier (Disk 2) 01, (Disk 3) 14 etc
## any other format, the script will not work
## 


import os

## os.chdir('C:\\Users\\Gerry\\Music\\Amazon Music\\Various artists\\Test_1')## 
os.chdir('C:\\Users\\Gerry\\Music\\Amazon Music\\Pink Floyd\\The Early Years 1965-1967 CAMBRIDGE ST ATION')

## first run set to N just to check file names. Only set to Y when satisfied it'll work for this folder
flag_rename_files = 'Y'

counter = 1

for f in os.listdir():
    dash_count = f.count('-')
    if (dash_count > 1):
        raise Exception("Error - file name " + str(f) + " contains too many - characters. This will cause program to fail. Exiting.")

    ## print ("Analysing file " + str(counter))
    file_name, file_ext = os.path.splitext(f)
    ## print('file_name = ' + str(file_name))
    f_id, f_name = file_name.split('-')
    f_id = f_id.strip()
    f_name = f_name.strip()
    ##print (f_id)

    




    ## get the first character of the string so we can check if it is a bracket
    first_char = f_id[0]
    
    if (first_char == "("):
        ## must be disk 2 or 3. Identify by finding the position of the second bracket
        f_id_end_bracket_position = f_id.find(")")
        ## print ("position of end bracket = " + str(f_id_end_bracket_position))
        
        ## can use this to get the disk no
        disk_no = f_id[f_id_end_bracket_position - 1].zfill(2)
        ## print ("disk number = " + str(disk_no))

        ## create new disk number (needs a leading zero)
        ## disk_no = '0'+disk_no
        ## print ("disk number updated to " + str(disk_no))

        ## Get the track number
        track_number = f_id[f_id_end_bracket_position+2: f_id_end_bracket_position+4]
        ## print (track_number)

        new_track_id = disk_no + "-" + track_number + " - " + f_name + file_ext
        print ("new track id = " + str(new_track_id))


    else:
        ## disk number must be 01
        disk_no = '01'
        ## print ("disk number updated to " + str(disk_no))

        ## track number must be first 2 characters
        track_number = f_id[0:2]
       ##  print ('Track Number on disk 1 is ' + str(track_number))

        ## concatenate

        new_track_id = disk_no + "-" + track_number + " - " + f_name + file_ext
        print ("new track id = " + str(new_track_id))



    if (flag_rename_files) == 'Y':
        os.rename(f, new_track_id)
    
    
    

    
    ## loop control
    counter +=1
