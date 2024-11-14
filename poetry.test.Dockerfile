FROM python:3.12

RUN mkdir app

WORKDIR /app

ENV PATH="/app/.venv/bin:${PATH}"

RUN python3 -m venv .venv && /app/.venv/bin/python3 -m pip install --upgrade pip

COPY . /app
RUN . .venv/bin/activate && pip3 install poetry

RUN poetry install

EXPOSE 8090

RUN chmod +x ./tests/scripts/test.sh

CMD ["/bin/bash"]
