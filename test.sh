#!/bin/bash
. .venv/bin/activate
mkdir flake_reports -p
flake8 > flake_reports/result_$(date +"%Y-%m-%d_%H.%M.%S").txt
pytest tests -n 8 -m "api" -q --alluredir=allure_reports
sleep 5m
