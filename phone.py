import turtle

def round_rectangle(length,high,cor_angle,cor_rad):    
    for i in range(2):
        turtle.fd(high)
        turtle.circle(cor_rad,cor_angle)
        turtle.fd(length)
        turtle.circle(cor_rad,cor_angle)      
    
def main():
    turtle.setup(1300,800,0,0)
    pythonsize=3
    turtle.pensize(pythonsize)
    turtle.speed(10)
    turtle.seth(90)
    
    turtle.pencolor("#8E8e8e")
    turtle.penup()  
    turtle.goto(202,-202)
    turtle.pendown()
    round_rectangle(244,484,90,30)

    turtle.penup()  
    turtle.goto(200,-200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#F0F0F0")
    round_rectangle(240,480,90,30)
    turtle.end_fill()
    
    turtle.pencolor("black")
    turtle.penup()  
    turtle.goto(185,-150)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("black")
    round_rectangle(270,380,90,0)
    turtle.end_fill()
 
    turtle.penup()  
    turtle.goto(80,265)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#9d9d9d")
    round_rectangle(60,4,90,1)
    turtle.end_fill()
 
    turtle.penup()  
    turtle.goto(67,290)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#3c3c3c")
    round_rectangle(36,4,90,1)
    turtle.end_fill()
   
    turtle.penup()  
    turtle.goto(0,265)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#3c3c3c")
    turtle.circle(6,360)
    turtle.end_fill()
  
    turtle.pencolor("#9d9d9d")
    turtle.penup()  
    turtle.goto(75,-185)
    turtle.pendown()
    turtle.circle(25,360)
    
    turtle.pencolor("#9d9d9d")
    turtle.penup()  
    turtle.goto(60,-190)
    turtle.pendown()    
    
    turtle.exitonclick()
    
main()
