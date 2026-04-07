"""
Main application - Student Grade Management System Demo
Shows practical usage of OOP classes
"""

from student import Student, Course, StudentManagementSystem


def main():
    """Main function to demonstrate the Student Management System"""
    
    # Create a management system
    system = StudentManagementSystem()
    
    print("\n" + "="*50)
    print("STUDENT GRADE MANAGEMENT SYSTEM")
    print("="*50 + "\n")
    
    # Create students
    print("--- Creating Students ---")
    student1 = Student("Alice Johnson", 20, "S001")
    student2 = Student("Bob Smith", 21, "S002")
    student3 = Student("Charlie Brown", 20, "S003")
    student4 = Student("Diana Prince", 22, "S004")
    
    # Add students to system
    system.add_student(student1)
    system.add_student(student2)
    system.add_student(student3)
    system.add_student(student4)
    
    # Create courses
    print("\n--- Creating Courses ---")
    python_course = Course("Python Programming", "CS101")
    data_science_course = Course("Data Science Basics", "CS102")
    web_dev_course = Course("Web Development", "CS103")
    
    system.add_course(python_course)
    system.add_course(data_science_course)
    system.add_course(web_dev_course)
    
    # Enroll students in courses
    print("\n--- Enrolling Students in Courses ---")
    python_course.enroll_student(student1)
    python_course.enroll_student(student2)
    python_course.enroll_student(student3)
    
    data_science_course.enroll_student(student1)
    data_science_course.enroll_student(student4)
    
    web_dev_course.enroll_student(student2)
    web_dev_course.enroll_student(student3)
    web_dev_course.enroll_student(student4)
    
    # Add grades for students
    print("\n--- Adding Grades for Students ---")
    
    # Alice's grades
    student1.add_grade("Python Programming", 92)
    student1.add_grade("Data Science Basics", 88)
    
    # Bob's grades
    student2.add_grade("Python Programming", 85)
    student2.add_grade("Web Development", 90)
    
    # Charlie's grades
    student3.add_grade("Python Programming", 78)
    student3.add_grade("Web Development", 82)
    
    # Diana's grades
    student4.add_grade("Data Science Basics", 95)
    student4.add_grade("Web Development", 93)
    
    # Display all students
    system.display_all_students()
    
    # Display individual student grades
    print("\n--- Individual Student Grade Reports ---")
    student1.display_grades()
    student2.display_grades()
    student3.display_grades()
    student4.display_grades()
    
    # Display top students
    system.display_top_students(3)
    
    # Display course information
    print("\n--- Course Information ---")
    python_course.display_course_info()
    data_science_course.display_course_info()
    web_dev_course.display_course_info()
    
    # Find and display specific student
    print("\n--- Finding Specific Student ---")
    search_id = "S001"
    found_student = system.find_student(search_id)
    if found_student:
        print(f"Found student with ID {search_id}:")
        found_student.display_info()
        found_student.display_grades()


if __name__ == "__main__":
    main()
