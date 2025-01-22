FROM python:3.10-alpine

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 4000

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:4000" ]