# Simple Timetable CSP using Backtracking

This program assigns time slots to four subjects: **Maths, Python, DBMS, and AI**.

Available time slots are **9:00 AM, 11:00 AM, and 2:00 PM**.

The program follows two rules:

* Maths and Python should not have the same time slot.
* DBMS and AI should not have the same time slot.

It uses **Backtracking** to assign the slots. If a conflict occurs, it goes back and tries another slot.

**Assign → Check → If conflict, go back → Try another slot → Continue until a valid timetable is found**

Finally, it prints a valid timetable that follows all the given rules.
