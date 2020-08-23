# This program is only intended to give an approximate and does not necessarily represent the teacher's grading.

grades_full = [
            [1, 21.67, "1"],
            [21.67, 23.33, "1+"],
            [23.33, 25, "1/2"],
            [25, 27.67, "2/1"],
            [27.67, 28.33, "2-"],
            [28.33, 38.33, "2"],
            [38.33, 40, "2+"],
            [40, 41.67, "2/3"],
            [41.67, 43.33, "3/2"],
            [43.33, 45, "3-"],
            [45, 55, "3"],
            [55, 56.67, "3+"],
            [56.67, 58.33, "3/4"],
            [58.33, 60, "4/3"],
            [60, 61.67, "4-"],
            [61.67, 71.67, "4"],
            [71.67, 73.33, "4+"],
            [73.33, 75, "4/5"],
            [75, 76.67, "5/4"],
            [76.67, 78.33, "5-"],
            [78.33, 88.33, "5"],
            [88.33, 90, "5+"],
            [90, 91.67, "5/6"],
            [91.67, 93.33, "6/5"],
            [93.33, 95, "6-"],
            [95, 100, "6"]
]

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

def calc_grade():
    final_grade = "NaN"

    print("How many points did you get?")
    pts = input('> ')

    print("How many points were achievable?")
    max_pts = input('> ')

    score_dec = float(pts) / float(max_pts)
    score = round(score_dec, 4) * 100

    print(f"Your score was: {score}%.")

    i = 0
    while i < len(grades):
        if score > grades[i][0]:
            i += 1
        else:
            final_score = grades[i - 1][1]
            print("You will most likely be graded " + final_score + ".\n\n")
            break
    calc_grade()

calc_grade()
