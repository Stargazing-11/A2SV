def gradingStudents(grades):
    for i in range(len(grades)):
        count=0
        if grades[i] < 38:
            continue
        while(grades[i]%5!=0):
            grades[i]+=1
            count +=1
        if count < 3:
            grades[i] = grades[i]
        else:
            grades[i]-=count
    return grades

