#!/bin/bash
. .venv/bin/activate
mkdir flake_reports -p
flake8 > flake_reports/result_$(date +"%Y-%m-%d_%H.%M.%S").txt
pytest tests -n 8 -m "ui" -q --alluredir=allure_reports
sleep 3s
copy flake_reports resul && cope allure_reports result
sleep 5m
