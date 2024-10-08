FROM python:3.11-slim

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

ENV APP_HOME=/app
WORKDIR $APP_HOME
COPY . ./
# COPY data/ /app/data/

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]