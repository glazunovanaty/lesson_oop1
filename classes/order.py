class Order:
    """
    Класс Order

    Этот класс представляет заказ в интернет-магазине.

    Атрибут класса _total_orders:
        Счетчик всех созданных заказов. Это атрибут класса, а не экземпляра, поэтому он общий для всех объектов Order.

    Метод __init__:
        Конструктор принимает список товаров (products) и инициализирует объект Order.
        Увеличивает счетчик _total_orders на 1 каждый раз при создании нового заказа.
        Пример: order1 = Order([product1]) создаст заказ, содержащий один товар.

    Метод calculate_discounted_price:
        Статический метод, который принимает цену и скидку в процентах и возвращает цену после применения скидки.
        Пример: Order.calculate_discounted_price(1000, 10) вернет 900.0.

    Метод total_orders:
        Метод класса, который возвращает общее количество созданных заказов.
        Пример: Order.total_orders() вернет общее количество заказов.

    Метод total_price:
        Вычисляет общую стоимость всех товаров в заказе, суммируя их цены.
        Пример: order1.total_price() вернет 1000, если в заказе один товар с ценой 1000.

    Метод __str__:
        Возвращает строковое представление объекта заказа, включающее общую стоимость заказа.
        Пример: print(order1) выведет Order(total_price=1000).
    """
    _total_orders = 0
    _global_order_list=list()
    
    def __init__(self, products):
        self.products = products
        Order._total_orders += 1
        Order._global_order_list.append(self)
        

    #@staticmethod
    #def calculate_discounted_price(price, discount):
    #    return price * (1 - discount / 100)

    @classmethod
    def total_orders(cls):
        return cls._total_orders

    def total_price(self):
        return sum(product.price for product in self.products)

    def __str__(self):
        result_str=f"Заказ: \n"
        for product in self.products:
            result_str+=product.__str__()+"\n"
        result_str+=f"Общая сумма заказа = {self.total_price()}"
        return result_str
    
    @staticmethod
    def sum_orders():
        summ=0
        for order in Order._global_order_list:
            for product in order.products:
                summ+=product.price
        return summ