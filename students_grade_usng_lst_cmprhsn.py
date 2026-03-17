students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 42},
    {"name": "Charlie", "score": 91},
    {"name": "David", "score": 65},
    {"name": "Eve", "score": 78}
]

all_scores = [s["score"] for s in students]
avg_score = sum(all_scores) / len(all_scores)

above_average = [s for s in students if s["score"] > avg_score]

graded_list = [
    {**s, "grade": "A" if s["score"] >= 80 else ("B" if s["score"] >= 60 else "C")}
    for s in students
]

print(f"Class Average: {avg_score}")
print("Above Average Students:", above_average)
print("Students with Grades:", graded_list)
