FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY ./slpr /code/
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y openalpr openalpr-utils libopenalpr-dev

COPY ./config/br.conf /usr/share/openalpr/runtime_data/config/
COPY ./config/lbr.traineddata /usr/share/openalpr/runtime_data/ocr/tessdata/
COPY ./config/lbr.traineddata /usr/share/openalpr/runtime_data/ocr/
COPY ./config/br.xml /usr/share/openalpr/runtime_data/region/

RUN cp -rf /usr/share/openalpr/runtime_data/ocr/tessdata/* /usr/share/openalpr/runtime_data/ocr/
