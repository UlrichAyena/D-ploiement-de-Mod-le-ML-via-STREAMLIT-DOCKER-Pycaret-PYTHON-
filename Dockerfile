
FROM python:3.11.5

WORKDIR /app

ADD . /app

RUN apt-get update && apt-get install -y libgomp1

RUN pip install -r requirements.txt

EXPOSE 1664

CMD streamlit run --server.port 1664 streamlit3_Ulrich.py
