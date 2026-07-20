#start
number_of_classes = int(input('how many classes?'))
while number_of_classes > 0:
    number_of_classes -= 1
    number_of_students = 0
    grade = 0
    sum_grades = 0

    while True:
        grade = int(input('grade [999 to exit]: '))
        if grade == 999:
            break

        if grade < 0 or grade > 100:
            print('invalid grade')
            continue

        sum_grades += grade
        number_of_students += 1

    if number_of_students == 0:
        print('no students')
    else:
        avg = sum_grades / number_of_students
        print('class number:')
        print('average grade of class ...', avg)


#stop