student = input("Enter sudent's name: ")
score = input("Enter student's score: ")

if int(score) >= 0 and int(score) <=50:
    print("%s's grade is 'Слаб 2'" % student)
elif int(score) >=51 and int(score) <=60:
    print("%s's grade is 'Среден 3'" % student)
elif int(score) >=61 and int(score) <=70:
    print("%s's grade is 'Добър 4'" % student)
elif int(score) >=71 and int(score) <=80:
    print("%s's grade is 'Много добър 5'" % student)
else:
    if int(score) == 100:
        print("%s's grade is 'Много отличен 6'" % student)
    else:
        print("%s's grade is 'Отличен 6'")
