from faker import Factory

from exercises_app.models import Student, SchoolSubject as Subject, SCHOOL_CLASS


def create_name():
    fake = Factory.create("en_US")
    first_name = fake.first_name()
    last_name = fake.last_name()
    return first_name, last_name


def create_students():
    for school_class_key, _ in SCHOOL_CLASS:
        for kid in range(0, 20):
            first_name, last_name = create_name()
            Student.objects.create(first_name=first_name,
                                   last_name=last_name,
                                   school_class=school_class_key)


def create_subjects():
    Subject.objects.create(name="English", teacher_name=" ".join(create_name()))
    Subject.objects.create(name="Basic Math", teacher_name=" ".join(create_name()))
    Subject.objects.create(name="French", teacher_name=" ".join(create_name()))
    Subject.objects.create(name="Physical Science", teacher_name=" ".join(create_name()))
    Subject.objects.create(name="Physical Education", teacher_name=" ".join(create_name()))
    Subject.objects.create(name="Woodshop", teacher_name=" ".join(create_name()))
    Subject.objects.create(name="Biology", teacher_name=" ".join(create_name()))
    Subject.objects.create(name="Chemistry", teacher_name=" ".join(create_name()))
    Subject.objects.create(name="Geography", teacher_name=" ".join(create_name()))

