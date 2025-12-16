purchases = [
            {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
            {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
            {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
            {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

# Рассчитайте и верните общую выручку (цена * количество для всех записей).
def total_revenue(purchases):
    total = 0
    for purchase in purchases:
        total += purchase["price"] * purchase["quantity"]
    return total


# Верните словарь, где ключ — категория, а значение — список уникальных товаров в этой категории.
def items_by_category(purchases):
    result = {}
    for purchase in purchases:
        category = purchase["category"]
        item = purchase["item"]

        if category not in result:
            result[category] = []

        if item not in result[category]:
            result[category].append(item)

    return result

# Выведите все покупки, где цена товара больше или равна min_price
def expensive_purchases(purchases, min_price):
    result = []
    for purchase in purchases:
        if purchase["price"] > min_price:
            result.append(purchase)

    return result

# Рассчитайте среднюю цену товаров по каждой категории
def average_price_by_category(purchases):
    sum = {}
    count = {}

    for purchase in purchases:
        category = purchase["category"]
        price = purchase["price"]

        if category not in sum:
            sum[category] = 0
            count[category] = 0

        sum[category] += price
        count[category] += 1

    average = {}
    for category in sum:
        average[category] = sum[category] / count[category]

    return average


#  Найдите и верните категорию, в которой куплено больше всего единиц товаров (учитывайте поле quantity).
def most_frequent_category(purchases):
    quantities = {}

    for purchase in purchases:
        category = purchase["category"]
        quantity = purchase["quantity"]

        if category not in quantities:
            quantities[category] = 0

        quantities[category] += quantity

    max_category = None
    max_quantity = 0

    for category in quantities:
        if quantities[category] > max_quantity:
            max_quantity = quantities[category]
            max_category = category

    return max_category



print("Общая выручка:", total_revenue(purchases))
print("Товары по категориям", items_by_category(purchases))
print("Покупки дороже 1.0:", expensive_purchases(purchases, 1.0))
print("Средняя цена по категориям:", average_price_by_category(purchases))
print("Категория с наибольшим количеством проданных товаров:", most_frequent_category(purchases))