M_students = []

for i in range(3):

    name = input(f"Digit the name of the student {i + 1}: ")

    notes = []

    for j in range(4):

        note = int(input(f"Digit the note {j + 1} of the student {name}: "))

        notes.append(note)

    M_students.append([name] + notes)

for student in M_students:

    name = student[0]

    notes = student[1:]

    media = sum(notes) / 4

    print("\n" + "-"*40)
    print(f"Name: {name}")
    print(f"Notes: {notes}")
    print(f"Média: {media}")

