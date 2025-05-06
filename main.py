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
states_to_learn = []

while len(guessed_states) < 50:
    user_guess = screen.textinput(title=f"{len(guessed_states)}/50 Correct Answers!")

    if user_guess == "Exit":
        for state in states:
            if state not in guessed_states:
                states_to_learn.append(state)
                new_file = pandas.Series(states_to_learn)
                new_file.to_csv("states_to_learn.csv")
        break
    
screen.exitonclick()