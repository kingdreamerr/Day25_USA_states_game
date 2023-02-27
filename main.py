import turtle
import pandas

screen = turtle.Screen()
screen.title("USA States Game")
img = 'blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)
states_guessed = []

data = pandas.read_csv('50_states.csv')
states_list = data['state'].to_list()


while len(states_guessed) < 50:
    answer = screen.textinput(title=f"{len(states_guessed)}/50 states correct",
                           prompt="what's another state's name?").title()
    
    if answer in states_list:
        states_guessed.append(answer)
        
screen.exitonclick()