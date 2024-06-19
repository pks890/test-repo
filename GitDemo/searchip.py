import json
import ipaddress

file_path = "testip.json"

def load_data():
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def find_matching_cidr(ip, data):
    ip_addr = ipaddress.ip_address(ip)
    for item in data:
        network = ipaddress.ip_network(item["cidr"])
        if ip_addr in network:
            return item
    return None

# Load data from the JSON file
data = load_data()

# IP address to check
ip_to_check = (input("enter the valid ip address to serach: "))

# Find and print the matching CIDR entry
matching_entry = find_matching_cidr(ip_to_check, data)
if matching_entry:
    print(matching_entry)
else:
    print(f"The IP address {ip_to_check} is NOT within any of the CIDR ranges.")
