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

3. Установка переменных окружения:

    ```bash
    export BROWSER=CHROME # или FIREFOX 
    export PASSWORD=password
    export LOGIN=user
    ```

    

# Запуск

* Запуск всех тестов проекта:

    ```bash
    python run_tests.py
    ```

* Запуск тестов, удовлетворяющих паттерну:
    ```bash
    python run_tests.py --pattern tests*.py
    ```

* Запуск всех тестов "как в CI":

  ```bash
  python -m unittest run_tests.py
  ```

* Запуск с "одноразовыми" переменными окружения:

  ```bash
  BROWSER=CHROME PASSWORD=user LOGIN=password python run_tests.py
  ```

  

# Разработка

* Запуск линтера:

  ```bash
  flake8
  ```

  

