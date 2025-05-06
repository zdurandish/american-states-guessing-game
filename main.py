from turtle import Turtle, Screen
import pandas

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

screen = Screen()
screen.title("U.S. States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:
    user_guess = screen.textinput(title=f"{len(guessed_states)}/50 Correct Answers!", prompt= "Guess a State!").title()

    if user_guess == "Exit":
        states_to_learn = [state for state in states if state not in guessed_states]
        new_file = pandas.Series(states_to_learn)
        new_file.to_csv("states_to_learn.csv")
        break
    if user_guess in states:
        guessed_states.append(user_guess)
        xcor = data[data.state == user_guess].x.item()
        ycor = data[data.state == user_guess].y.item()
        turt = Turtle()
        turt.hideturtle()
        turt.penup()
        turt.goto(xcor, ycor)
        turt.write(user_guess)