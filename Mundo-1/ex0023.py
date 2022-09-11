#num = str(input('Digite um numero de 0 a 9999:')).strip()
#print('unidade:{}'.format(num[3]))
#print('dezena:{}'.format(num[2]))
#print('centena:{}'.format(num[1]))
#print('milhar:{}'.format(num[0]))

num = int(input('Digite um numede de 0 a 9999:'))
unidade = num % 10          #metodo mais facil usar a divisao inteira (//) e fazer o resto da divisao por 10
num =(num - unidade) / 10   #utilizando 1 para unidade, 10 para dezena, 100 para centena, 1000 para milhar
dezena = num % 10
num = (num - dezena) / 10
centena = num % 10
milhar = num / 10
print('unidade:{}'.format(unidade))
print('dezena:{:.0f}'.format(dezena))
print('centena:{}'.format(int(centena)))
print('milhar:{}'.format(int(milhar)))

