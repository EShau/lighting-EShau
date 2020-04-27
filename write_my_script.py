from random import randint

with open('my_script','w+') as fileWriter:
    fileWriter.write("push\n")
    coords = []
    for i in range(2500):
        r = 25
        x,y,z = randint(0,500), randint(0,500), randint(-500,0)
        inside = False
        for ball in coords:
            if abs(x-ball[0]) < 35 and abs(y-ball[1]) < 35 and abs(z-ball[2]) < 35:
                inside = True
                break
        if not inside:
            coords.append([x,y,z])
            fileWriter.write("sphere\n")
            fileWriter.write(str(x) + " " + str(y) + " " + str(z) + " " + str(r) + "\n")
    fileWriter.write("save\n")
    fileWriter.write("ball_pit.png")
