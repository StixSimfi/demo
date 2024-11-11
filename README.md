# demo
Демонстрационный проект.

## Запуск в контейнерах
Для запуска сборки контейнеров перейдите в директорию src/docker
- cd src/docker
- Выпоните команду docker-compose up -d --build
- Результат прогонки тестов будут размещены в директории result.

## Запуск локально
Для запуска локально выполните команды в корневой папке проекта:
- python -m venv .venv
- . .venv/bin/activate (для Linux) .venv/Scripts/activate.bat
- pip install poetry
- poetry install
- pytest test -n 4 -q --alluredir=allure_reports

