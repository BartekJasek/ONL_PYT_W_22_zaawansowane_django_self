from random import randint

from django.core.management.base import BaseCommand

from exercises_app.models import Student, GRADES, StudentGrades, SchoolSubject


class Command(BaseCommand):
    help = 'Populates school with student grades for each subject.'

    def handle(self, *args, **options):
        students = Student.objects.all()  # Pobranie wszystkich uczniów
        school_subjects = SchoolSubject.objects.all()  # Pobranie wszystkich przedmiotów
        student_grades = []

        for student in students:  # Dla każdego ucznia
            for school_subject in school_subjects:  # I każdego przedmiotu
                number_of_grades = randint(3, 10)  # losujemy ile ocen będzie mieć uczeń z danego przedmiotu


                for _ in range(number_of_grades):  # Losujemy n-razy
                    random_index = randint(0, len(GRADES) - 1)  # Wybieramy losowy index
                    grade = GRADES[random_index]
                    # zapisujemy do bazy ocenę dla ucznia z przedmiotu
                    student_grades.append(StudentGrades(student=student, school_subject=school_subject, grade=grade[0]))

        StudentGrades.objects.bulk_create(student_grades)