print('Body mass index (BMI) is a simple way to identify weight-related problems, such as obesity or malnutrition, in children, adolescents, adults, and the elderly.\nIn addition to calculating your BMI, this calculator also indicates the ideal weight range you should have to ensure a better quality of life.\nMaintaining a weight within the ideal range helps prevent the onset of several chronic diseases, such as diabetes and hypertension.\nEnter your data into the calculator and calculate your BMI:')

height = float(input('What is your height : '))

type_ = input('Is the measurement in feet or meters : ')

if type_ == 'feet':

    height = height * 0.3048

    print('Next question')


else:

    print('Next question')

weight = float(input('What is your weight : '))

type_2 = input('Is the measurement pounds or kilogram : ')

if type_2 == 'pounds':

    convert_2 = weight * 0.45

    result = weight / (height*height)

    print(f'Your BMI is {result}')

else:

    result = weight / (height*height)

    print(f'Your BMI is {result}')

print('See the table below :\nBMI less than 18,5 = thinness\nBMI between 18,5 and 24,9 = Normal\nBMI between 25 and 29,9 = overweight\nBMI between 30,0 and 34,9 = Grade I obesity\nBMI between 35 and 39,9 = Grade II obesity\nBMI Greater than 40 = Grade III obesity ')

if result < 18.5:

    print('Your situation is thinness')

elif result >= 18.5 and result <= 24.9:

    print('Your situation is normal')

elif result >= 25 and result <=29.9:

    print('Your situation is overweight')

elif result >= 30 and result <=34.9:

    print('Your situation is Grade I obesity')

elif result >= 35 and result <=39.9:

    print('Your situation is Grade II obesity')

else:

    print('Your situation is Grade III obesity')