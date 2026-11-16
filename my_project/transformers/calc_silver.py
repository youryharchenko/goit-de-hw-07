import pymysql

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(data, *args, **kwargs):
    selected_medal = None
    
    # Безпечне вилучення обраної медалі з урахуванням можливих форматів вхідних даних
    try:
        if isinstance(data, list) and len(data) > 0:
            first_item = data[0]
            if isinstance(first_item, dict):
                selected_medal = first_item.get("medal")
        elif isinstance(data, dict):
            selected_medal = data.get("medal")
    except Exception as e:
        print(f"Попередження при розборі даних: {e}")
    
    target_medal = "Silver"
    
    if selected_medal != target_medal:
        print(f"Це не {target_medal}. Блок пропущено.")
        return None
        
    print(f"Виконується розрахунок та запис для {target_medal}!")
    
    
    connection = pymysql.connect(
        host='mysql',
        user='mage_user',
        password='mage_password',
        database='medal_db',
        port=3306
    )
    
    try:
        with connection.cursor() as cursor:
            # Звертаємося до локальної тестової таблиці athlete_event_results
            query = """
                INSERT INTO medal_results (medal_type, count, created_at)
                SELECT %s, COUNT(*), NOW()
                FROM athlete_event_results
                WHERE medal = %s
            """
            cursor.execute(query, (target_medal, target_medal))
            connection.commit()
            print(f"Успішно записано дані для {target_medal}!")
    finally:
        connection.close()
        
    return {"medal_type": target_medal, "status": "inserted"}