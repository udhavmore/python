def getNextMultiple(num, multiple):
    mod = num % multiple
    roundup = num - mod
    if mod > 0:
        roundup += 5
    return roundup
    

def gradingStudents(grades):
    # Write your code here
    final_grades = []
    for grade in grades:
        if grade < 38:
            print(f"grade less than 38: {grade}")
            final_grades.append(grade)
            continue
    
        rounded_grade = getNextMultiple(grade, 5)
        print(f"rounded_grade: {rounded_grade}")
        if rounded_grade - grade < 3:
            final_grades.append(rounded_grade)
        else:
            final_grades.append(grade)
        
    return final_grades

grades = [73,67,40,33]

print(gradingStudents(grades))