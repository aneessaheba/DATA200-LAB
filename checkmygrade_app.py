import sys
import csv
import time

class Student:
    def __init__(self, firstName, lastName, email_address, course_id, grade, marks):
        self.firstName = firstName.strip()
        self.lastName = lastName.strip()
        self.email_address = email_address.strip()
        self.course_id = course_id.strip()
        self.grade = grade.strip()
        self.marks = float(marks) if marks else 0.0

    def display_records(self):
        print(f"{self.firstName} {self.lastName} ({self.email_address}) | Course: {self.course_id} | Grade: {self.grade} | Marks: {self.marks}")

    def check_my_grades(self):
        print(f"{self.firstName} {self.lastName}'s Grade: {self.grade}")

    def check_my_marks(self):
        print(f"{self.firstName} {self.lastName}'s Marks: {self.marks}")

    def update_student_record(self, firstName=None, lastName=None, email_address=None, course_id=None, grade=None, marks=None):
        if firstName:
            self.firstName = firstName.strip()
        if lastName:
            self.lastName = lastName.strip()
        if email_address:
            self.email_address = email_address.strip()
        if course_id:
            self.course_id = course_id.strip()
        if grade:
            self.grade = grade.strip()
        if marks:
            self.marks = float(marks)
        print("Student record updated.")

class StudentNode:
    def __init__(self, student):
        self.student = student
        self.next = None

class StudentLinkedList:
    def __init__(self):
        self.head = None

    def add_new_student(self, student):
        new_node = StudentNode(student)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Student {student.firstName} {student.lastName} added.")

    def delete_new_student(self, email):
        current = self.head
        previous = None
        email = email.strip().lower()
        while current:
            if current.student.email_address.lower() == email:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                print("Student deleted.")
                return True
            previous = current
            current = current.next
        print("Student not found.")
        return False

    def update_student(self, old_email, updated_student):
        current = self.head
        old_email = old_email.strip().lower()
        while current:
            if current.student.email_address.lower() == old_email:
                current.student = updated_student
                print("Student record updated.")
                return True
            current = current.next
        print("Student not found.")
        return False

    def search_student(self, email):
        email = email.strip().lower()
        current = self.head
        start_time = time.time()
        while current:
            if current.student.email_address.lower() == email:
                elapsed = time.time() - start_time
                print(f"Search completed in {elapsed:.6f} seconds.")
                return current.student
            current = current.next
        elapsed = time.time() - start_time
        print(f"Student not found. Search completed in {elapsed:.6f} seconds.")
        return None

    def display_all_students(self):
        if not self.head:
            print("No student records available.")
            return
        current = self.head
        while current:
            current.student.display_records()
            current = current.next

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.student)
            current = current.next
        return result

    def display_sorted_by_name(self):
        students_list = self.to_list()
        start_time = time.time()
        students_list.sort(key=lambda s: (s.lastName.lower(), s.firstName.lower()))
        elapsed = time.time() - start_time
        print(f"\n--- Students Sorted by Name (Last, First). Sorting took {elapsed:.6f} seconds ---")
        for student in students_list:
            student.display_records()

    def display_sorted_by_marks_desc(self):
        students_list = self.to_list()
        start_time = time.time()
        students_list.sort(key=lambda s: s.marks, reverse=True)
        elapsed = time.time() - start_time
        print(f"\n--- Students Sorted by Marks (High to Low). Sorting took {elapsed:.6f} seconds ---")
        for student in students_list:
            student.display_records()

    def average_marks(self, course_id=None):
        students_list = self.to_list()
        if course_id:
            students_list = [s for s in students_list if s.course_id.lower() == course_id.lower()]
        if not students_list:
            print("No students found (or no matching course) to compute average.")
            return
        total = sum(s.marks for s in students_list)
        avg = total / len(students_list)
        if course_id:
            print(f"Average marks for course '{course_id}': {avg:.2f}")
        else:
            print(f"Average marks (All Courses): {avg:.2f}")

    def median_marks(self, course_id=None):
        students_list = self.to_list()
        if course_id:
            students_list = [s for s in students_list if s.course_id.lower() == course_id.lower()]
        if not students_list:
            print("No students found (or no matching course) to compute median.")
            return
        sorted_marks = sorted(s.marks for s in students_list)
        n = len(sorted_marks)
        mid = n // 2
        if n % 2 == 1:
            median_val = sorted_marks[mid]
        else:
            median_val = (sorted_marks[mid - 1] + sorted_marks[mid]) / 2
        if course_id:
            print(f"Median marks for course '{course_id}': {median_val:.2f}")
        else:
            print(f"Median marks (All Courses): {median_val:.2f}")

