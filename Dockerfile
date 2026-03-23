# 1. Python 3.11 슬림 이미지 사용
FROM python:3.11-slim

# 2. 필수 시스템 패키지 설치 (네트워크 스캐닝용)
RUN apt-get update && apt-get install -y --no-install-recommends \
    tcpdump \
    libpcap-dev \
    nmap \
    && rm -rf /var/lib/apt/lists/*

# 3. 작업 디렉토리 설정
WORKDIR /app

# 4. 의존성 설치 (캐시 최적화를 위해 먼저 복사)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. 소스 코드 복사
COPY . .

# 6. 포트 설정
EXPOSE 5000

# 7. Gunicorn을 이용한 실행 (src/app.py 내의 app 객체 호출 기준)
# --bind 0.0.0.0:5000 설정을 통해 외부 접속 허용
CMD ["sh", "-c", "PYTHONPATH=src gunicorn --bind 0.0.0.0:5000 src.app:app"]