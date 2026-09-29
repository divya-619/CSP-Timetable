# 1. Variables (subjects)
subjects = ["Maths", "Python", "DBMS", "AI"]

# 2. Domain (available time slots)
slots = ["9:00 AM", "11:00 AM", "2:00 PM"]

# 3. Constraints (these pairs cannot be in the same slot)
not_together = [("Maths", "Python"), ("DBMS", "AI")]

timetable = {}

def is_safe(subject, slot):
    """Return True if giving this slot to the subject breaks no rule."""
    for a, b in not_together:
        if subject == a and timetable.get(b) == slot:
            return False
        if subject == b and timetable.get(a) == slot:
            return False
    return True

def solve(index):
    """Assign slots one subject at a time (backtracking)."""
    # All subjects done -> solution found
    if index == len(subjects):
        return True

    subject = subjects[index]

    for slot in slots:
        if is_safe(subject, slot):
            timetable[subject] = slot      
            if solve(index + 1):           
                return True
            del timetable[subject]         

    return False

if solve(0):
    print("Final Timetable")
    print("-" * 22)
    for subject in subjects:
        print(subject, "->", timetable[subject])
else:
    print("No valid timetable found.")