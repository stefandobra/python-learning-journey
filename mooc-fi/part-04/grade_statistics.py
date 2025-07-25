# def user_input():

#     list = []
    
#     while True:
#         points = input("Exam points and exercises completed: ")

#         if points == "":
#             break
#         list.append(points)
#     return list

# def separate(list: list):
#     exam_points = []
#     exercises_completed = []
#     for points in  list:
#         exam_points.append(int(points.split()[0]))
#         exercises_completed.append(int(points.split()[1]))

#     return exam_points , exercises_completed

# def convert_to_points(exercises_completed: list):
#     exercises_points = []

#     for point in exercises_completed:
#         exercises_points.append(point // 10)

#     return exercises_points

# def grade(exam_points: list, exercises_points: list):
#     grades= []

#     for i in range(len(exam_points)):
#         grades.append(exam_points[i] + exercises_points[i])

#     return grades

# def passed(exam_points: list, grades: list):
#     passed = 0
#     for i in range(len(exam_points)):
#         if exam_points[i] > 9 and grades[i] > 14:
#             passed += 1
#     return passed

# def grade_distribution(exam_points: list, grades: list):
#     fail = 0 
#     first = 0 
#     second = 0 
#     third = 0 
#     fourth = 0 
#     fifth = 0

#     for i in range(len(exam_points)):
#         if exam_points[i] < 10 or grades[i] < 15:
#             fail += 1
#         elif grades[i] < 18:
#             first += 1
#         elif grades[i] < 21:
#             second += 1
#         elif grades[i] < 24:
#             third += 1
#         elif grades[i] < 28:
#             fourth += 1
#         else:
#             fifth += 1

#     print("Grade distribution:")
#     print(f"  5: {'*' * fifth}")
#     print(f"  4: {'*' * fourth}")
#     print(f"  3: {'*' * third}")
#     print(f"  2: {'*' * second}")
#     print(f"  1: {'*' * first}")
#     print(f"  0: {'*' * fail}")

    

# def statistics(grades: list, exam_points: list):
#     print("Statistics:")
#     average = sum(grades) / len(grades)
#     print(f"Points average: {average:.1f}")

#     pass_percentage = passed(exam_points, grades) / len(grades) * 100

#     print(f"Pass percentage: {pass_percentage:.1f}")


# def main():
#     print(user_input())
#     print()
#     exam_points, exercises_completed = separate(user_input())

#     exercises_points = convert_to_points(exercises_completed)

#     print(f"Exam points : {exam_points}")
#     print()
#     print(f"Exercises completed: {exercises_completed}")
#     print(f"Exercises points: {exercises_points}")
#     print()

#     grades = grade(exam_points, exercises_points)
#     print(f"Grades: {grades}")
#     print()

#     statistics(grades, exam_points)

#     grade_distribution(exam_points, grades)




# #main()

# exam_points, exercises_completed = separate(user_input())

# exercises_points = convert_to_points(exercises_completed)

# grades = grade(exam_points, exercises_points)

# statistics(grades, exam_points)

# grade_distribution(exam_points, grades)


def exam_and_exercise_completed(inpt):
    separator = inpt.find(" ")
    exam = int(inpt[:separator])
    exercise = int(inpt[separator+1:])
    return [exam, exercise]

def exercise_points(amount):
    return amount // 10

def grade(points):
    boundry = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if points >= boundry[i]:
            return i

def mean(points):
    return sum(points) / len(points)
 
 
def main():

    points = []
    grades = [0] * 6

    while True:
        inpt = input("Exam points and exercises completed: ")
        if len(inpt) == 0:
            break

        exam_and_exercises = exam_and_exercise_completed(inpt)
        exercises_points = exercise_points(exam_and_exercises[1])
        total_points = exam_and_exercises[0] + exercises_points

        points.append(total_points)

        grd = grade(total_points)

        if exam_and_exercises[0] < 10:
            grd = 0
        grades[grd] += 1

    pass_percentage = (len(points) - grades[0]) / len(points) * 100

    print("Statistics:")
    print(f"Points average: {mean(points):.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        stars = "*" * grades[i]
        print(f"  {i}: {stars}")
 
main()



 


