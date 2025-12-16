purchases = [
            {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
            {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
            {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
            {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


def total_revenue(purchases):
    total = 0
    for purchase in purchases:
        total += purchase["price"] * purchase["quantity"]
    return total

print("Общая выручка:", total_revenue(purchases))