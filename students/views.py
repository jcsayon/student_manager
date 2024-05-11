from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from .forms import FilterForm

def student_list(request):
    query = request.GET.get('search', '')
    students = Student.objects.filter(first_name__icontains=query) | Student.objects.filter(last_name__icontains=query)
    return render(request, 'students/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})



def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit_student.html', {'form': form, 'student': student})


def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('/')


def student_list(request):
    form = FilterForm(request.GET or None)
    students = Student.objects.all()
    if form.is_valid():
        full_name = form.cleaned_data.get('full_name')
        course = form.cleaned_data.get('course')
        gender = form.cleaned_data.get('gender')
        age_min = form.cleaned_data.get('age_min')
        age_max = form.cleaned_data.get('age_max')

        if full_name:
            students = students.filter(first_name__icontains=full_name) | students.filter(last_name__icontains=full_name)
        if course:
            students = students.filter(course=course)
        if gender:
            students = students.filter(gender=gender)
        if age_min is not None:
            students = students.filter(age__gte=age_min)
        if age_max is not None:
            students = students.filter(age__lte=age_max)

    return render(request, 'students/student_list.html', {'form': form, 'students': students})