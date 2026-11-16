-- 1. Створюємо цільову таблицю для результатів згідно з пунктом 1 завдання
CREATE TABLE IF NOT EXISTS medal_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    medal_type VARCHAR(50),
    count INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Створюємо тестову таблицю-джерело athlete_event_results
CREATE TABLE IF NOT EXISTS athlete_event_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    athlete_name VARCHAR(100),
    medal VARCHAR(50)
);

-- 3. Очищаємо та наповнюємо тестовими даними (наприклад: 3 Gold, 2 Silver, 4 Bronze)
DELETE FROM athlete_event_results;

INSERT INTO athlete_event_results (athlete_name, medal) VALUES 
('An athlete 1', 'Gold'),
('An athlete 2', 'Gold'),
('An athlete 3', 'Gold'),
('An athlete 4', 'Silver'),
('An athlete 5', 'Silver'),
('An athlete 6', 'Bronze'),
('An athlete 7', 'Bronze'),
('An athlete 8', 'Bronze'),
('An athlete 9', 'Bronze');