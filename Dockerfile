FROM python:3.9.16-alpine3.16
WORKDIR /usr/src/app
COPY app.py ./
RUN python3 -m pip install flask
EXPOSE 5000
CMD python3 app.py
