FROM python:3.12


RUN mkdir app

WORKDIR /app

ENV PATH="/app/.venv/bin:${PATH}"

RUN python3 -m venv .venv

COPY . /app

RUN . .venv/bin/activate
RUN python3 -m pip install --upgrade pip
RUN pip3 install poetry
RUN poetry install
RUN chmod +x test.sh

CMD ["/bin/bash"]
