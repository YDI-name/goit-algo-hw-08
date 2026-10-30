import heapq


def min_cost_to_connect_cables(cables):
    if not cables or len(cables) == 1:
        return 0

    # Перетворюємо список на мінімальну купу (in-place)
    heapq.heapify(cables)

    total_cost = 0

    # Працюємо, поки не залишиться один цільний кабель
    while len(cables) > 1:
        # Витягуємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Витрати на поточне з'єднання
        current_cost = first + second
        total_cost += current_cost

        # Кладемо об'єднаний кабель назад у купу
        heapq.heappush(cables, current_cost)

    return total_cost


# Приклад використання:
cables = [4, 3, 2, 6]
print(f"Мінімальні витрати: {min_cost_to_connect_cables(cables)}")
