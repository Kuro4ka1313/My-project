from levels import levels
from playground import canvas, window, walls, keys, doors, exits, players, createlevel, secrets
currentLevel=0
createlevel(levels[currentLevel])
def playerMove(event):
    global currentLevel
    player=players[0]
    key=event.keysym
    x=0
    y=0
    if key=="Up":
        y-=5
    if key=="Down":
        y+=5
    if key=="Right":
        x+=5
    if key=="Left":
        x-=5
    canvas.move(player, x, y)
    for wall in walls:
        x1, y1, x2, y2=canvas.coords(wall)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            canvas.move(player, -x, -y)
    for key in keys:
        x1, y1, x2, y2=canvas.coords(key)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            canvas.delete(key)
            keys.remove(key)
            if len(keys)==0:
                for door in doors:   
                    canvas.itemconfig(door, fill="green")
    for door in doors:
        x1, y1, x2, y2=canvas.coords(door)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            if canvas.itemcget(door, "fill")=="red":
               canvas.move(player, -x, -y)
    for exit in exits:
        x1, y1, x2, y2=canvas.coords(exit)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            currentLevel+=1
            canvas.delete("all")
            if currentLevel<len(levels):
                createlevel(levels[currentLevel])
            else:
                canvas.create_text(225, 225, text="You Won The Game", fill="red", font="Arial 20")
                canvas.unbind_all("<Key>")
                return
    for secret in secrets:
        x1, y1, x2, y2=canvas.coords(secret)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            canvas.move(player, -x, -y)
canvas.bind_all("<Key>", playerMove)
window.mainloop()   
