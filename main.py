import socket
import ipaddress
import math
import time
from concurrent.futures import ThreadPoolExecutor

target_ip= input("Enter target IP address: ")

try:
   ipaddress.IPv4Address(target_ip)
   print("Valid IP address")
except ValueError:
   print("Invalid IP address")
   raise SystemExit

try:
   start_port=int(input("Enter starting port: "))
   end_port=int(input("Enter ending port: "))
except ValueError:
   print("Invalid input! Please enter a number.")
   raise SystemExit

print("For the begginers, Timeout is the maximum time to wait for each connection attempt.")
try:
    timeout = float(input("Enter timeout in seconds (press Enter for recommended default 2): ") or 2)
    if timeout <= 0 or not math.isfinite(timeout):
       print("Error: Timeout must be a positive, finite number.")
       raise SystemExit
    else:
       print(f"the timeout has been set: {timeout}")
except ValueError:
   print("Invalid input! Please enter a number.")
   raise SystemExit

try:
   new_timeout = float(input("Enter the retry timeout in seconds: "))
   if new_timeout <= 0 or not math.isfinite(new_timeout):
          print("Error: Timeout must be a positive, finite number.")
          raise SystemExit
   else:
          print(f"the new timeout has been set: {new_timeout}")
except ValueError:
      print("Invalid input! Please enter a number.")
      raise SystemExit

try:
    workers = int(input("How many workers you want to check the ports? (choose between 1 - 20 workers)"))
    if workers < 1 or workers > 20:
        print("Error: You need to put between 1 - 20 workers.")
        raise SystemExit
    else:
        print(f"You have set {workers} workers")
except ValueError:
    print("Invalid input! Please enter a number.")
    raise SystemExit

if start_port > end_port:    
   print("Error: Your starting port is higher than the ending port")
elif start_port < 1 or end_port < 1:   
   print("Your port is invalid")
elif start_port > 65535 or end_port > 65535:
   print("Your port is invalid")
else:    
   print("Starting port scan...")
   start_time = time.perf_counter()
   def scan_port(target_ip, port, timeout, new_timeout):
           try:
               connection= socket.create_connection((target_ip, port), timeout=timeout)
               print(f"port {port}: OPEN")
               connection.close()
           except ConnectionRefusedError:
               print(f"Port {port}: CLOSED")
           except socket.timeout:
               try:
                  connection= socket.create_connection((target_ip, port), new_timeout)
                  print(f"port {port}: OPEN")
                  connection.close()
               except socket.timeout:
                   print("The second attempt has Timeout")
               except ConnectionRefusedError:
                   print(f"Port {port}: CLOSED")
               except OSError as error:
                              print(f"Port {port}: ERROR ({error})")
           except OSError as error:
               print(f"Port {port}: ERROR ({error})")
   with ThreadPoolExecutor(max_workers=workers) as executor:
    for port in range(start_port, end_port + 1):
        executor.submit(scan_port, target_ip, port, timeout, new_timeout)
   end_time = time.perf_counter()
   elapsed_time = end_time - start_time
   print(f"The scan was done in: {elapsed_time:.2f} seconds")