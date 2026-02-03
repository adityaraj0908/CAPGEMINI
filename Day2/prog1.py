no_of_students_who_passed = 0

students = [("A", 78),("B", "ab"),("C", 35),("D", 92),("E", 120)  ]

for name, marks in students:
    if marks == "ab":
        continue

    if marks > 100:
        break

    if marks >= 40:
        pass_count += 1

print("Number of students passed:", no_of_students_who_passed)
