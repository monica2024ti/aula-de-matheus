ano = inte(input('digite o ano: '))
if (ano%4==0 and ano%100!=0) or ano%400==00:
    print(' o ano é bissexto!')
else:
    print('se nao for bissexto')
