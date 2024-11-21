
import random
import time
import threading

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.transaction = 100

    def deposit(self):
        for i in range(self.transaction):
            amount = random.randint(50,500)
            self.balance += amount
            print(f'Пополнение: {amount}. Баланс: {self.balance}.')
            if self.balance >= 500 and self.lock.locked():
               self.lock.release()
               time.sleep(0.001)

    def take(self):
        for i in range(self.transaction):
            amount = random.randint(50, 500)
            print(f'Запрос на {amount}')
            #self.lock.acquire()
            if amount <= self.balance:
                self.balance -= amount
                print(f'Снятие: {amount}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                time.sleep(0.001)



bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')






