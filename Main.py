import turtle, os, math, random, winsound, platform

window = turtle.Screen()
window.bgcolor("Black")
window.title("Space Invaders")
window.bgpic("background.gif")
window.tracer(0)


score = 0

turtle.register_shape("invader.gif")
turtle.register_shape("ship.gif")
turtle.register_shape("ship2.gif")

#Res de jogo
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()

#jogador

player = turtle.Turtle()
player.color("Green")
player.shape("ship2.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

#Score

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.setposition(-290, 280)
scorestring = "Score: %s" %score
pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
pen.hideturtle()


#invaders
num_Enemy = 30
enemies = []

for i in range(num_Enemy):
    enemies.append(turtle.Turtle())

enemy_start_x = -220
enemy_start_y = 250
enemy_number = 0


for enemy in enemies:    
    enemy.color("red")
    enemy.speed(0)
    enemy.penup()
    enemy.shape("invader.gif")
    x = enemy_start_x + (50*enemy_number)
    y = enemy_start_y 
    enemy.setposition(x,y)
    enemy_number += 1

    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0

enemyspeed = 0.1 


#weapon
weapon = turtle.Turtle()
weapon.color("yellow")
weapon.shape("triangle")
weapon.penup()
weapon.speed(0)
weapon.setheading(90)
weapon.shapesize(0.5,0.5)
weapon.hideturtle()

weaponspeed = 0.3

#estado da arma

weaponready = "ready"

#Sound

def play_sound(sound_file, time = 0):
    if platform.system() == "Windows":
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    elif platform.system() == "Linux":
        os.system("aqplay -q {}&".format(sound_file))
    else:
        os.system("afplay {}&".format(sound_file))

time = 0

if time > 0:
    turtle.ontimer(lambda: play_sound(sound_file, time), t=int(time*1000))





#funções de movimento
def esquerda():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def direita():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def firing_weapon():
    global weaponready
    if weaponready == "ready":
        x = player.xcor()
        y = player.ycor() + 10
        weapon.setposition(x,y)
        weapon.showturtle()
        winsound.PlaySound("Gun pistol shot silenced.wav", winsound.SND_ASYNC)
    
#hitbox a partir de distâncias    
def colisao(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+(math.pow(t1.ycor()-t2.ycor(),2)))
    if distance < 20:
        return True
    else:
        return False



window.listen()
window.onkeypress(esquerda, "Left")
window.onkeypress(direita, "Right")
window.onkeypress(firing_weapon, "space")


while True:
    window.update()

    
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)


        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        
          #Colisão
        if colisao(weapon, enemy):
            weapon.hideturtle()
            weaponready == "ready"
            weapon.setposition(0,-400)
            x = random.randint(-200, 200)
            y = random.randint(100,250)
            enemy.setposition(x,y)
            winsound.PlaySound("Roblox Explosion Sound Effect.wav", winsound.SND_ASYNC)
            score += 1
            scorestring = "Score: %s" %score
            pen.clear()
            pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
    
        if colisao(enemy, player):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    #movimentos da bala
        y = weapon.ycor()
        y += weaponspeed
        weapon.sety(y)

        if weapon.ycor() > 275:
            weapon.hideturtle()
            weaponready == "ready"



       
