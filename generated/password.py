import random
print("-*-" * 10)
print("WELCOME SIMPLE PASSWORD GENERATED")
print("-*-" * 10)

lower_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.upper()
all = '0123456789@$&#!^*%'
result = (lower_case + upper_case + all)

length = 20
password = ''.join(random.sample(result, length))
print(f'RANDOM PASSWORD GENERATED is', password)
print("-*-" * 10)
