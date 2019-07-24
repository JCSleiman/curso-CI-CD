FROM python:3.7-alpine
WORKDIR /var/www/
COPY . .
RUN pip3 install Flask==1.0
EXPOSE 5000
CMD ["python3", "app.py"]
