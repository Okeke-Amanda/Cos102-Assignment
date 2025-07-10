"""
a program to compute the grade of scores
70-100=A
60-69=B
50-59=C
45-49=D
40-44=E
0-39=F

A pseudocode:
step1: algorithm start.
step2: enter the student_score.
step3: if student_score is greater than or equal to 70, then set grade to A.
step4: else if student_score is greater than or equal to 60 and is less than  
           or equal to 69, then set grade to B.
step5: else if student_score is greater than or equal to 50 and less than or 
           equal to 59, then set grade to C.
step6: else if student_score is greater than or equal to 45 and less than or 
           equal to 49, then set grade to D.
step7: else if student_score is greater than or equal to 40 and less than or 
           equal to 44, then set grade to E.
step8: else, set grade to F.
step9: algorithm end.
"""

student_score=int(input("what is your score?"))
if student_score>=70:
          print("A")
elif student_score>=60 and student_score<=69:
          print("B")
elif student_score>=50 and student_score<=59:
          print("C")
elif student_score>=45 and student_score<=49:
          print("D")
elif student_score>=40 and student_score<=44:
          print("E")
else:
          print("F")