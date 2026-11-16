import time

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(*args, **kwargs):
    print(f"Отримані дані від усіх батьківських блоків: {args}")
    # Безпечно витягуємо дані від активного батьківського блоку
    active_data = None
    # Перебираємо результати від усіх гілок, ігноруючи None
    for item in args:
        if item:
            active_data = item
            break

    print(f"Активні дані з гілки: {active_data}")
    
    # Затримка 35 секунд для тестування сенсора (пункт 6 завдання)
    delay_seconds = 35
    print(f"⏳ Початок затримки на {delay_seconds} секунд...")
    time.sleep(delay_seconds)
    print("✅ Затримку успішно завершено!")
    
    return {"status": "completed", "delayed_seconds": delay_seconds}