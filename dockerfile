FROM python:3.10

WORKDIR /app

RUN apt update
RUN apt-get install -y unzip libaio1 wget
RUN apt-get clean autoclean
RUN apt-get autoremove --yes
RUN rm -rf /var/lib/{apt,dpkg,cache,log}

# Instalação de dependências necessárias
RUN apt-get update && apt-get install -y \
    libdbus-1-dev \
    libcups2-dev \
    libgirepository1.0-dev \
    libldap2-dev libsasl2-dev \
    postgresql postgresql-contrib libpq-dev

COPY . .

RUN /bin/sh -c python -m venv /app/iury

# Instalação de pacotes Python, incluindo o psycopg2 para PostgreSQL
RUN pip install --upgrade pip && \
    pip install setuptools_scm && \
    pip install django && \
    pip install psycopg2 && \
    pip install python-decouple && \
    pip install -r requirements.txt && \
    pip install whitenoise && \
    pip install gunicorn && \
    pip install watchdog && \
    pip install psutil && \
    pip install requests && \
    pip install WeasyPrint && \
    pip install beautifulsoup4

RUN apt-get update && apt-get install -y inotify-tools

# Expondo a porta padrão do Django
EXPOSE 9000

CMD ["/bin/bash", "/app/run_all.sh"]