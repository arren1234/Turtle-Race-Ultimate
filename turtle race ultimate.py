import turtle #adds turtle functions
import random #adds random functions
t3 = turtle.Turtle() 
t1 = turtle.Turtle()
t4 = turtle.Turtle()         #adds turtles 3,1,4,6,7
t6 = turtle.Turtle()
t7 = turtle.Turtle()
wn = turtle.Screen() #adds screen
t1.shape("turtle")   
t1.color("green")  #colors and shapes bg and t1
wn.bgcolor("tan")
t2 = turtle.Turtle() 
t2.shape("turtle")#adds shapes and colors turtle 2
t2.color("blue")
t4.shape("turtle")#shapes and colors turtle 4
t4.color("yellow")
t4.up()
t1.up()#raises pen of turtle 1,2,6 and 4
t2.up()
t6.up()
t5 = turtle.Turtle() #adds shapes colors and lifts pen of turtle 5
t5.color("purple")
t5.shape("turtle")
t5.up()
t6.color("black")#colors and shapes turtle 6
t6.shape("turtle")
t7.color("orange")#colors shape a lifts pen of turtle 7
t7.shape("turtle")
t7.up()
t8 = turtle.Turtle()
t8.color("grey")#adds colors shape a lifts pen of turtle 8
t8.shape("arrow")
t8.up()
t9 = turtle.Turtle()
t9.shape("turtle")#adds colors shape a lifts pen of turtle 9
t9.color("pink")
t9.up()
t3.pensize(15)
t3.color("red")
t3.up()
t3.goto(350,-500)#makes finish line using turtle 3
t3.lt(90)
t3.down()
t3.fd(1100)
t1.goto(-350,20)
t2.goto(-350,-20)
t4.goto(-350,-60)
t5.goto(-350, 60)#puts racers in starting position
t6.goto(-350, 100)
t7.goto(-350,-100)
t8.goto(-1400,140)
t9.goto(-350,-140)
t1.speed(1)
t2.speed(1)
t4.speed(1)#sets racer speed
t5.speed(1)
t6.speed(1)
t7.speed(1)
t8.speed(1)
t9.speed(1)
for size in range(1000):#functions as endless loop
    t1.fd(random.randrange(30,70)) #t1 is a green turtle with the very consistent movement
    t2.fd(random.randrange(-20,120)) #t2 is a blue turtle with a slightly higher max but lower min
    t4.fd(random.randrange(10,90))#t4 is a a yellow turtle with a very slightly lower max and higher min
    t5.fd(random.randrange(0,100))#t5 is a purple turtle with standard stats
    t6.fd(random.randrange(-100,200))#t6 is a black turtle with a very high max and low min
    t7.rt(random.randrange(0,360))#t7 is an orange turtle with high max and normal low but random turns
    t7.fd(random.randrange(200,300))
    t8.fd(150)#t8 is a grey space ship with a non random movement of a high 150 but starts much farther back
    t9.fd(random.randrange(-1000,1000))#t9 is a pink turtle with the most random movement with a max of 1000 and min of -1000