class Grades:
    def __init__(self, grade_id, grade, marks_range):
        self.grade_id = grade_id.strip()
        self.grade = grade.strip()
        self.marks_range = marks_range.strip()

    def display_grade_report(self):
        print(f"Grade ID: {self.grade_id} | Grade: {self.grade} | Marks Range: {self.marks_range}")

    def add_grade(self, grades_list):
        grades_list.append(self)
        print(f"Grade {self.grade_id} added.")

    def delete_grade(self, grades_list):
        if self in grades_list:
            grades_list.remove(self)
            print(f"Grade {self.grade_id} deleted.")
        else:
            print("Grade not found.")

    def modify_grade(self, grade_id=None, grade=None, marks_range=None):
        if grade_id:
            self.grade_id = grade_id.strip()
        if grade:
            self.grade = grade.strip()
        if marks_range:
            self.marks_range = marks_range.strip()
        print(f"Grade {self.grade_id} modified.")

class Course:
    def __init__(self, course_id, credits, course_name):
        self.course_id = course_id.strip()
        self.credits = credits.strip()
        self.course_name = course_name.strip()

    def display_courses(self):
        print(f"Course ID: {self.course_id} | Credits: {self.credits} | Course Name: {self.course_name}")

    def add_new_course(self, course_list):
        course_list.append(self)
        print(f"Course {self.course_id} added.")

    def delete_new_course(self, course_list):
        if self in course_list:
            course_list.remove(self)
            print(f"Course {self.course_id} deleted.")
        else:
            print("Course not found.")

class Professor:
    def __init__(self, name, email_address, rank, course_id):
        self.name = name.strip()
        self.email_address = email_address.strip()
        self.rank = rank.strip()
        self.course_id = course_id.strip()

    def professors_details(self):
        print(f"Professor: {self.name} | Email: {self.email_address} | Rank: {self.rank} | Course: {self.course_id}")

    def add_new_professor(self, professor_list):
        professor_list.append(self)
        print(f"Professor {self.name} added.")

    def delete_professore(self, professor_list):
        if self in professor_list:
            professor_list.remove(self)
            print(f"Professor {self.name} deleted.")
        else:
            print("Professor not found.")

    def modify_professor_details(self, name=None, email_address=None, rank=None, course_id=None):
        if name:
            self.name = name.strip()
        if email_address:
            self.email_address = email_address.strip()
        if rank:
            self.rank = rank.strip()
        if course_id:
            self.course_id = course_id.strip()
        print("Professor details modified.")

    def show_course_details_by_professor(self, course_list):
        matches = [c for c in course_list if c.course_id.lower() == self.course_id.lower()]
        if matches:
            print(f"{self.name} teaches:")
            for course in matches:
                course.display_courses()
        else:
            print("No matching course found.")

class LoginUser:
    def __init__(self, email_id, password, role):
        self.email_id = email_id.strip()
        self.password = self.encrypt_password(password)
        self.role = role.strip()

    def encrypt_password(self, plain_text):
        shift = 4
        return "".join(chr((ord(c) + shift) % 256) for c in plain_text.strip())

    def decrypt_password(self, encrypted_text):
        shift = 4
        return "".join(chr((ord(c) - shift) % 256) for c in encrypted_text)

    def login(self, email, password):
        if (self.email_id.lower() == email.strip().lower() and self.decrypt_password(self.password) == password.strip()):
            print("Login successful.")
            return True
        print("Invalid credentials.")
        return False

    def logout(self):
        print(f"{self.email_id} logged out.")

    def change_password(self, new_password):
        self.password = self.encrypt_password(new_password)
        print("Password changed successfully.")

    def display_user(self):
        print(f"Email: {self.email_id} | Encrypted Password: {self.password} | Role: {self.role}")

