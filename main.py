import turtle
import pandas

screen = turtle.Screen()
screen.title("USA States Game")
img = 'blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv('50_states.csv')

print(data)
screen.exitonclick()