FROM python:3.10

ADD ./ .

RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

CMD ["python", "./main.py"]