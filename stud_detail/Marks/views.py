from django.shortcuts import *
from Marks.models import stud

# Create your views here.


def input(request):
    if request.method == "POST" :
            name = request.POST['name']
            marks1 = request.POST['marks1']
            marks2 = request.POST['marks2']
            marks3 = request.POST['marks3']
            marks4 = request.POST['marks4']
            marks5 = request.POST['marks5']
            total = int(marks1) + int(marks2) +int (marks3) + int(marks4) + int(marks5)
            percentage = (total/500)*100
            if percentage >= 90 :
                grade = 'A' 
            elif percentage >= 80 :
                grade = 'B'
            elif percentage >= 70 :
                grade = 'C'
            elif percentage >= 60 :
                grade = 'D'
            else:
                grade = 'F'
            
            min_marks = min(marks1, marks2, marks3, marks4, marks5)
    
            data = stud(name=name,marks1=marks1,marks2=marks2,marks3=marks3,marks4=marks4,marks5=marks5,total=total,percentage=percentage,     grade=grade,min_marks=min_marks)
            data.save()
            return redirect('data_table')
       
    return render(request,'home.html')                


def output(request):
    data  = stud.objects.all()
    return render(request, 'show.html',{'data':data})

def deldata(request,id):
    data = stud.objects.get(id=id)
    data.delete()
    return redirect('data_table')

def update(request,id):
    data = stud.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        marks1 = request.POST['marks1']
        marks2 = request.POST['marks2']
        marks3 = request.POST['marks3']
        marks4 = request.POST['marks4']
        marks5 = request.POST['marks5']
        total = int(marks1) + int(marks2) +int (marks3) + int(marks4) + int(marks5)
        percentage = (total/500)*100
        if percentage >= 90 :
            grade = 'A'
        elif percentage >= 80 :
            grade = 'B'
        elif percentage >= 70 :
            grade = 'C'
        elif percentage >= 60 :
            grade = 'D'
        else:
            grade = 'F'
        
        min_marks = min(marks1, marks2, marks3, marks4, marks5)

        data.name = name
        data.marks1 = marks1
        data.marks2 = marks2
        data.marks3 = marks3
        data.marks4 = marks4
        data.marks5 = marks5
        data.total = total
        data.percentage = percentage
        data.grade = grade
        data.min_marks = min_marks
        data.save()
        return redirect('data_table')
    return render(request,'update.html',{"data":data})
