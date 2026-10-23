import random
from datetime import datetime, timedelta

# Пример генерации реалистичной истории инцидентов для демонстрации жюри
CAMERAS = [
    {"id": "cam_01", "name": "Камера 1 (Цех сборки №1)", "zone": "Зона станков"},
    {"id": "cam_02", "name": "Камера 2 (Склад готовой продукции)", "zone": "Проезд погрузчиков"},
    {"id": "cam_03", "name": "Камера 3 (Погрузочный терминал А)", "zone": "Зона разгрузки"},
    {"id": "cam_04", "name": "Камера 4 (Периметр цеха)", "zone": "Пешеходная дорожка"}
]

VIOLATIONS = [
    {"type": "Отсутствие СИЗ (каска / жилет)", "severity": "Средняя", "weight": 50},
    {"type": "Опасное сближение с техникой", "severity": "Высокая", "weight": 30},
    {"type": "Падение человека / потеря сознания", "severity": "Критическая", "weight": 10},
    {"type": "Использование мобильного телефона у станка", "severity": "Низкая", "weight": 10}
]

STATUSES = ["Подтверждено мастером", "Меры приняты превентивно", "Ложное срабатывание"]

def generate_mock_events(count=40):
    events = []
    now = datetime.now()
    
    for i in range(count):
        cam = random.choice(CAMERAS)
        # Взвешенный выбор типа нарушения
        violation = random.choices(
            VIOLATIONS, 
            weights=[v["weight"] for v in VIOLATIONS]
        )[0]
        
        # Разброс по времени за последние 7 дней
        random_minutes = random.randint(10, 7 * 24 * 60)
        event_time = now - timedelta(minutes=random_minutes)
        
        # Имитация пика нарушений в начале смен (8:00 - 10:00 или 20:00 - 22:00)
        status = "Ложное срабатывание" if random.random() < 0.08 else random.choice(STATUSES[:2])
        
        events.append({
            "id": f"INC-{1000 + i}",
            "timestamp": event_time.strftime("%Y-%m-%d %H:%M:%S"),
            "camera_id": cam["id"],
            "camera_name": cam["name"],
            "zone": cam["zone"],
            "violation_type": violation["type"],
            "severity": violation["severity"],
            "confidence": round(random.uniform(0.85, 0.98), 2),
            "status": status,
            "snapshot_url": f"/static/snapshots/event_{random.randint(1, 5)}.jpg"
        })
        
    return sorted(events, key=lambda x: x["timestamp"], reverse=True)

if __name__ == "__main__":
    mock_data = generate_mock_events(50)
    print(f"Успешно сгенерировано {len(mock_data)} демонстрационных событий.")
    print("Пример первого события:", mock_data[0])
