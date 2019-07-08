import turtle
turtle.setup(1300,800,0,0)

def round_rectangle(length,high,cor_angle,cor_rad):    
    for i in range(2):
        turtle.fd(high)
        turtle.circle(cor_rad,cor_angle)
        turtle.fd(length)
        turtle.circle(cor_rad,cor_angle)      
    
def draw_phone(x,y):    
    pythonsize=3
    turtle.pensize(pythonsize)
    turtle.speed(30)
    turtle.seth(90)

    turtle.pencolor("#8E8e8e")
    turtle.penup()  
    turtle.goto(x+202,y+-202)
    turtle.pendown()
    round_rectangle(244,484,90,30)

    turtle.penup()  
    turtle.goto(x+200,y+-200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#F0F0F0")
    round_rectangle(240,480,90,30)
    turtle.end_fill()
    
    turtle.pencolor("black")
    turtle.penup()  
    turtle.goto(x+185,y+-150)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("black")
    round_rectangle(270,380,90,0)
    turtle.end_fill()
 
    turtle.penup()  
    turtle.goto(x+80,y+265)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#9d9d9d")
    round_rectangle(60,4,90,1)
    turtle.end_fill()
 
    turtle.penup()  
    turtle.goto(x+67,y+290)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#3c3c3c")
    round_rectangle(36,4,90,1)
    turtle.end_fill()
   
    turtle.penup()  
    turtle.goto(x+0,y+265)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#3c3c3c")
    turtle.circle(6,360)
    turtle.end_fill()
  
    turtle.pencolor("#9d9d9d")
    turtle.penup()  
    turtle.goto(x+75,y+-185)
    turtle.pendown()
    turtle.circle(25,360)
    
    turtle.pencolor("#9d9d9d")
    turtle.penup()  
    turtle.goto(x+60,y+-190)
    turtle.pendown()    
    

def main():
    draw_phone(0,0)
    draw_phone(300,50)
    draw_phone(500,-400)
    draw_phone(-200,300)
    draw_phone(-600,50)
    turtle.exitonclick()
    
main()
