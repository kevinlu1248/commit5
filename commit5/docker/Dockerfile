FROM python:3.10-slim-buster
RUN apt-get update && apt-get install -y git build-essential
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install torch==2.0.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install -r requirements.txt
COPY . /app
RUN python download_tokenizer.py
EXPOSE 1729
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "1729"]