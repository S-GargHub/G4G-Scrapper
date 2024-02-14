FROM python:3

RUN mkdir -p /home/app

WORKDIR /home/app

COPY requirements.txt .

COPY modules/ ./modules/

COPY *.py .

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]

