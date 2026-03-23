FROM python:3.11-slim

# 네트워크 스캔에 필요한 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    tcpdump \
    libpcap-dev \
    nmap \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
# Flask 실행 (Gunicorn 사용 권장)
CMD ["python", "src/app.py"]