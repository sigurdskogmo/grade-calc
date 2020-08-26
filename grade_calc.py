# This program is only intended to give an approximate and does not necessarily represent the teacher's grading.

from grade_scale import grades

def get_value(message, min_val):
    while True:
        user_input = input(message)
        try:
            val = int(user_input)
            if val >= min_val:
                break
            else:
                print(f"Must be higher than {min_val}, try again")
        except ValueError:
            print("Not an integer! Try again.")
    return val

def calc_grade():   
    pts = get_value("How many points did you get?\n> ", 0)
    max_pts = get_value("How many points were achievable?\n> ", 1)

    score_dec = float(pts) / float(max_pts)
    score = round(score_dec, 4) * 100

    print(f"Your score was: {score}%.")

    i = 0
    while i < len(grades):
        if score > grades[i][0]:
            i += 1
        else:
            final_score = grades[i - 1][1]
            print("You will most likely be graded " + final_score + ".\n")
            break
    calc_grade()

calc_grade()
