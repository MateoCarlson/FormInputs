from flask import Flask, request, render_template
app = Flask(__name__)

#find character logic:
#ask a series of questions to find right character(s)
#if agressive playstyle
#add damage points
#if passive agressive playstyle
#add damage points
#if clutch playstyle (high risk high reward)
#add tank points
#if very passive
#add support points
#if movement playstyle
#add movement points
#if stationary playstyle
#add stationary points


def select_house(playstyle, movement):
    # create dictionary mapping house names to point values
    classes = { "Damage": 0, "Tank": 0, "Support": 0 }
    style = { "Movement" : 0, "Stationary" : 0 }

    # add points to each class based on how their favorite playstyle aligns
    if playstyle == "Full on agression, no holding back.":
        classes["Damage"] += 1
    elif playstyle == "Let the enemy come to you, then crush them.":
        classes["Damage"] += 2
    elif playstyle == "Wait for the right moment, then save your team.":
        classes["Tank"] += 3
    elif playstyle == "Stay in the back, and let others do your dirty work.":
        classes["Support"] += 4

    # add points to each type based on how their potion aligns
    if movement == "Constant motion, no down time.":
        style["Movement"] += 1
    elif movement == "Slow and methodical":
        style["Stationary"] += 2


    # choose the hero with the highest value
    selected_hero = None
    for hero, points in classes.items():
        if selected_hero is None or classes[selected_hero] < points:
            selected_hero = hero

    # return the selected hero
    return selected_hero


@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    playstyle = request.form.get('input_playstyle', '')
    movement = request.form.get('input_select', '')
    if name is "":
        return render_template("main_page.html", group = 1,
                           output="You did not input a name %s, but you should consider playing:" % name)
    else:
        return render_template("main_page.html", group = 1,
                           output= "Hello %s, you should play:" % name)
