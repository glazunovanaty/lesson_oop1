class Discount:
    """
    Класс Discount

    Этот класс представляет скидку в интернет-магазине.

    Метод __init__:
        Конструктор инициализирует объект Discount с двумя атрибутами: description (описание дисконта) и discount_percent  (размер скидки).
        Пример: discount1 = Discount("Летнаяя распродажа", 50) создаст скидку с названием "Летняя распродажа" и значением скидки 50.

    Метод __str__:
        Возвращает строковое представление объекта, чтобы его можно было удобно вывести с помощью print.
        Пример: print(discount1) выведет Скидка Летняя распродажа размер 50%.
    """
    def __init__(self, description: str, discount_percent: int):
        self.description  = description 
        self.discount_percent   = discount_percent 

    def __str__(self):
        return f"Скидка {self.description} размер {self.discount_percent}%"
    
    @staticmethod
    def calculate_discounted_price(product, discount):
        result=product.price * (1 - discount.discount_percent / 100)
        print(f"Расчет скидки для товара {product.name} с ценой {product.price} '{discount.description}' в размере {discount.discount_percent}%, цена со скидкой = {int(result)}")
        return result
        
    @staticmethod
    def activate_discount_to_order(order, discount):
        for product in order.products:
            product.price=product.price * (1 - discount.discount_percent / 100)
        print(f"К заказу применена скидка {discount.description} в размере {discount.discount_percent}%\n Обновленный заказ:\n {order}\n")
        return
        
