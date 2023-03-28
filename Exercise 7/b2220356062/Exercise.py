try:
    import sys
except ImportError:
    print("Error: Cannot import sys module")
    sys.exit(1)

input_file = 'Students.txt'

all_students = []

for line in open(input_file, "r"):
    line = line.rstrip()
    students = line.split(':')
    uni_department = students[1].split(',')
    students.pop(1)
    for i in uni_department:
        students.append(i)
    all_students.append(students)
    

names_found = set()
for student in all_students:
    for i in range(1, len(sys.argv)):
        try:
            name_index = student.index(sys.argv[i])
            name = student[name_index]
            print("Name: {}, University: {}, Department: {}".format(name, student[name_index+1], student[name_index+2]))
            names_found.add(name)
        except ValueError:
            continue

for i in range(1, len(sys.argv)):
    if sys.argv[i] not in names_found:
        print("No record of '{}' was found!".format(sys.argv[i]))