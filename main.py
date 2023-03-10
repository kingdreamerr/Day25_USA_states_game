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
    if answer == "Exit":
        break

    if answer in states_list:
        states_guessed.append(answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer] 
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)

un_guessed_names = []

for states in states_list:
    if states not in states_guessed:
        un_guessed_names.append(states)
    new_data = pandas.DataFrame(un_guessed_names)
    new_data.to_csv('states to learn.csv')
screen.exitonclick()