students = ["Rado", "Ivo", "Maria", "Nina"]
grades = [3, 4.5, 5.5, 6]



def grades_that_pass(students, grades, limit):
    passed = []
    for i in range (0, len(grades)):
        if grades[i] >= limit:
            passed = passed + [students[i]]
    return passed
    
            
     

result = grades_that_pass(students, grades, 5.0)
print (result)
