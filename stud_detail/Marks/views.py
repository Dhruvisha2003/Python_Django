from django.shortcuts import render

# Create your views here.
#create student form that have their name and marks of 5 subject then print total per minimum marks and grade

def input(request):
    if request.method == "POST" :
        name = request.POST['name']
        marks1 = request.POST['marks1']
        marks2 = request.POST['marks2']
        marks3 = request.POST['marks3']
        marks4 = request.POST['marks4']
        marks5 = request.POST['marks5']
        total = int(marks1) + int(marks2) + int(marks3) + int(marks4) + int(marks5)
        per = (total/5)*100
        if per >= 90 :
            grade = 'A'
        elif per >= 80 :
            grade = 'B'
        elif per >= 70 :
            grade = 'C'
        elif per >= 60 :
            grade = 'D'
        else:
            grade = 'F'
        if marks1 < marks2 :
            if marks1 < marks3:
                if marks1 < marks4:
                    if marks1 < marks5:
                        min_marks = marks1
                    else:
                        min_marks = marks5
                else:
                    if marks4 < marks5:
                        min_marks = marks4
                    else:
                        min_marks = marks5
            else:
                if marks3 < marks4:
                    if marks3 < marks5:
                        min_marks = marks3
                    else:
                        min_marks = marks5
                else:
                    if marks4 < marks5:
                        min_marks = marks4
                    else:
                        min_marks = marks5
        else:
            if marks2 < marks3:
                if marks2 < marks4:
                    if marks2 < marks5:
                        min_marks = marks2
                    else:
                        min_marks = marks5
                else:
                    if marks4 < marks5:
                        min_marks = marks4
                    else:
                        min_marks = marks5
            else:
                if marks3 < marks4:
                    if marks3 < marks5:
                        min_marks = marks3
                    else:
                        min_marks = marks5
                else:
                    if marks4 < marks5:
                        min_marks = marks4
                    else:
                        min_marks = marks5
                        
