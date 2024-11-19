#!/bin/bash
flake8 > flake_reports/result_$(date +"%Y-%m-%d_%H.%M.%S").txt
pytest tests -q --alluredir=allure
cp -r allure allure_reports
cp *.png screens
sleep 5m
