import turtle
from fileinput import lineno
import random

solution = input
num1 = random.randint(-100,100)
num2 = random.randint(-100, 100)
operation = random.randint(1,4)
if operation == 1:
    symbol = "+"
    num1 = random.randint(-100,100)
    num2 = random.randint(-100, 100)
    solution = num1 + num2
elif operation == 2:
    symbol = "-"
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)
    solution = num1 - num2
elif operation == 3:
    symbol = "*"
    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10)
    solution = num1 * num2
elif operation == 4:
    symbol = "/"
    num1 = random.randint(-10, 10)
    num2 = random.randint(-1, 10)
    sign =  random.randint(1,2)
    if sign == 2:
        num2 = num2 * -1
    solution = num1 / num2

screen = turtle.Screen()
screen.screensize( 500,  500)
screen.bgcolor('black')
t = turtle.Turtle()
t.speed(0)
# menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor('white')
t.write('background color', font = ('arial', 30, 'normal'), align='center')

t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor('tan')
t.write('1.Tan', font = ('arial', 20, 'normal'), align='left')

t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor('azure')
t.write('2.Azure', font = ('arial', 20, 'normal'), align='left')

t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor('aquamarine')
t.write('3.AquaMarine', font = ('arial', 20, 'normal'), align='left')

t.penup()
t.goto(-75,-50)
t.pendown()
t.pencolor('dark khaki')
t.write('4.DarkKhaki', font = ('arial', 20, 'normal'), align='left')

t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor('white')
t.write('Select a color', font = ('arial', 30, 'normal'), align='center')

choose = int(input("Select a color: "))
if choose == 1:
    screen.bgcolor('tan')
elif choose == 2:
    screen.bgcolor('azure')
elif choose == 3:
    screen.bgcolor('aquamarine')
else:
    screen.bgcolor('dark khaki')
t.clear()
t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('black')
t.write('Enter your name: ', font = ('arial', 30, 'normal'), align='center')

name = input("Enter your name: ")
t.clear()
# number1 = int(input("Enter a number: "))

t.penup()
t.goto(0,100)
t.pendown()
t.pencolor('black')
t.write(name, font = ('arial', 30, 'normal'), align='center')



t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor('green')
t.write(num1, font = ('arial', 30, 'normal'), align='center')


# number2 = int(input("Enter a number: "))


t.penup()
t.goto(-50,0)
t.pendown()
t.pencolor('pink')
t.write(num2, font = ('arial', 30, 'normal'), align='center')


if operation == 1:
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.pencolor('black')
    t.write("+", font=('arial', 30, 'normal'), align='center')
elif operation == 2:
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.pencolor('black')
    t.write("-", font=('arial', 30, 'normal'), align='center')

elif operation == 3:
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.pencolor('black')
    t.write("*", font=('arial', 30, 'normal'), align='center')

elif operation == 4:
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.pencolor('black')
    t.write("/", font=('arial', 30, 'normal'), align='center')
# t.penup()
# t.goto(-100,0)
# t.pendown()
# t.pencolor('black')
# t.write("+", font = ('arial', 30, 'normal'), align='center')


# ans1 = number1 + number2


t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('black')
t.write("=", font = ('arial', 30, 'normal'), align='center')

final_ans = int(input("Enter the answer: "))

t.penup()
t.goto(50,0)
t.pendown()
t.pencolor('black')
t.write(solution, font = ('arial', 30, 'normal'), align='center')



t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor('black')
t.write('your answer: '+ str(final_ans), font = ('arial', 30, 'normal'), align='center')



if final_ans != solution:
    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.pencolor('black')
    t.write('close', font=('arial', 30, 'normal'), align='center')
    screen.bgcolor('red')
if final_ans == solution:
    screen.bgcolor('blue')


turtle.done()

#t.write('hhhj', font = ('arial', 30, 'normal'), align='center')


#ts pmo🥀




turtle.done()
