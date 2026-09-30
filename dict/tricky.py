students = ["Ajay", "Ravi", "Neha"]
scores = [85, 90, 88]

student_record = {"school": "DPS Indore"}
records = []

for i in range(len(students)):
    # breakpoint()
    # student_record = {"school": "DPS Indore"}
    student_record["name"] = students[i]
    student_record["score"] = scores[i]
    records.append(student_record)

print(records)
















# student_record={}
# for i in range(len(students)):
#     # breakpoint()
#     student_record={}
#     student_record["name"] = students[i]
#     student_record["score"] = scores[i]
#     records.append(student_record)

# print(records)
