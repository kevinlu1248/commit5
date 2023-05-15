FROM python:3.10-slim-buster
RUN apt-get update && apt-get install -y git
RUN pip install chromadb==0.3.22 torch==2.0.1+cpu transformers==4.28.0.dev0
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN python scripts/download_tokenizer.py
EXPOSE 1729
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1729"]