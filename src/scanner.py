import ipaddress
from scapy.all import ARP, Ether, srp
import logging

# Scapy 로그 레벨을 DEBUG로 설정 (패킷 송수신 상세 정보 출력)
logging.getLogger("scapy.runtime").setLevel(logging.DEBUG)

def ip_scan(network_cidr="10.100.0.0/24"):
    """
    ARP 요청을 보내 네트워크 내에 응답하는 장비가 있는지 체크합니다.
    """

    print(f"\n[START] Scanning network: {network_cidr}", flush=True)
    
    try:
        # 1. ARP 패킷 생성 (누구 10.100.0.x 있니? 라고 묻는 패킷)
        # Ether는 목적지 주소를 브로드캐스트(모두에게)로 설정합니다.
        ans, unans = srp(
            Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=network_cidr), 
            timeout=5,      # 응답을 기다릴 시간 (초)
            verbose=False,  # 진행 과정을 터미널에 뿌리지 않음
            inter=0.005,       # 패킷 간 간격 (네트워크 부하 방지)
            retry=2
        )

        # 2. 응답이 온 패킷에서 IP 주소만 추출하여 리스트로 만듦
        active_hosts = [received.psrc for sent, received in ans]
        
        # 중복 제거 및 정렬
        return sorted(active_hosts)

    except Exception as e:
        print(f"Scan Error: {e}", flush=True)
        return []

def get_network_status(network_cidr="10.100.0.0/24"):

    """
    입력된 CIDR 범위 내의 모든 IP에 대해 활성화 여부를 반환합니다.
    network_cidr: "10.100.0.0/24" 형태
    active_hosts: nmap에서 검출된 실시간 IP 리스트 (Set 권장)
    """

    try:
        network = ipaddress.ip_network(network_cidr)
        active_set = set(ip_scan()) 

        status_list = []
        for ip in network.hosts():

            str_ip = str(ip)
            status_list.append({
                "ip": str_ip,
                "is_active": str_ip in active_set
            })

        return {
            "network": network_cidr,
            "active_count": len(active_set),
            "total_count": len(status_list),
            "data": status_list
        }

    except ValueError as e:
        print(f"Invalid CIDR: {e}")
        return []