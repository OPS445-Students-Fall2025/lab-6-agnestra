#!/usr/bin/env python3
#Author: Agnestra Mahat
#Author ID: 128939238

class Student:
    #Define the name and number when a student object ias created, ex.student1 = Student('john', 025969102)
    def __init__(self, name, number):
        self.name = name
        self.number = number 
        self.courses = {}
        
    #Return student name and number, works even when the datatype for student number is not an string
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + str(self.number)
    
    # Add a new course and grade to student record
    def addGrade(self, course, grade):
        self.courses[course] = grade
    
    #Calculate the grade points average of all courses, avoids zero division error
    def displayGPA(self):
        if len(self.courses) == 0:      
            gpa = 0.0
            return 'GPA of student ' + self.name + ' is ' + str(gpa)
        else:
            gpa = 0.0
            for course in self.courses.keys():
                gpa = gpa + self.courses[course]
            return 'GPA of student ' + self.name + ' is ' + str(gpa/float(len(self.courses)))
        
        
    
    #Return a list of course that the student passed(not a 0.0 grade)
    def displayCourses(self):
        passedCourses = []
        for course in self.courses:
            if self.courses[course] > 0.0:
                passedCourses.append(course)
        return passedCourses
    
if __name__ == '__main__':
    #Create first studnet object and add grades for each class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)


    #Create second student object and add grades for each class
    student2 = Student('Jessica', '123456')
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    #Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    #Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())

