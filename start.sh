# 이미지 빌드
docker build -t ip-scanner .

# 컨테이너 실행
docker run -d \
  --name ip-scanner \
  --net=host \
  --privileged \
  ip-scanner