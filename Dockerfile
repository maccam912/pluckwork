FROM python:3.12

RUN curl -sSL https://pdm-project.org/install-pdm.py | python3 -

WORKDIR /app
COPY . .
RUN /root/.local/bin/pdm install -G:all
RUN /root/.local/bin/pdm run alembic upgrade head
EXPOSE 8080
CMD /root/.local/bin/pdm run serve
