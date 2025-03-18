import unittest
import time
from checkmygrade_app import Student, StudentLinkedList, Course, Professor, Grades, LoginUser

class TestCheckMyGradeApp(unittest.TestCase):

    def setUp(self):
        self.student_list = StudentLinkedList()
        self.courses = []
        self.professors = []
        self.grades = []
        self.logins = []

    def test_student_addition(self):
        student = Student("sri", "nidhi", "srinidhi@sjsu.edu", "DATA200", "A", "95")
        self.student_list.add_new_student(student)
        self.assertIsNotNone(self.student_list.search_student("srinidhi@sjsu.edu"))

    def test_student_deletion(self):
        student = Student("sharan", "patil", "sharan@sjsu.edu", "DATA201", "B", "85")
        self.student_list.add_new_student(student)
        self.assertTrue(self.student_list.delete_new_student("sharan@sjsu.edu"))
        self.assertIsNone(self.student_list.search_student("sharan@sjsu.edu"))

    def test_student_modification(self):
        student = Student("Alice", "Johnson", "alice@sjsu.edu", "DATA203", "C", "75")
        self.student_list.add_new_student(student)
        updated_student = Student("Alice", "Johnson", "alice@sjsu.edu", "DATA203", "B", "85")
        self.assertTrue(self.student_list.update_student("alice@sjsu.edu", updated_student))
        found_student = self.student_list.search_student("alice@sjsu.edu")
        self.assertEqual(found_student.grade, "B")
        self.assertEqual(found_student.marks, 85.0)

    def test_large_dataset_search(self):
        for i in range(1000):
            student = Student(f"first_n{i}", f"last_n{i}", f"student{i}@sjsu.edu", f"DATA{i}", "A", "90")
            self.student_list.add_new_student(student)
        
        start_time = time.time()
        found_student = self.student_list.search_student("student500@sjsu.edu")
        end_time = time.time()
        
        self.assertIsNotNone(found_student)
        self.assertLess(end_time - start_time, 1.0)  

    def test_sorting_by_name(self):
        students = [
            Student("sri", "nidhi", "srinidhi@sjsu.edu", "DATA200", "A", "95"),
            Student("sharan", "patil", "sharan@sjsu.edu", "DATA201", "B", "85"),
            Student("Alice", "Johnson", "alice@sjsu.edu", "DATA203", "C", "75")
        ]
        for student in students:
            self.student_list.add_new_student(student)
        
        sorted_students = self.student_list.to_list()
        sorted_students.sort(key=lambda s: (s.lastName.lower(), s.firstName.lower()))
        
        self.assertEqual(sorted_students[0].firstName, "Alice")
        self.assertEqual(sorted_students[1].firstName, "sri")
        self.assertEqual(sorted_students[2].firstName, "sharan")

    def test_sorting_by_marks(self):
        students = [
            Student("sri", "nidhi", "srinidhi@sjsu.edu", "DATA200", "A", "95"),
            Student("sharan", "patil", "sharan@sjsu.edu", "DATA201", "B", "85"),
            Student("Alice", "Johnson", "alice@sjsu.edu", "DATA203", "C", "75")
        ]
        for student in students:
            self.student_list.add_new_student(student)
        
        sorted_students = self.student_list.to_list()
        sorted_students.sort(key=lambda s: s.marks, reverse=True)
        
        self.assertEqual(sorted_students[0].firstName, "sri")
        self.assertEqual(sorted_students[1].firstName, "sharan")
        self.assertEqual(sorted_students[2].firstName, "Alice")

    def test_course_operations(self):
        course = Course("DATA200", "3", "Introduction to Python Programming")
        self.courses.append(course)
        self.assertEqual(len(self.courses), 1)
        
        course.delete_new_course(self.courses)
        self.assertEqual(len(self.courses), 0)

    def test_professor_operations(self):
        professor = Professor("Param", "param@sjsu.edu", "Associate Professor", "DATA200")
        self.professors.append(professor)
        self.assertEqual(len(self.professors), 1)
        
        professor.modify_professor_details(rank="Full Professor")
        self.assertEqual(self.professors[0].rank, "Full Professor")

    def test_grade_operations(self):
        grade = Grades("G1", "A", "90-100")
        self.grades.append(grade)
        self.assertEqual(len(self.grades), 1)
        
        grade.modify_grade(marks_range="91-100")
        self.assertEqual(self.grades[0].marks_range, "91-100")

    def test_login_user(self):
        user = LoginUser("user@sjsu.edu", "password123", "student")
        self.logins.append(user)
        
        self.assertTrue(user.login("user@sjsu.edu", "password123"))
        self.assertFalse(user.login("user@sjsu.edu", "wrongpassword"))

if __name__ == '__main__':
    unittest.main()
