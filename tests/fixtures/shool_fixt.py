import pytest

from source.school import Student, Course


@pytest.fixture
def student_factory():
    def create_student(student_id, name):
        return Student(student_id, name)

    return create_student


@pytest.fixture
def course_factory():
    def create_course(course_id, title):
        return Course(course_id, title)

    return create_course
