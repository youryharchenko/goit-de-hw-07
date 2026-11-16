import random

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.
    """
    # Випадковий вибір однієї з трьох медалей
    selected_medal = random.choice(['Bronze', 'Silver', 'Gold'])
    
    print(f"Обрана медаль: {selected_medal}")
    
    # Повертаємо дані, які будуть передані на наступні кроки
    return {"medal": selected_medal}