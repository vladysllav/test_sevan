FROM python:3.7
WORKDIR /code
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP server.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
