class GradeSystem:

    def __init__(self):
        self.subjects = ["Math", "English", "Science", "Commerce", "Arts"]
        self.scores = []
        self.name = ""


    def input_name(self):
        while True:
            name = input("Enter student name: ").strip()
            if name == "":
                print("Please enter your name first!\n")
            elif not name.replace(" ", "").isalpha():
                print("Name must contain alphabets only!\n")
            else:
                self.name = name
                break


    def input_scores(self):
        print()
        for subject in self.subjects:
            score = float(input(f"Enter {subject} score: "))
            self.scores.append(score)


    def get_grade(self, score):
        if score >= 91:
            return "A+", 5.0
        elif score >= 81:
            return "A", 4.0
        elif score >= 71:
            return "B", 3.0
        elif score >= 61:
            return "C", 2.0
        elif score >= 50:
            return "D", 1.0
        else:
            return "F", 0.0


    def show_results(self):
        print(f"\n=== Results for {self.name} ===")
        total = 0
        gpa_total = 0

        for i in range(len(self.subjects)):
            score = self.scores[i]
            grade, gpa = self.get_grade(score)
            if score >= 50:
                status = "Pass"
            else:
                status = "Fail"    

            print(f"{self.subjects[i]}: {score} | {grade} | {status}")

            total += score
            gpa_total += gpa

        average = total / len(self.subjects)
        final_gpa = gpa_total / len(self.subjects)

        print(f"\nAverage : {average:.2f}")
        print(f"GPA     : {final_gpa:.2f} / 5.0")


    def save_to_file(self):
        filename = "students.txt"

        with open(filename, "a") as f:
            f.write(f"Student: {self.name}\n")
        
            total = 0
            gpa_total = 0

            for i in range(len(self.subjects)):
                score = self.scores[i]
                grade, gpa = self.get_grade(score)
                if score >= 50:
                    status = "Pass"
                else:
                    status = "Fail"

                f.write(f"  {self.subjects[i]}: {score} | {grade} | {status}\n")

                total += score
                gpa_total += gpa

            average = total / len(self.subjects)
            final_gpa = gpa_total / len(self.subjects)

            f.write(f"  Average : {average:.2f}\n")
            f.write(f"  GPA     : {final_gpa:.2f} / 5.0\n")
            f.write("-------------------------------\n")

        print(f"\nSaved to {filename}")


    def run(self):
        print("=== Grade Calculator ===\n")
        self.input_name()
        self.input_scores()
        self.show_results()
        self.save_to_file()


calculator = GradeSystem()
calculator.run()