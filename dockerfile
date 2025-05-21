FROM python:3.12.7

RUN mkdir /src
WORKDIR /src

COPY . /src

RUN curl -sSL https://install.python-poetry.org | python - \
    && ln -s /root/.local/bin/poetry /usr/bin/poetry \
    && /root/.local/bin/poetry config virtualenvs.in-project true \
    && /root/.local/bin/poetry config virtualenvs.create false \
    && /root/.local/bin/poetry self add poetry-plugin-export \
    && /root/.local/bin/poetry export --without-hashes --format=requirements.txt > requirements.txt
# \
#     && /root/.local/bin/poetry install

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# CMD tail -f /dev/null