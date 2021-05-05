import math
position=[0,0]
while True:
    enter=input()
    if not enter:
        break
    enter=enter.split(" ")
    number=int(enter[1])
    mov=enter[0]
    if mov=="UP":
        position[0]+=mov
    elif mov=="DOWN":
        position[0]-=mov
    elif mov=="LEFT":
        position[1]-=mov
    elif mov=="RIGHT":
        position[1]+=mov
    else:
        pass
print(int(round(math.sqrt(position[0]**2+position[1]**2))))