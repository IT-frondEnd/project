# /*from ftplib import print_line

print("------------------HUSH KELIPSIZ-------------")
balance = 230000

while True:
    son = int(input("""
          0)chiqish
          1)Ozbek tili
          2)Ingilis tili
          3)Rus tili
        Tilni tanlang: 
        """))
    if son==0:
        break


    elif son == 1:
        tanlangan = int(input("""
        1)Balans
        2)Pul yechish
        3)Pul qoyish
        """))

        if tanlangan == 1:
            print(f"sizning balnsingiz {balance} uzs ga teng!")
        elif tanlangan == 2:
            summa = int(input("Summani kiritng! :"))
            balance = balance - summa
            print(f"sizning balnsizgizda {balance} uzs qoldi")
            print("Marhamat, pulingizni olishingiz mumkin!")
        elif tanlangan == 3:
            summa1 = int(input("Qanchah pul qoyasiz: "))
            balance = balance + summa1
            print(f"sizning balansingiz {balance} ga teng!")

    elif son == 2:
        tanlangan1 = int(input("""
        0)close
        1)Balance
        2)Withdraw money
        3)Deposit money
        """))

        if son==0:
            break

        elif tanlangan1 == 1:
            print(f"Your balance is {balance} UZS!")
        elif tanlangan1 == 2:
            summa = int(input("Enter the amount: "))
            balance = balance - summa
            print(f"Your balance is {balance} UZS left.")
            print("You can now withdraw your money!")
        elif tanlangan1 == 3:
            summa1 = int(input("How much money will you deposit: "))
            balance = balance + summa1
            print(f"Your balance is {balance} UZS!")

    elif son == 3:
        tanlangan2 = int(input("""
        0)закрит
        1)Баланс
        2)Снимать деньги
        3)Вносить деньги
        """))

        if son==0:
           break
        elif tanlangan2 == 1:
            print(f"Ваш баланс {balance} UZS!")
        elif tanlangan2 == 2:
            summa = int(input("Введите сумму: "))
            balance = balance - summa
            print(f"На вашем балансе осталось {balance} UZS.")
            print("Теперь вы можете снять свои деньги!")
        elif tanlangan2 == 3:
            summa1 = int(input("Сколько денег вы хотите внести: "))
            balance = balance + summa1
            print(f"Ваш баланс {balance} UZS!")
