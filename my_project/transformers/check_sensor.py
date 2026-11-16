import pymysql
from datetime import datetime

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(data, *args, **kwargs):
    
    
    connection = pymysql.connect(
        host='mysql',
        user='mage_user',
        password='mage_password',
        database='medal_db',
        port=3306
    )
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT created_at FROM medal_results ORDER BY id DESC LIMIT 1;")
            row = cursor.fetchone()
            if not row:
                raise Exception("❌ Таблиця порожня, записи відсутні!")
            
            latest_time = row[0]
            now = datetime.now()
            diff_seconds = (now - latest_time).total_seconds()
            
            print(f"Час найновішого запису: {latest_time}, поточний час: {now}, різниця: {diff_seconds:.1f} сек")
            
            # Перевірка: якщо запис старший за 30 секунд, сенсор падає
            if diff_seconds > 30:
                raise Exception(f"❌ Сенсор впав: найновіший запис занадто старий ({diff_seconds:.1f} сек > 30 сек)!")
            else:
                print("✅ Сенсор успішно пройшов перевірку: запис свіжий!")
    finally:
        connection.close()
        
    return {"sensor_status": "passed"}