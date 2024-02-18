import queue
import random
import time

# Створення черги заявок
request_queue = queue.Queue()


def generate_request():
    """Генерує нову заявку та додає її до черги."""
    # Генерація унікального ідентифікатора заявки
    request_id = random.randint(1000, 9999)
    print(f"Генеруємо нову заявку з ID: {request_id}")
    # Додавання заявки до черги
    request_queue.put(request_id)


def process_request():
    """Обробляє заявку, видаляючи її з черги."""
    if not request_queue.empty():
        # Видалення заявки з черги
        request_id = request_queue.get()
        print(f"Обробляємо заявку з ID: {request_id}")
    else:
        print("Черга пуста. Немає заявок для обробки.")


def main():
    """Головний цикл програми для генерації та обробки заявок."""
    for _ in range(10):  # Припустимо, генеруємо та обробляємо 10 заявок
        generate_request()
        time.sleep(1)  # Імітація затримки
        process_request()
        time.sleep(1)  # Імітація затримки


if __name__ == "__main__":
    main()
