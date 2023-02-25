FROM python:3.8
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN sh -c python manage.py makemigrations
COPY . .
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]