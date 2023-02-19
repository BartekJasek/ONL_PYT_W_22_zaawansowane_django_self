from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import StudentSearchForm, StudentForm, PizzaToppingsForm
from .models import SCHOOL_CLASS, Student, SchoolSubject, StudentGrades, Pizza


class SchoolView(View):
    def get(self, request):
        html = """<!doctype html>
        <html>
            <head><meta charset="utf-8"></head>
            <body>
                <h1>Szkoła podstawowa nr 1 im. Chucka Norrisa.</h1>
                <h2>Klasy:</h2>
                <ul>
                    {}
                </ul>
            </body>
        </html>
        """
        class_list = []
        for school_class in SCHOOL_CLASS:
            class_list.append("<li><a href='/class/{}'>{}</a></li>".format(school_class[0], school_class[1]))
        classes_part = "".join(class_list)
        return HttpResponse(html.format(classes_part))


class SchoolClassView(View):
    def get(self, request, school_class):
        students = Student.objects.filter(school_class=school_class).order_by('last_name')
        return render(request, "class.html", {"students": students,
                                              "class_name": SCHOOL_CLASS[int(school_class) - 1][1]})


def my_view(request):
    context = {'main_page': 'Nagłówek H1'}
    return render(request, 'my_view.html', context)


class StudentView(View):
    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        subjects = SchoolSubject.objects.all()
        return render(request, "studentview.html", {"student": student,
                                                    "subjects": subjects})


class StudentGradeView(View):
    def get(self, request, student_id, subject_id):
        student = get_object_or_404(Student, id=student_id)
        subject = get_object_or_404(SchoolSubject, id=subject_id)
        grades = StudentGrades.objects.filter(student=student_id, school_subject=subject_id)

        average_grade = round(sum(grade.grade for grade in grades) / len(grades), 2)

        return render(request, "gradesview.html", {"student": student,
                                                   "subject": subject,
                                                   "grades": grades,
                                                   "average": average_grade})


class StudentSearchView(View):
    def get(self, request):
        search_form = StudentSearchForm()
        context = {'search_form': search_form}
        return render(request, 'student_search.html', context)

    def post(self, request):
        search_form = StudentSearchForm(request.POST)
        if search_form.is_valid():
            last_name = search_form.cleaned_data['last_name']
            students = Student.objects.filter(last_name__icontains=last_name)
            context = {"students": students, 'search_form': search_form, 'students': 'empty'}
            return render(request, 'student_search.html', context)
        else:
            context = {'search_form': search_form, 'students': 'empty'}
            return render(request, 'student_search.html', context)


class CreateStudentView(View):
    def get(self, request):
        create_form = StudentForm()
        context = {'create_form': create_form}
        return render(request, 'student_create.html', context)

    def post(self, request):
        create_form = StudentForm(request.POST)
        if create_form.is_valid():
            first_name = create_form.cleaned_data['first_name']
            last_name = create_form.cleaned_data['last_name']
            school_class = create_form.cleaned_data['school_class']
            year_of_birth = create_form.cleaned_data['year_of_birth']
            student = Student.objects.create(
                last_name=last_name, first_name=first_name, school_class=school_class, year_of_birth=year_of_birth)
            return redirect('student-view', student_id=student.id)


class PizzaToppingsView(View):
    def get(self, request):
        form = PizzaToppingsForm()
        context = {'form': form}
        return render(request, 'pizza_toppings.html', context)

    def post(self, request):
        form = PizzaToppingsForm(request.POST)
        if form.is_valid():
            size = form.cleaned_data['size']
            toppings = form.cleaned_data['toppings']
            pizza = Pizza.objects.create(size=size)
            pizza.toppings.set(toppings)
            context = {'form': PizzaToppingsForm()}
            return render(request, 'pizza_toppings.html', context)