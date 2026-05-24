print("=== Grade Calculator ===\n")

subjects = ["Math", "English", "Science", "Commerce", "Arts"]
scores = []

for subject in subjects:
    score = float(input(f"Enter {subject} score: "))
    scores.append(score)

print("\n--- Results ---")

total = 0
gpa_total = 0

for i in range(len(subjects)):
    score = scores[i]
    total += score

    if score >= 91:
        grade = "A+"
        gpa = 5.0
    elif score >= 81:
        grade = "A"
        gpa = 4.0
    elif score >= 71:
        grade = "B"
        gpa = 3.0
    elif score >= 61:
        grade = "C"
        gpa = 2.0
    elif score >= 50:
        grade = "D"
        gpa = 1.0
    else:
        grade = "F"
        gpa = 0.0

    gpa_total += gpa

    status = "Pass" if score >= 50 else "Fail"
    print(f"{subjects[i]}: {score} | {grade} | {status}")

average = total / len(subjects)
final_gpa = gpa_total / len(subjects)

print(f"\nAverage: {average:.2f}")
print(f"GPA: {final_gpa:.2f} / 5.0")
