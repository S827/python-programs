print("Welcome to the GPA calculator.")
print("Please enter your letter grades, one per line.")
print("Enter a blank line to designate the end.")

# map from letter grade to point value
points = {'A+':4.0, 'A':4.0, 'A-':3.67, 'B+':3.33, 'B':3.0, 'B-':2.67, 'C+':2.33, 'C':2.0, 'D+':1.33, 'D':1.0, 'F':0.0}

num_course = 0
total_points = 0
done = False

while not done:
    grade = input()       # read input from user
    if grade == '':       # empty line was entered
        done = True
    elif grade not in points:   # unrecognized grade entered
        print("Uknown grade {} being ignored".format(grade))
    else:
        num_course += 1
        total_points += points[grade]

if num_course > 0:         # avoid division by zero
    print("Your GPA is {0:.3}".format(total_points / num_course))
