from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=600, height=500)
race_is_on = False
user_guess = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_positions = [-100, -60, -20, 20, 60, 100,]
all_turtles = []



for numbers in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[numbers])
    new_turtle.penup()
    new_turtle.goto(x=-280, y=starting_positions[numbers])
    all_turtles.append(new_turtle)


if user_guess:
    race_is_on = True

while race_is_on:

    for turtle in all_turtles:
        if turtle.xcor() > 280:
            race_is_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_guess:
                print(f"You won. The {winning_colour} turtle is the winner.")
            else:
                print(f"You lost. The {winning_colour} turtle is the winner.")


        rand_dist = random.randint(-1, 10)
        turtle.forward(rand_dist)

screen.exitonclick()