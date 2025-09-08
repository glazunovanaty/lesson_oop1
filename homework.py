# Пример использования статических методов и методов класса в интернет-магазине
# Предположим, у нас есть интернет-магазин с классом Product, который представляет товар, и классом Order, который представляет заказ. 
# Мы будем использовать статические методы для расчета скидок и методы класса для подсчета общего количества заказов.
from classes.order import Order
from classes.product import Product
from classes.customer import Customer
from classes.discount import Discount

# Создаем продукты
product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 500)
product3 = Product("TV", 7000)

# Создаем заказы
order1 = Order([product1])
order2 = Order([product2, product1])

customer1=Customer("Иван",[order1,order2])
print(customer1)

# Выводим общее количество заказов
print(f"Всего заказов: {Order.total_orders()}")  # Вывод: Всего заказов: 2

# Выводим информацию о заказах
print(order1)  # Вывод: Заказ (Общая цена = 1000)
print(order2)  # Вывод: Заказ (Общая цена = 1500)
print()

#Сравним товары по цене
print(product1==product2) # Вывод: False
print(product2<product1) # Вывод: True
print(product2>product1) # Вывод: False
print()

#Создаем скидки
discount1 = Discount("Летняя распродажа", 50)
discount2 = Discount("Скидка постоянного клиента", 10)
print(discount1) # Вывод: Скидка Летняя распродажа размер 50%
print(discount2) # Вывод:  Скидка Скидка постоянного клиента размер 10%

#Вывод общего количества заказов
print(f"Всего создано заказов {Order._total_orders} на общую сумму {Order.sum_orders()}") 
# Вывод: Всего создано заказов 2 на общую сумму 2500
print()

#Создание новых заказов и нового покупателя
order3 = Order([product2, product1, product3])
customer2=Customer("Мария",[order3])
print(customer2) # Вывод Клиент: Мария Заказы:  Заказ:  Smartphone Цена=500 Laptop Цена=1000 TV Цена=7000 Общая сумма заказа = 8500 
print()
#Вывод общего количества заказов
print(f"Всего создано заказов {Order._total_orders} на общую сумму {Order.sum_orders()}") # Вывод Всего создано заказов 3 на общую сумму 11000
print()

#Добавление заказа
order4 = Order([product1,product2])
customer2.append_order([order4])
print(customer2) # Вывод Клиент: Мария Заказы:  Заказ: Smartphone Цена=500 Laptop Цена=1000 TV Цена=7000 Общая сумма заказа = 8500  Заказ:  Laptop Цена=1000 Smartphone Цена=500 Общая сумма заказа = 1500 
print()
#Вывод общего количества заказов
print(f"Всего создано заказов {Order._total_orders} на общую сумму {Order.sum_orders()}") #Всего создано заказов 4 на общую сумму 12500
print()

#Расчет скидок для товаров
Discount.calculate_discounted_price(product1,discount1) #Расчет скидки для товара Laptop с ценой 1000 'Летняя распродажа' в размере 50%, цена со скидкой = 500
Discount.calculate_discounted_price(product2,discount2) #Расчет скидки для товара Smartphone с ценой 500 'Скидка постоянного клиента' в размере 10%, цена со скидкой = 450
print()

#Применение скидки к заказу
Discount.activate_discount_to_order(order2,discount2)
print(f"Всего создано заказов {Order._total_orders} на общую сумму {Order.sum_orders()}")
print()
Discount.activate_discount_to_order(order3,discount2)
print(f"Всего создано заказов {Order._total_orders} на общую сумму {Order.sum_orders()}")
print()
Discount.activate_discount_to_order(order2,discount2)
print(f"Всего создано заказов {Order._total_orders} на общую сумму {Order.sum_orders()}")
print()

