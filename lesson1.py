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

        students.sort(key= lambda x: x["score"], reverse= True)
        print(f"The student with the highest score is: {students[0]["id"]} - {students[0]["name"]} - {students[0]["score"]}")
        print("\n")

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