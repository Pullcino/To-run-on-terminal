urna = [
    ["Arthur", 0],
    ["Emily", 0],
    ["ALice", 0]
]

for line in range(4):

    vote = input("Digit the name of the candidate you wanna vote: (Arthur, Emily, Alice)")

    for candidate in urna:

        encontrado = False
    
    for candidato in urna:
        
        if candidato[0] == vote:
            
            candidato[1] += 1
            
            encontrado = True
            break
    
    if not encontrado:
        print("Voto nulo.")

print("\n Results: ")

