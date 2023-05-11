FROM python:3.10-slim-buster
RUN apt-get update && apt-get install -y git
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 1729
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1729"]