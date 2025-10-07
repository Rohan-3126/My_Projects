import turtle

def screen_prompt():
    screen = turtle.Screen()
    screen.setup(750,750)
    screen.bgcolor("white")
    filename1 = turtle.textinput("File name","Enter the source file name with extension.")
    filename2 = turtle.textinput("File name","Enter the received file name with extension.")
    return filename1, filename2

def art():
    art = r'''

   ___ _               _                        
  / __\ |__   ___  ___| | _____ _   _ _ __ ___  
 / /  | '_ \ / _ \/ __| |/ / __| | | | '_ ` _ \ 
/ /___| | | |  __/ (__|   <\__ \ |_| | | | | | |
\____/|_| |_|\___|\___|_|\_\___/\__,_|_| |_| |_|

            '''
    return(art)


def open_file(filename):
    
    f = open(filename)
    data = []
    for i in f:
        data.append(i)
    return data
    f.close()

def checksum(lst,seed):
    data = 0
    for i in lst:
        for j in i:
            datum = ord(j)
            data += datum
    data_value = data % seed
    checksum = data_value ^ seed
    return(checksum)
