sH = input('Height (cm): ')
sW = input('Weight (kg): ')

h1 = int(sH)
weight = float(sW)
height = float(h1/100)

bmi = weight/(height**2)

if bmi<18.5:
    print('Too Light')
elif 18.5<=bmi<25:
    print('Normal')
elif 25<=bmi<28:
    print('Overweight')
elif 28<=bmi<32:
    print('Fat')
else:
    print('Seriously Fat')
