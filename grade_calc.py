# This program is only intended to give an approximate and does not necessarily represent the teacher's grading.

grades = [
    [1, "1"],
    [21.67, "1+"],
    [23.33, "1/2"],
    [25, "2/1"],
    [27.67, "2-"],
    [28.33, "2"],
    [38.33, "2+"],
    [40, "2/3"],
    [41.67, "3/2"],
    [43.33, "3-"],
    [45, "3"],
    [55, "3+"],
    [56.67, "3/4"],
    [58.33, "4/3"],
    [60, "4-"],
    [61.67, "4"],
    [71.67, "4+"],
    [73.33, "4/5"],
    [75, "5/4"],
    [76.67, "5-"],
    [78.33, "5"],
    [88.33, "5+"],
    [90, "5/6"],
    [91.67, "6/5"],
    [93.33, "6-"],
    [95, "6"],
    [100, "NO GRADE"]
]
def get_value(message):
    while True:
        user_input = input(message)
        try:
            val = int(user_input)
            if val >= 0:
                break
            else:
                print("Points can't be negative, try again")
        except ValueError:
            print("Not an integer! Try again.")
    return val

def calc_grade():
    pts = get_value("How many points did you get?\n> ")
    max_pts = get_value("How many points were achievable?\n> ")

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
