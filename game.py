import turtle
import math
import random
import os



BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
ENEMY_COUNT = 5
BASE_X, BASE_Y = 0, -300





class Missile:

    def __init__ (self,x, y, color, x2, y2):
        self.x = x
        self.y = y
        self.color = color

        pen = turtle.Turtle(visible=False)
        pen.speed(0)
        pen.color(color)
        pen.penup()
        pen.setpos(x=x, y=y)
        pen.pendown()
        heading = pen.towards(x2,y2)
        pen.setheading(heading)
        pen.showturtle()
        self.pen = pen

        self.state = 'launched'
        self.target = x2,y2
        self.radius = 0


    def step(self):
        if self.state == 'launched':
            self.pen.forward(4)
            if self.pen.distance(x=self.target[0], y=self.target[1]) <20:
               self.state = 'explode'
               self.pen.shape('circle')
        elif self.state == 'explode':
            self.radius += 1
            if self.radius > 5 :
                self.state = 'dead'
                self.pen.clear()
                self.pen.hideturtle()
            else:
                self.pen.shapesize(self.radius)
        elif self.state == 'dead':
            self.pen.clear()
            self.pen.hideturtle()

    def distance (self, x , y):
        return self.pen.distance(x=x,y=y)

   
    def get_x(self):
        return self.pen.xcor()
  
    def get_y(self):
        return self.pen.ycor()    

class Building:
    def __init__(self,x,y,name):
        self.name = name

        pen = turtle.Turtle()
        pen.hideturtle 
        pen.speed(0)
        pen.penup()
        pen.setpos(x=x, y=y)
        pic_path = os.path.join(BASE_PATH, "images",self.get_pic_name())
        window.register_shape(pic_path)
        pen.shape(pic_path)
        pen.showturtle()
        self.health = 2000
        self.pen = pen

    def get_pic_name(self):
        return f"{self.name}_1.gif"


class MissileBase(Building):
    def get_pic_name(self):
        return f"{self.name}.gif"



class Base:
    
    def __init__(self,x,y,type):
        self.position_x = x
        self.positionn_y = y
        self.model = type
        self.health = 2000
        self.hit_damage = 100

        pen_base = turtle.Turtle(visible=False)
        pen_base.speed(0)
        pen_base.penup()
        pen_base.setpos(x=x,y=y)
        picture = ('images/base.gif')
        window.register_shape(picture)
        pen_base.showturtle()


def fire_missile(x,y):    
    info = Missile (color='white',x=BASE_X,y=BASE_Y,x2=x,y2=y)
    our_missiles.append(info)

def fire_enemy_missile():
    missile_x = random.randint(-600, 600)
    info = Missile (color='red',x=missile_x,y=400,x2=BASE_X,y2=BASE_Y)
    enemy_missiles.append(info)


def move_missiles(missiles):
    for missile in missiles :
        missile.step()
            
    dead_missiles = [missile for missile in missiles if missile.state == 'dead']
    for dead in dead_missiles:
        missiles.remove(dead)


def check_enemy_count():
    if len(enemy_missiles) < ENEMY_COUNT:
       fire_enemy_missile()



def check_interceptions():
    for our_missile in our_missiles:
        if our_missile.state != 'explode':
            continue
        for enemy_missile in enemy_missiles :
            if enemy_missile.distance(our_missile.get_x(), our_missile.get_y()) < our_missile.radius * 10 :
                    enemy_missile.state = 'dead'






def game_over():
    return base.health < 1


def check_impact():
    for enemy_missile in enemy_missiles :
         if enemy_missile.state !='explode':
             continue
         if enemy_missile.distance(BASE_X,BASE_Y) < enemy_missile.radius * 10 :
            base.health -=100


window = turtle.Screen()
window.setup(1200 + 3, 800 + 3)
window.screensize(1200, 800)
window.bgpic(os.path.join(BASE_PATH, "images", "background.png"))
window.tracer(n=1)
window.onclick(fire_missile)

our_missiles = []
enemy_missiles = []
buildings = []

base = MissileBase(x=BASE_X,y=BASE_Y, name='base')
buildings.append(base)

building_infos = {
    'house':[BASE_X - 400, BASE_Y],
    'kremlin':[BASE_X - 200, BASE_Y],
    'nuclear':[BASE_X + 200, BASE_Y],
    'skyscraper':[BASE_X + 400, BASE_Y]
}



for name,position in building_infos.items():
    base = Building(x=position[0],y=position[1], name=name)
    buildings.append(base)




while True:
    window.update()
    if game_over():
        continue
    check_impact()
    check_enemy_count()
    check_interceptions()
    move_missiles(missiles=our_missiles)
    move_missiles(missiles=enemy_missiles)
    








           
           
            
                        
