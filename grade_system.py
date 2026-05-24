class GradeSystem:

    def __init__(self):
        self.subjects = ["Math", "English", "Science", "Commerce", "Arts"]
        self.scores = []
        self.name = ""

    def input_name(self):
        while True:
            name = input("Enter Your Name: ").strip()
            if name == "":
                print("Must Enter Your Name First!\n")
            elif not name.replace(" ", "").isalpha():
                print("Name Must Be In Alphabets Only!\n")
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
            status = "Pass" if score >= 50 else "Fail"

            print(f"{self.subjects[i]}: {score} | {grade} | {status}")

            total += score
            gpa_total += gpa

        average = total / len(self.subjects)
        final_gpa = gpa_total / len(self.subjects)

        print(f"\nAverage : {average:.2f}")
        print(f"GPA     : {final_gpa:.2f} / 5.0")

    def run(self):
        print("=== Grade Calculator ===\n")
        self.input_name()
        self.input_scores()
        self.show_results()


calculator = GradeSystem()
calculator.run()