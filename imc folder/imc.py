print('Body mass index (BMI) is a simple way to identify weight-related problems, such as obesity or malnutrition, in children, adolescents, adults, and the elderly.In addition to calculating your BMI, this calculator also indicates the ideal weight range you should have to ensure a better quality of life. Maintaining a weight within the ideal range helps prevent the onset of several chronic diseases, such as diabetes and hypertension.Enter your data into the calculator and calculate your BMI:')

height = float(input('What is your height : '))

if len(height) == 3 :

    height = height * 30.48

weight = float(input('What is you weight : '))

result = weight / (height*height)

print(result)