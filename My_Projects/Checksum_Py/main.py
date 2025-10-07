import mods
import turtle
turtle.hideturtle()
turtle.penup()

header = mods.art()
print(header)

seed_text = turtle.textinput("Seed value","Enter the seed value : ")
seed = int(seed_text)
if seed < 600:
    turtle.goto(0,180)
    turtle.write("UNAUTHORISED SEED VALUE",align="center", font=("Courier", 33, "bold"))
    turtle.goto(0,100)
    turtle.write("The seed value must be within the range of 600 to 700.",align = "center",font=("Standard",16))
    turtle.Screen().bgcolor("#FFFF8F")
    print("=====================================")
    print("You have entered the wrong seed value")
    print("=====================================")
    
elif seed > 600 and seed < 700:
    filename1,filename2 = mods.screen_prompt()

    data1 = mods.open_file(filename1)
    data2 = mods.open_file(filename2)

    cksum1 = mods.checksum(data1,seed)
    cksum2 = mods.checksum(data2,seed)

    
    turtle.goto(-50,-100)
    turtle.write(f"Checksum of source file     : {cksum1}",align = "center",font=("Standard",16))
    

    print("\n")

    turtle.goto(-50,-150)
    turtle.write(f"Checksum of received file   : {cksum2}",align = 'center',font=("Standard",16))
    

    print("\n")
    print(cksum1)
    print(cksum2)

    turtle.goto(0,0)
    turtle.write(f"The entered source file is   : \n {filename1}",align="center",font=("Standard",16,))

    print("\n")
    
    turtle.goto(0,-50)
    turtle.write(f"The entered received file is : \n {filename2}",align="center",font=("Standard",16,))
    print("\n")


   
    if (cksum1 == cksum2):
    
        turtle.goto(0,180)
        turtle.write("THE FILE IS SAFE",align="center", font=("Courier", 33, "bold"))
        turtle.Screen().bgcolor("#3DED97")
        print("============================================")
        print("The file is safe to use. It is not corrupted")
        print("============================================")
    
    else:
    
        turtle.goto(0,180)
        turtle.write("THE FILE IS NOT SAFE",align="center", font=("Courier", 33, "bold"))
        turtle.Screen().bgcolor("#FA8072")
        print("============================================================")
        print("The file may be corrupted, take caution while using the file")
        print("============================================================")


    checksum = 'checksum.gif'
    turtle.Screen().register_shape(checksum)
    turtle = turtle.Turtle(shape=checksum)
    turtle.penup()
    turtle.goto(0,300)
    turtle.stamp()
    turtle.hideturtle()

else:
    pass
            
    
            
    
    
    
