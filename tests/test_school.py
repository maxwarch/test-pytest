import pytest


def test_add_course(course_factory, student_factory):
    course = course_factory(101, "math")
    student = student_factory(1, "Maxime")

    course.add_student(student)

    assert course.student_count() == 1
    assert student in course.students


def test_add_physics(course_factory, student_factory):
    course = course_factory(102, "physic")
    student1 = student_factory(1, "Maxime")
    student2 = student_factory(2, "Elie")
    students = [student1, student2]

    for student in students:
        course.add_student(student)

    assert course.student_count() == 2

    for student in students:
        assert student in course.students
