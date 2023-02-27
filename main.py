import turtle
import pandas

screen = turtle.Screen()
screen.title("USA States Game")
img = 'blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)
states_guessed = []

data = pandas.read_csv('50_states.csv')


while len(states_guessed) < 50:
    answer = screen.textinput(title=f"{len(states_guessed)}/50 states correct",
                           prompt="what's another state's name?").title()
screen.exitonclick()