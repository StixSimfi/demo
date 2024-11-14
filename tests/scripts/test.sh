#!/bin/bash
flake8 > flake_reports/result_$(date +"%Y-%m-%d_%H.%M.%S").txt
pytest tests -n 8 -q --alluredir=allure_reports
sleep 5m
