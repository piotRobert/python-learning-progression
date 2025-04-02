import turtle, pandas

PROJECT_FILES = "d25_csv_data_and_pandas/d25_states_game/"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(750,500)
image = f"{PROJECT_FILES}/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
guessed_states = []
data = pandas.read_csv(f"{PROJECT_FILES}50_states.csv")
all_states = data.state.to_list()

t = turtle.Turtle()
t.hideturtle()
t.penup()
screen.tracer(0)

while len(guessed_states) < 50 :

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv(f"{PROJECT_FILES}states_to_learn.csv")

        break
    if answer_state in all_states:
        if answer_state not in guessed_states:
            state_data = data[data.state == answer_state]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer_state, align="center", font=("Arial", 10, "normal"))
            guessed_states.append(answer_state) 