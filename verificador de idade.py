idade= int(input('digite a idade:'))

if idade < 13:
    print('criança')
elif idade > 13 and idade < 17 :
    print('adolescente')
elif idade > 18 and idade < 60 :
    print('adulto')
else :
    print('idoso')
 