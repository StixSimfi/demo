# demo
Демонстрационный проект.
Часть кода из реальной задачи.
Есть некий сервер с проектами, которые хранятся в контейнерах docker.
Политика безопасности не позволяет управлять инфраструктурой. DevOps написали 
hooks, принимающие запрос вида:
curl -fH "X-Webhook-Token: 4f69baaf-a498-48a4-8275-405f8a10d175" http://someserver:8089/hooks/docker-qa-manage?command=ps
и возвращающий ответ в виде строки:
"sbp_nspk_sanbox-iso_20022_server-1";"stoped";"2024-10-25 12:18:42 +0300 MSK";"someserver.prod.mc/sbp_nspk_sanbox:iso_moc;"Up 10 days"
"sbp_nspk_sanbox-http_sbp_mk_server-1";"exited";"2024-10-25 12:18:42 +0300 MSK";"someserver.prod.mc/sbp_nspk_sanbox:iso_moc;"Exited (1) 10 days ago"
"sbp_nspk_sanbox-nginx-1";"running";"2024-10-25 12:18:42 +0300 MSK";"someserver.prod.mc/aotps_dkk/sbp_nspk_sanbox:iso_moc_nginx;"Up 10 days"
Необходимо реализовать некий api и front для управления контейнерами включающий:
- Получение списка контейнеров (добавлять и удалять мы их не можем, получаем только строку состояния листа)
- Реализовать команды запуска, остановки и перезагрузки контейнеров.
Проект демонстрационный токен забит гвоздями не реализовывалась авторизация на сервере, окружение забито гвоздями.

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

