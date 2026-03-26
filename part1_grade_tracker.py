#Task 1:Data Parsing & Profile Cleaning
raw_students = [
    {"name": "  ayesha SHARMA ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma", "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": " Priya Nair ", "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA", "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ", "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]
cleaned_students = []

print("Validation Status")
for student in raw_students:
    # 1. Name cleaning (Whitespace remove + Title Case)
    clean_name = student["name"].strip().title()
    
    # 2. Roll number to integer
    clean_roll = int(student["roll"])
    
    # 3. marks_str to list of integers
    # First split using comma,then change each mark to integer
    clean_marks = [int(m.strip()) for m in student["marks_str"].split(",")]
    
    # 4. Name Validation (Check if all characters are alphabetic)
    # For allowing space (" ", "") used
    is_valid = clean_name.replace(" ", "").isalpha()
    status = "✓ Valid name" if is_valid else "X Invalid name"
    print(f"{clean_name}: {status}")
    
    # Cleaned data to new list
    cleaned_students.append({
        "name": clean_name,
        "roll": clean_roll,
        "marks": clean_marks
    })
    print("\n--- Student Profiles ---")
for s in cleaned_students:
    print("-" * 30)
    print(f"Student : {s['name']}")
    print(f"Roll No : {s['roll']}")
    print(f"Marks   : {s['marks']}")
print("-" * 30)

#Task 2: Marks Analysis (Loops + Conditionals)

for s in cleaned_students:
    # 1. Total marks and their average
    # s["marks"] it is a list, like [88, 72, 95, 60, 78]
    total_marks = sum(s["marks"])
    number_of_subjects = len(s["marks"])
    s["average"] = total_marks / number_of_subjects
    
    # 2. Putting condition: if average is 50 or greater then pass else fail
    if s["average"] >= 50:
        s["status"] = "Pass"
    else:
        s["status"] = "Fail"

# Now lets print the output to check
print("\nTask 2: Analysis Result")
for s in cleaned_students:
    print(f"{s['name']} | Average: {s['average']:.2f} | Status: {s['status']}")

#Task 3: Class Performance Summary

# 1. Pass and Fail (Count)
pass_count = sum(1 for s in cleaned_students if s['status'] == "Pass")
fail_count = sum(1 for s in cleaned_students if s['status'] == "Fail")

# 2. Class Topper(With high average)
# max() function will be used here
topper = max(cleaned_students, key=lambda x: x['average'])

# 3. Average of the entire class
# Sabhi students ke averages ka sum / total students
class_avg = sum(s['average'] for s in cleaned_students) / len(cleaned_students)

#Final Results Print
print("\n" + "="*30)
print("   CLASS PERFORMANCE SUMMARY")
print("="*30)
print(f"Total Students Passed : {pass_count}")
print(f"Total Students Failed : {fail_count}")
print(f"Class Topper          : {topper['name']} (Avg: {topper['average']:.2f})")
print(f"Class Overall Average : {class_avg:.2f}")
print("="*30)

# Requirement: Roll Number 103's name CAPS and in lowercase 
for s in cleaned_students:
    if s["roll"] == 103:
        print(f"\nSpecial Case (Roll 103):")
        print(f"Uppercase: {s['name'].upper()}")
        print(f"Lowercase: {s['name'].lower()}")

#Task 4: String Manipulation Utility

# Original essay provided in the assignment
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# 1. Strip leading and trailing whitespace
clean_essay = essay.strip()
print(f"\n1. Cleaned Essay (Stripped):\n'{clean_essay}'")

# 2. Convert to Title Case
title_essay = clean_essay.title()
print(f"\n2. Title Case Essay:\n{title_essay}")

# 3. Count occurrences of the word "python" (case-insensitive)
# We use .lower() to ensure all instances are counted correctly
python_count = clean_essay.lower().count("python")
print(f"\n3. Occurrences of 'python': {python_count}")

# 4. Replace "python" with "Python 🐍"
# Note: Using .lower() first to catch all instances, then replacing
replaced_essay = clean_essay.lower().replace("python", "Python 🐍")
print(f"\n4. Replaced Essay:\n{replaced_essay}")

# 5. Split essay into individual sentences
# Splitting based on period followed by a space ". "
sentences_list = clean_essay.split(". ")
print(f"\n5. List of Sentences:\n{sentences_list}")

# 6. Print numbered sentences with proper formatting
print("\n6. Final Numbered Sentences:")
for index, sentence in enumerate(sentences_list, 1):
    # Cleaning each sentence and capitalizing the first letter
    formatted_sentence = sentence.strip().capitalize()
    
    # Adding a period at the end if it's missing
    if not formatted_sentence.endswith("."):
        formatted_sentence += "."
        
    print(f"{index}. {formatted_sentence}")        