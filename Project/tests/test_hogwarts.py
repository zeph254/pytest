import pytest
from source.school import Classroom, Teacher, Student 

# 🏰 Fixture to create a Hogwarts-style classroom
@pytest.fixture
def hogwarts_classroom():
    teacher = Teacher("Severus Snape")  # Potions Master 🧪
    students = [
        Student("Harry Potter"),
        Student("Hermione Granger"),
        Student("Ron Weasley"),
        Student("Draco Malfoy"),
    ]
    return Classroom(teacher, students, "Defense Against the Dark Arts")

# ⚡ Test adding students (up to the limit)
@pytest.mark.parametrize("new_student_name", ["Neville Longbottom", "Luna Lovegood"])
def test_add_student(hogwarts_classroom, new_student_name):
    new_student = Student(new_student_name)
    hogwarts_classroom.add_student(new_student)
    assert new_student in hogwarts_classroom.students

# 🚨 Test adding too many students
def test_classroom_full():
    teacher = Teacher("Minerva McGonagall")  # Transfiguration Professor ✨
    students = [Student(f"Student {i}") for i in range(10)]
    classroom = Classroom(teacher, students, "Transfiguration")

    with pytest.raises(ValueError, match="Classroom is full"):
        classroom.add_student(Student("Tom Riddle"))

# 🔥 Test removing a student
def test_remove_student(hogwarts_classroom):
    hogwarts_classroom.remove_student("Draco Malfoy")
    assert all(student.name != "Draco Malfoy" for student in hogwarts_classroom.students)

# 🎭 Test changing the teacher
def test_change_teacher(hogwarts_classroom):
    new_teacher = Teacher("Albus Dumbledore")
    hogwarts_classroom.change_teacher(new_teacher)
    assert hogwarts_classroom.teacher == new_teacher
