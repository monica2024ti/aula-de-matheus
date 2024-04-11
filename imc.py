peso =  float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Magreza')
elif imc > 18.5 and imc < 24.9:
    print('Saudável')
elif imc > 25 and imc < 29.9:
    print('Sobrepeso')
elif imc > 30 and imc < 34.9:
    print("obesidade grau 1")
elif imc >  35 and imc < 39.9:
    print('obesidade grau 2')
else:
    print("obeso morbido")



