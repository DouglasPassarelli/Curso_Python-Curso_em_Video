tabuada = int(input('Digite um numero:'))
print('A tabuada de {} e'.format(tabuada))
print('=' *12)
count = 0
r = 1
for count in range(10):
   count = count + 1
   r = tabuada * count
   print(tabuada,  'X', count, '= {}'.format(r))
print('=' *12)

#Segunda opção

#nu = (int(input('Digite um numero:')))
#print('A tabuada de {} e'.format(nu))
#print('=' * 12)
#print('{} X {:2} = {}'.format(nu, 1, nu*1))
#print('{} X {:2} = {}'.format(nu, 2, nu*2))
#print('{} X {:2} = {}'.format(nu, 3, nu*3))
#print('{} X {:2} = {}'.format(nu, 4, nu*4))
#print('{} X {:2} = {}'.format(nu, 5, nu*5))
#print('{} X {:2} = {}'.format(nu, 6, nu*6))
#print('{} X {:2} = {}'.format(nu, 7, nu*7))
#print('{} X {:2} = {}'.format(nu, 9, nu*9))
#print('{} X {:2} = {}'.format(nu, 10, nu*10))
#print('=' *12)
