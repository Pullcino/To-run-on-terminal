urna = [
    ["Arthur", 0],
    ["Emily", 0],
    ["ALice", 0]
]

for line in range(4):

    vote = input("Digit the name of the candidate you wanna vote: (Arthur, Emily, Alice)")

    encontrado = False

    for candidato in urna:
        
        if candidato[0] == vote:
            
            candidato[1] += 1
            
            encontrado = True
            break
    
    if not encontrado:
        print("Voto nulo.")

maximum_votes = -1
winner = ""

for candidato in urna:

    print(f"{candidato[0]}: {candidato[1]} votos")

    if candidato[1] > maximum_votes:

        maximum_votes = candidato[1]
        
        winner = candidato[0]

print(f"The winner is : {winner} com {maximum_votes} votes")


