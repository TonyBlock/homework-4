# Сборка
1. Настройка virtual enviroment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
2. Установка зависимостей:
    ```bash
   pip install -r requirements.txt
   ```

3. У

# Запуск

* Запуск всех тестов проекта:

    ```bash
    ./run_tests.py
    ```

* Запуск тестов, удовлетворяющих паттерну
    ```bash
    ./run_tests.py --pattern tests*.py
    ```

* Запуск всех тестов "как в CI":

  ```bash
  python -m unittest run_tests.py
  ```

# Разработка

* Запуск линтера:

  ```bash
  flake8
  ```

  

