"""
Student Grade Management System
Demonstrates OOP concepts: Classes, Encapsulation, Inheritance, and Methods
"""


class Person:
    """Base class for all persons"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        """Display basic person information"""
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    """Student class inheriting from Person"""
    
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = {}  # Dictionary to store course name and grades
    
    def add_grade(self, course, grade):
        """Add a grade for a course"""
        if 0 <= grade <= 100:
            self.courses[course] = grade
            print(f"✓ Added grade {grade} for {course}")
        else:
            print(f"✗ Invalid grade. Please enter grade between 0-100")
    
    def get_gpa(self):
        """Calculate average GPA"""
        if not self.courses:
            return 0
        return sum(self.courses.values()) / len(self.courses)
    
    def display_info(self):
        """Override parent method to display student info"""
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"GPA: {self.get_gpa():.2f}")
    
    def display_grades(self):
        """Display all grades for the student"""
        if not self.courses:
            print(f"{self.name} has no grades yet.")
            return
        
        print(f"\n--- Grades for {self.name} ---")
        for course, grade in self.courses.items():
            print(f"  {course}: {grade}")
        print(f"Average GPA: {self.get_gpa():.2f}\n")


class Course:
    """Course class to manage course information"""
    
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.students = []
    
    def enroll_student(self, student):
        """Enroll a student in the course"""
        if student not in self.students:
            self.students.append(student)
            print(f"✓ {student.name} enrolled in {self.course_name}")
        else:
            print(f"✗ {student.name} is already enrolled")
    
    def display_course_info(self):
        """Display course information"""
        print(f"\nCourse: {self.course_name} ({self.course_code})")
        print(f"Enrolled Students: {len(self.students)}")
        for student in self.students:
            print(f"  - {student.name} (ID: {student.student_id})")


class StudentManagementSystem:
    """Management system for students and courses"""
    
    def __init__(self):
        self.students = []
        self.courses = []
    
    def add_student(self, student):
        """Add a student to the system"""
        self.students.append(student)
        print(f"✓ Student {student.name} added to system")
    
    def add_course(self, course):
        """Add a course to the system"""
        self.courses.append(course)
        print(f"✓ Course {course.course_name} added to system")
    
    def find_student(self, student_id):
        """Find a student by ID"""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def display_all_students(self):
        """Display information for all students"""
        print("\n" + "="*50)
        print("ALL STUDENTS IN SYSTEM")
        print("="*50)
        if not self.students:
            print("No students in system")
            return
        
        for student in self.students:
            student.display_info()
            print("-" * 50)
    
    def display_top_students(self, n=3):
        """Display top N students by GPA"""
        if not self.students:
            print("No students in system")
            return
        
        sorted_students = sorted(self.students, key=lambda s: s.get_gpa(), reverse=True)
        print(f"\n{'TOP ' + str(n) + ' STUDENTS':^50}")
        print("="*50)
        for i, student in enumerate(sorted_students[:n], 1):
            print(f"{i}. {student.name} - GPA: {student.get_gpa():.2f}")
        print("="*50)
