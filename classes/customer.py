class Customer:
    """
    Класс Customer

    Этот класс представляетклиента в интернет-магазине.

    Метод __init__:
        Конструктор инициализирует объект Product с двумя атрибутами: name (название товара) и orders (список заказов).
        Пример: customer1 = Customer("Иван", [order1, order2]) создаст клиента с именем "Иван" и списком из 2-х заказрв
    Метод __str__:
        Возвращает строковое представление объекта, чтобы его можно было удобно вывести с помощью print.
        Пример: print(customer1) выведет:
        Клиент: Иван
        Заказы:
        Заказ 1
        Заказ 2
    """
    
    def __init__(self, name: str, orders: list):
        self.name = name
        self.orders = orders
        __count_orders = len(orders)

    def __str__(self): 
        result_str=f"Клиент: {self.name}\nЗаказы: \n"
        for order in self.orders:
            result_str+=f"{order.__str__()} \n"
        return result_str
    
    def append_order(self,orders:list):
        for order in orders:
            self.orders.append(order)
        