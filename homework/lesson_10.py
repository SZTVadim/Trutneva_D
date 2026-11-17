def calculate_total(price, tax_percent):
    if tax_percent > 20 or price < 0:
        return "Ошибка: неверные входные данные"
    total = price + (price * tax_percent / 100)
    return total


print(calculate_total(1000, 10))
print(calculate_total(1000, 25))
print(calculate_total(-500, 10))


def get_level(points):
    if points >= 100:
        return "Эксперт"
    elif points >= 50:
        return "Продвинутый"
    elif points >= 20:
        return "Начинающий"
    else:
        return "Новичок"


def process_status(status):
    match status:
        case "active":
            return "Статус активен"
        case "inactive":
            return "Статус неактивен"
        case "pending":
            return "Статус в ожидании"
        case "blocked":
            return "Статус заблокирован"
        case _:
            return "Неизвестный статус"
