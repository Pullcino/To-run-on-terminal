q1 = int(input("1 - Add a person\n2 - Leave\n"))
number_of_people = 0
people = []

while q1 != 2:
    if q1 == 1:

        info1 = input("Digit the name of the person: ")
        info2 = int(input("Digit the age of the person: "))
        person = {"Name": info1, "Age": info2}

        people.append(person)
        number_of_people = number_of_people + 1

        
        oldest = max(people, key=lambda x: x["Age"])
        youngest = min(people, key=lambda x: x["Age"])

        q1 = int(input("1 - Add a person\n2 - Leave\n"))

    if q1 == 2:


        print(f"All the people: {people}")
        print(f"{number_of_people} people were registered")
        print(f"Oldest person: {oldest}")
        print(f"Yougest person: {youngest}")

        break