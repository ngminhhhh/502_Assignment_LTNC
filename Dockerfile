FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \          
    python3-dev \             
    swig \                    
    libxml2-dev \              
    libxslt1-dev \            
    zlib1g-dev \               
    libjpeg-dev \              
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir --timeout=120 --retries=5 -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
