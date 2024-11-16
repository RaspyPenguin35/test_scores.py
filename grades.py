import random
grades=[random.randint(0,100)for i in range(20)]
print (grades)
low_grades=[]
mid_grades=[]
high_grades=[]
for i in grades:
    if i<=30:
        low_grades.append(i)
    elif 31<=i<=79:
        mid_grades.append(i)
    else:
         high_grades.append(i)
print ("Test Scores",grades)
print ("Lowest Scores (Fail)",low_grades)
print ("Average Scores (Pass)",mid_grades)
print ("Highest Scores (Pass)",high_grades)