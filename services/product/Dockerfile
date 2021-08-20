FROM python:3.9

WORKDIR /app

ENV FLASK_APP=product.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5005

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5005

CMD ["flask", "run"]