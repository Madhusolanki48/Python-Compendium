with open('4newfile.txt','w')as file:
    # file.write('This is a new file created !')
    file.writelines(['This is a new file created !','\nThis is another line to be added.'])
    
    
    
    try:
        with open('4newfile2.txt','a')as file:   #--using a we can append in the txt file
            file.writelines(['This is a new file created !','\nThis is another line to be added.'])
    except FileNotFoundError as e:
        print("ERROR",e)


