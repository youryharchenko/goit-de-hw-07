-- Docs: https://docs.mage.ai/guides/sql-blocks
@condition
def evaluate_condition(outputs, *args, **kwargs) -> bool:
    # outputs отримує результат від батьківського блоку pick_medal
    last_output = outputs[0] if outputs else {}
    # Блок виконається лише якщо обрана медаль 'gold'
    return last_output.get("medal") == "gold"@condition
