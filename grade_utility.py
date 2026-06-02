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