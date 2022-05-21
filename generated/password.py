import random

print('-=-' * 20)
print("WELCOME SIMPLE PASSWORD GENERATED")
print('-=-' * 20)


lower_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.upper()
num = '0123456789'
symbol = '@$&#!^*%'

result = (lower_case + upper_case + num + symbol)

length = 20
password = ''.join(random.sample(result, length))
print(f'RANDOM PASSWORD GENERATED is', {password})
print('-=-' * 20)
print('SEE YOU NEXT TIME')
