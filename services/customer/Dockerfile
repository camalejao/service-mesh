FROM python:3.9

WORKDIR /app

ENV FLASK_APP=customer.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["flask", "run"]