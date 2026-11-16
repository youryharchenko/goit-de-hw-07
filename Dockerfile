FROM mageai/mageai:latest

# Встановлюємо бібліотеку для роботи з MySQL через SQLAlchemy
RUN pip install pymysql cryptography