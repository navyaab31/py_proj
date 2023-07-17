# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
#  Print the average of the marks array for the student name provided, showing 2 places after the decimal.
n=int(input())
std={}
for i in range(n):
    name = input("enter name: ")
    marks = list(map(float, input("enter the score: ").split()))
    std[name]=marks
# print(name)
# print(marks)
# print(std)
std_name=input("enter the student name: ")
for i in std:
    if i==std_name:
        score_list=[j for j in std[i]]
        # avg_score=0
        for i in score_list:
            avg_score = sum(score_list)/len(score_list)
        print(format(avg_score,".2f"))
            
