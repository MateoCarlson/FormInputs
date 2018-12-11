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


"""
def select_house(playstyle, movement):
    # create dictionary mapping house names to point values
    classes = { "Damage": 0, "Tank": 0, "Support": 0 }
    style = { "Movement" : 0, "Stationary" : 0 }

    # add points to each house based on how their favorite spell aligns
    if playstyle == "Agressive":
        classes["Damage"] += 1
    elif playstyle == "Passive Agressive":
        classes["Damage"] += 2
    elif playstyle == "Clutch":
        classes["Tank"] += 3
    elif playstyle == "Very Passive":
        classes["Support"] += 4

    # add points to each house based on how their potion aligns
    if movement == "Faster moving/ Movement based characters":
        style["Movement"] += 1
    elif movement == "Slower moving/ Stationary characters":
        style["Stationary"] += 2


    # choose the house with the highest value
    selected_hero = None
    for hero, points in classes.items():
        if selected_hero is None or classes[selected_hero] < points:
            selected_hero = house

    # return the selected house
    return selected_hero
"""


@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    dropdown = request.form.get('input_dropdown', '')
    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    if name is "":
        return render_template("main_page.html", input_data=dropdown,
                           output="You did not input a name %s, but you should consider playing:" % name)
    else:
        return render_template("main_page.html", input_data=dropdown,
                           output="%s, you should consider playing:" % name)
