import random
import time

def generate_random_ip():
   """ Generate a random IP address from different subnets"""
   subnet = random.choice(["192.168.1", "192.168.2", "10.0.0"])
   return f"{subnet}.{random.randint(0,20)}"


def check_firewall_rules(ip, blocklist, allowlist, ip_request_count):
  """ Check if an IP is in allowlist, blacklist, or exceeds request limit"""

  if ip in allowlist:
     return "allow"
  
  if ip in blocklist:
     return "block"
  
  #Rate Limiting: if an IP Exceeds 3 requests, block it
  ip_request_count[ip] = ip_request_count.get(ip, 0) + 1
  if ip_request_count[ip] > 3:
     return "rate-limit"
  
  return "allow"


def log_request(ip, action, request_log):
   """ Log the firewall decisions"""
   timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
   log_entry = f"{timestamp} - IP: {ip}, Action: {action}"
   request_log.append(log_entry)
   print(log_entry)


def main():

   blocklist = {
     "192.168.1.1": "block", 
     "192.168.1.3": "block",  
     "192.168.1.7": "block",  
     "192.168.1.17": "block",  
     "192.168.1.9": "block",  
     "192.168.1.16": "block"   
    }
   
   allowlist = {
      "192.168.1.100": "allow"
   }

   request_log = [] #stores logs
   ip_request_count = {} # Tracks IP request frequency

   for _ in range(12):
       ip_address = generate_random_ip()
       action = check_firewall_rules(ip_address, allowlist, blocklist, ip_request_count)
       log_request(ip_address, action, request_log)



if __name__== "__main__":
    main()
