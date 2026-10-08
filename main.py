if __name__ == "__main__":
    students = []
    n = int(input("Enter number of students: "))

    for i in range(n):
        student_id = input("Enter student ID: ")
        name = input("Enter full name: ")
        score = float(input("Enter Python score: "))

        student = {"id": student_id, "name": name, "score": score}

        students.append(student)

        print("\n====STUDENT LIST====")
        for student in students:
            print(student["id"], student["name"], student["score"])

        if len(students) > 0:
            highest = student[n]
            for students in students:
                if student["score"] > highest["score"]:
                    highest = student

            print("\n===STUDENT WITH HIGHEST SCORE===")
            print(highest["id"], highest["name"], highest["score"])

            total = 0
            for student in students:
                total = total + student["score"]
            average = total / len(students)

            print("\n===AVARAGE SCORE===")
            print(average)

            print("\n===PASS STUDENTS===")
            for student in students:
                if student["score"] >= 5:
                    print(student["id"], student["name"], student["score"])

            else:
                print("List empty")                       