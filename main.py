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




screen.exitonclick()