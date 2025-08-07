FROM python:3.11

WORKDIR /app

# copy requirements
COPY requirements.txt ./

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# launch server
CMD ["python", "manage.py" , "runserver", "0.0.0.0:8000"]

EXPOSE 8000
