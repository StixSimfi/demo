FROM python:3.12-alpine

RUN mkdir app

WORKDIR /app

RUN python3 -m venv .venv && /app/.venv/bin/python3 -m pip install --upgrade pip

COPY . /app
RUN source /app/.venv/bin/activate && pip3 install --no-cache-dir -r /app/requirements.txt

ENV PATH="/app/.venv/bin:${PATH}"

EXPOSE 8000

CMD ["python3"]

