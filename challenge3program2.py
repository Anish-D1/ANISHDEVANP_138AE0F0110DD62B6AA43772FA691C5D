
#*challenge 3program 2*
#ANISH DEVAN P


class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  # Syntax - lambda arg:exp
  return sorted_students


students = [
    Student("Aron", "A123", 8.8),
    Student("Saikrishna", "A124", 7.6),
    Student("Sowmiya", "A125", 9.0),
    Student("Mahima", "A126", 9.9),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                     student.roll_number,
                                                     student.cgpa))
