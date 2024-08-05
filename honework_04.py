# # Задание 1
import random
dex_name = "OKX"
wallet_address = "0x127sw218sshwv222scacswaf2"
random_num = random.randint(1, 60)
print(f"Вывожу {random_num} токенов с биржи {dex_name} на кошелек {wallet_address}")

# # Задание 2
number = -15
print(abs(number) + 10)

# Задание 3
num = int(input())
print(f"является ли число {num} четным: {num % 2 == 0}")
print(f"является ли число {num} нечетным: {num % 2 != 0}")

# Задание 4
balance = 20
transaction_count = 56
volume = 11000
middle_transaction_summ = volume / transaction_count
drop_balance = 25
drop_transaction_count = 50
drop_volume = 10000
drop_middle_transaction_summ = 100


print(f"Eligible:{balance > drop_balance and transaction_count > drop_transaction_count and volume > drop_volume and middle_transaction_summ > drop_middle_transaction_summ} ")