class CheckMyGradeApp:
    def __init__(self):
        self.students = StudentLinkedList()
        self.grades = []
        self.courses = []
        self.professors = []
        self.logins = []
        self.load_data()

    def load_data(self):
        self.load_students("Student.csv")
        self.load_courses("Course.csv")
        self.load_professors("Professor.csv")
        self.load_logins("Login.csv")
        self.load_grades("Grades.csv")

    def save_data(self):
        self.save_students("Student.csv")
        self.save_courses("Course.csv")
        self.save_professors("Professor.csv")
        self.save_logins("Login.csv")
        self.save_grades("Grades.csv")
        print("All data successfully saved.")

    def load_students(self, filename):
        try:
            with open(filename, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        row.get('firstname', ''),
                        row.get('lastname', ''),
                        row.get('email', ''),
                        row.get('courseId', ''),
                        row.get('grade', ''),
                        row.get('marks', '0')
                    )
                    self.students.add_new_student(student)
        except FileNotFoundError:
            print(f"{filename} not found. Starting with empty student list.")

    def save_students(self, filename):
        with open(filename, 'w', newline='') as file:
            fieldnames = ['email', 'firstname', 'lastname', 'courseId', 'grade', 'marks']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            current = self.students.head
            while current:
                s = current.student
                writer.writerow({
                    'email': s.email_address,
                    'firstname': s.firstName,
                    'lastname': s.lastName,
                    'courseId': s.course_id,
                    'grade': s.grade,
                    'marks': s.marks
                })
                current = current.next

    def load_courses(self, filename):
        try:
            with open(filename, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    course = Course(
                        row.get('courseId', ''),
                        row.get('Credits', ''),
                        row.get('Course_Name', '')
                    )
                    self.courses.append(course)
        except FileNotFoundError:
            print(f"{filename} not found. Starting with empty course list.")

    def save_courses(self, filename):
        with open(filename, 'w', newline='') as file:
            fieldnames = ['courseId', 'Credits', 'Course_Name']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for c in self.courses:
                writer.writerow({
                    'courseId': c.course_id,
                    'Credits': c.credits,
                    'Course_Name': c.course_name
                })

    def load_professors(self, filename):
        try:
            with open(filename, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    professor = Professor(
                        row.get('Professor_Name', ''),
                        row.get('Professor_id', ''),
                        row.get('Rank', ''),
                        row.get('courseID', '')
                    )
                    self.professors.append(professor)
        except FileNotFoundError:
            print(f"{filename} not found. Starting with empty professor list.")

    def save_professors(self, filename):
        with open(filename, 'w', newline='') as file:
            fieldnames = ['Professor_id', 'Professor_Name', 'Rank', 'courseID']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for p in self.professors:
                writer.writerow({
                    'Professor_id': p.email_address,
                    'Professor_Name': p.name,
                    'Rank': p.rank,
                    'courseID': p.course_id
                })

    def load_logins(self, filename):
        try:
            with open(filename, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    user = LoginUser(
                        row.get('User_id', ''),
                        row.get('Password', ''),
                        row.get('Role', '')
                    )
                    self.logins.append(user)
        except FileNotFoundError:
            print(f"{filename} not found. Starting with empty login list.")

    def save_logins(self, filename):
        with open(filename, 'w', newline='') as file:
            fieldnames = ['User_id', 'Password', 'Role']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for u in self.logins:
                writer.writerow({
                    'User_id': u.email_id,
                    'Password': u.password,
                    'Role': u.role
                })

    def load_grades(self, filename):
        try:
            with open(filename, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    grade = Grades(
                        row.get('grade_id', ''),
                        row.get('grade', ''),
                        row.get('marks_range', '')
                    )
                    self.grades.append(grade)
        except FileNotFoundError:
            print(f"{filename} not found. Starting with empty grades list.")

    def save_grades(self, filename):
        with open(filename, 'w', newline='') as file:
            fieldnames = ['grade_id', 'grade', 'marks_range']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for g in self.grades:
                writer.writerow({
                    'grade_id': g.grade_id,
                    'grade': g.grade,
                    'marks_range': g.marks_range
                })

    def menu(self):
        print("\n--- CheckMyGrade Main Menu ---")
        print("1. Login Operations")
        print("2. Student Operations")
        print("3. Professor Operations")
        print("4. Course Operations")
        print("5. Grades Operations")
        print("6. Reports & Stats")
        print("7. Exit")

    def run(self):
        try:
            while True:
                self.menu()
                choice = input("Enter your choice: ").strip()
                if choice == "1":
                    self.login_operations()
                elif choice == "2":
                    self.student_operations()
                elif choice == "3":
                    self.professor_operations()
                elif choice == "4":
                    self.course_operations()
                elif choice == "5":
                    self.grades_operations()
                elif choice == "6":
                    self.reports_and_stats_menu()
                elif choice == "7":
                    print("Saving data before exiting...")
                    self.save_data()
                    print("Data saved successfully. Exiting CheckMyGrade Application.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        except KeyboardInterrupt:
            print("\nDetected interruption! Saving data before exit...")
            self.save_data()
            print("Data saved successfully. Goodbye!")
            sys.exit(0)

    def login_operations_menu(self):
        print("\n--- Login Operations ---")
        print("a. Login")
        print("b. Change Password")
        print("c. Signup (New user)")
        print("d. Return to Main Menu")

    def login_operations(self):
        while True:
            self.login_operations_menu()
            ch = input("Choose an option: ").strip().lower()
            if ch == 'a':
                email = input("Email: ")
                password = input("Password: ")
                user_found = next((u for u in self.logins if u.email_id.lower() == email.lower()), None)
                if user_found:
                    user_found.login(email, password)
                else:
                    print("User not found.")
            elif ch == 'b':
                email = input("Email: ")
                user_found = next((u for u in self.logins if u.email_id.lower() == email.lower()), None)
                if user_found:
                    new_pass = input("New Password: ")
                    user_found.change_password(new_pass)
                else:
                    print("User not found.")
            elif ch == 'c':
                email = input("Email: ")
                password = input("Password: ")
                role = input("Role: ")
                new_user = LoginUser(email, password, role)
                self.logins.append(new_user)
                print("New user added.")
            elif ch == 'd':
                break
            else:
                print("Invalid option.")

    def student_operations_menu(self):
        print("\n--- Student Operations ---")
        print("a. Display All Students")
        print("b. Search Student Record")
        print("c. Add New Student")
        print("d. Delete Student")
        print("e. Update Student Record")
        print("f. Check Grades")
        print("g. Check Marks")
        print("h. Return to Main Menu")

    def student_operations(self):
        while True:
            self.student_operations_menu()
            ch = input("Choose an option: ").strip().lower()
            if ch == 'a':
                self.students.display_all_students()
            elif ch == 'b':
                email = input("Enter student's email: ")
                student = self.students.search_student(email)
                if student:
                    student.display_records()
            elif ch == 'c':
                firstName = input("Enter first name: ")
                lastName = input("Enter last name: ")
                email = input("Enter email: ")
                course_id = input("Enter course ID: ")
                grade = input("Enter grade: ")
                marks = input("Enter marks: ")
                new_student = Student(firstName, lastName, email, course_id, grade, marks)
                self.students.add_new_student(new_student)
            elif ch == 'd':
                email = input("Enter student's email to delete: ")
                self.students.delete_new_student(email)
            elif ch == 'e':
                email = input("Enter student's current email to update: ")
                student = self.students.search_student(email)
                if student:
                    print("Enter new details (leave blank to keep current)")
                    firstName = input("First name: ") or student.firstName
                    lastName = input("Last name: ") or student.lastName
                    email_new = input("Email: ") or student.email_address
                    course_id = input("Course ID: ") or student.course_id
                    grade = input("Grade: ") or student.grade
                    marks = input("Marks: ") or str(student.marks)
                    updated_student = Student(firstName, lastName, email_new, course_id, grade, marks)
                    self.students.update_student(email, updated_student)
            elif ch == 'f':
                email = input("Enter student's email to check grades: ")
                student = self.students.search_student(email)
                if student:
                    student.check_my_grades()
            elif ch == 'g':
                email = input("Enter student's email to check marks: ")
                student = self.students.search_student(email)
                if student:
                    student.check_my_marks()
            elif ch == 'h':
                break
            else:
                print("Invalid option.")

    def professor_operations_menu(self):
        print("\n--- Professor Operations ---")
        print("a. Display All Professors")
        print("b. Add New Professor")
        print("c. Delete Professor")
        print("d. Modify Professor Details")
        print("e. Show Professor's Course Details")
        print("f. Return to Main Menu")

    def professor_operations(self):
        while True:
            self.professor_operations_menu()
            ch = input("Choose an option: ").strip().lower()
            if ch == 'a':
                if not self.professors:
                    print("No professor records available.")
                else:
                    for p in self.professors:
                        p.professors_details()
            elif ch == 'b':
                name = input("Name: ")
                email = input("Email: ")
                rank = input("Rank: ")
                course_id = input("Course ID: ")
                course_match = next((c for c in self.courses if c.course_id.lower() == course_id.lower()), None)
                if course_match:
                    print(f"Found Course: {course_match.course_name} | Credits: {course_match.credits}")
                else:
                    print("Warning: Course not found in Course.csv. Please add the course first.")
                new_prof = Professor(name, email, rank, course_id)
                new_prof.add_new_professor(self.professors)
            elif ch == 'c':
                email = input("Enter professor's email to delete: ")
                prof_found = next((p for p in self.professors if p.email_address.lower() == email.lower()), None)
                if prof_found:
                    prof_found.delete_professore(self.professors)
                else:
                    print("Professor not found.")
            elif ch == 'd':
                email = input("Enter professor's email to modify: ")
                prof_found = next((p for p in self.professors if p.email_address.lower() == email.lower()), None)
                if prof_found:
                    print("Enter new details (leave blank to keep current):")
                    name = input("Name: ") or prof_found.name
                    email_new = input("Email: ") or prof_found.email_address
                    rank = input("Rank: ") or prof_found.rank
                    course_id = input("Course ID: ") or prof_found.course_id
                    prof_found.modify_professor_details(name, email_new, rank, course_id)
                else:
                    print("Professor not found.")
            elif ch == 'e':
                email = input("Enter professor's email to view course details: ")
                prof_found = next((p for p in self.professors if p.email_address.lower() == email.lower()), None)
                if prof_found:
                    prof_found.show_course_details_by_professor(self.courses)
                else:
                    print("Professor not found.")
            elif ch == 'f':
                break
            else:
                print("Invalid option.")

    def course_operations_menu(self):
        print("\n--- Course Operations ---")
        print("a. Display All Courses")
        print("b. Add New Course")
        print("c. Delete Course")
        print("d. Return to Main Menu")

    def course_operations(self):
        while True:
            self.course_operations_menu()
            ch = input("Choose an option: ").strip().lower()
            if ch == 'a':
                if not self.courses:
                    print("No course records available.")
                else:
                    for c in self.courses:
                        c.display_courses()
            elif ch == 'b':
                course_id = input("Course ID: ")
                credits = input("Credits: ")
                course_name = input("Course Name: ")
                new_course = Course(course_id, credits, course_name)
                new_course.add_new_course(self.courses)
            elif ch == 'c':
                course_id = input("Enter Course ID to delete: ")
                course_found = next((co for co in self.courses if co.course_id.lower() == course_id.lower()), None)
                if course_found:
                    course_found.delete_new_course(self.courses)
                else:
                    print("Course not found.")
            elif ch == 'd':
                break
            else:
                print("Invalid option.")

    def grades_operations_menu(self):
        print("\n--- Grades Operations ---")
        print("a. Display Grade Reports")
        print("b. Add New Grade")
        print("c. Delete Grade")
        print("d. Modify Grade")
        print("e. Return to Main Menu")

    def grades_operations(self):
        while True:
            self.grades_operations_menu()
            ch = input("Choose an option: ").strip().lower()
            if ch == 'a':
                if not self.grades:
                    print("No grade records available.")
                else:
                    for g in self.grades:
                        g.display_grade_report()
            elif ch == 'b':
                grade_id = input("Grade ID: ")
                grade_val = input("Grade (A, B, C, etc.): ")
                marks_range = input("Marks Range (e.g., 90-100): ")
                new_grade = Grades(grade_id, grade_val, marks_range)
                new_grade.add_grade(self.grades)
            elif ch == 'c':
                grade_id = input("Grade ID to delete: ")
                found = next((g for g in self.grades if g.grade_id.lower() == grade_id.lower()), None)
                if found:
                    found.delete_grade(self.grades)
                else:
                    print("Grade not found.")
            elif ch == 'd':
                grade_id = input("Grade ID to modify: ")
                found = next((g for g in self.grades if g.grade_id.lower() == grade_id.lower()), None)
                if found:
                    new_grade_id = input("New Grade ID (blank to keep current): ")
                    new_grade_val = input("New Grade (blank to keep current): ")
                    new_marks_range = input("New Marks Range (blank to keep current): ")
                    found.modify_grade(new_grade_id, new_grade_val, new_marks_range)
                else:
                    print("Grade not found.")
            elif ch == 'e':
                break
            else:
                print("Invalid option.")

    def reports_and_stats_menu(self):
        while True:
            print("\n--- Reports & Stats Menu ---")
            print("a. Sort Students by Name")
            print("b. Sort Students by Marks (Descending)")
            print("c. Average Marks (All or by Course)")
            print("d. Median Marks (All or by Course)")
            print("e. Course-wise Report (Which students?)")
            print("f. Professor-wise Report (Which students?)")
            print("g. Student-wise Report (All courses/grades?)")
            print("h. Return to Main Menu")
            choice = input("Choose an option: ").strip().lower()
            if choice == 'a':
                self.students.display_sorted_by_name()
            elif choice == 'b':
                self.students.display_sorted_by_marks_desc()
            elif choice == 'c':
                c_id = input("Enter course ID (or leave blank for ALL): ").strip()
                if c_id == "":
                    self.students.average_marks()
                else:
                    self.students.average_marks(c_id)
            elif choice == 'd':
                c_id = input("Enter course ID (or leave blank for ALL): ").strip()
                if c_id == "":
                    self.students.median_marks()
                else:
                    self.students.median_marks(c_id)
            elif choice == 'e':
                c_id = input("Enter course ID: ")
                self.report_course(c_id)
            elif choice == 'f':
                email = input("Enter professor's email: ")
                self.report_professor(email)
            elif choice == 'g':
                email = input("Enter student's email: ")
                self.report_student(email)
            elif choice == 'h':
                break
            else:
                print("Invalid option.")

    def report_course(self, course_id):
        course_id = course_id.strip().lower()
        found_any = False
        current = self.students.head
        print(f"\n--- Course-wise Report for Course ID: {course_id} ---")
        while current:
            if current.student.course_id.lower() == course_id:
                current.student.display_records()
                found_any = True
            current = current.next
        if not found_any:
            print("No students found for that course.")

    def report_professor(self, prof_email):
        prof_email = prof_email.strip().lower()
        professor_found = None
        for p in self.professors:
            if p.email_address.lower() == prof_email:
                professor_found = p
                break
        if not professor_found:
            print("Professor not found.")
            return
        prof_course_id = professor_found.course_id.lower()
        print(f"\n--- Professor-wise Report for: {professor_found.name}, Course: {prof_course_id} ---")
        current = self.students.head
        found_any = False
        while current:
            if current.student.course_id.lower() == prof_course_id:
                current.student.display_records()
                found_any = True
            current = current.next
        if not found_any:
            print("No students found for that professor's course.")

    def report_student(self, student_email):
        student = self.students.search_student(student_email)
        if student:
            print("\n--- Student-wise Report ---")
            student.display_records()
        else:
            print("Student not found.")

if __name__ == "__main__":
    app = CheckMyGradeApp()
    app.run()
