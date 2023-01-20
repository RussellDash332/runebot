FROM python:3.10

ADD ./ .

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]