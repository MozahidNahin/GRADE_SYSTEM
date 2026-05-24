class GradeSystem:

    def __init__(self):
        self.subjects = ["Math", "English", "Science", "Commerce", "Arts"]
        self.scores = []

    def input_scores(self):
        print("=== Grade Calculator ===\n")
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
        print("\n--- Results ---")
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
        self.input_scores()
        self.show_results()


calculator = GradeSystem()
calculator.run()