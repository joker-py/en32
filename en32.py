# -*- coding: utf-8 -*-

#!/usr/bin/env python3
from os import getenv, system
import time, asyncio
import socket, threading
from timer import Timer
timer = Timer()
from queue import Queue

def loading(arg):
 th = threading.currentThread()
 while getattr(th, "do_run", True):
  print(r'[\] LOADING')
  time.sleep(0.1)
  system('clear')
  print(r'[-] LOADING')
  time.sleep(0.1)
  system('clear')
  print(r'[/] LOADING')
  time.sleep(0.1)
  system('clear')

def main():
 print("""\033[0;35m\n""" + r"""
 |¯¯¯¯¯¯¯   |\      |   /¯¯¯¯¯\   /¯¯¯¯¯\
 |          | \     |         /         /
 |          |  \    |        /         /
 |- - -     |   \   |     - <         /
 |          |    \  |        \       /
 |          |     \ |         \     /
 |_ _ _ _   |      \|   \ _ _ /    /_ _ _
 BY J0K3R                           V1.0""", '\n')

 print('[!] WELCONE in ENTRY TO\n')
 ip = input(r'[?] ENTER ADRESS >> ')
 pf = input(r'[?] ENTER START SCAN PORT >> ')
 pt = input(r'[?] ENTER END SCAN PORT >> ')

  
 th = threading.Thread(target=loading, args=("task",))
 th.start()
 
 timer.start()
 queue = Queue()
 open_ports = []

 def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        return True
    except:
        return False

 def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

 def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            open_ports.append(port)

 port_list = range(int(pf), int(pt))
 fill_queue(port_list)

 thread_list = []
 for t in range(800):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

 for thread in thread_list:
    thread.start()

 for thread in thread_list:
    thread.join()
 timer.stop()
 th.do_run = False
 th.join()
 if not open_ports:
    print("""\033[0;35m\n""" + r"""
 	|¯¯¯¯¯¯¯   |\      |   /¯¯¯¯¯\   /¯¯¯¯¯\
 	|          | \     |         /         /
 	|          |  \    |        /         /
 	|- - -     |   \   |     - <         /
 	|          |    \  |        \       /
 	|          |     \ |         \     /
 	|_ _ _ _   |      \|   \ _ _ /    /_ _ _
 	BY J0K3R                           V1.0""", '\n')
    print(f'+----------------------------------------+------------------------------------------+-----------------+')
    print(f'│                 ADRESS:                │               OPEN PORTS:                │      TIME:      │')
    print(f'+----------------------------------------+------------------------------------------+-----------------+')
    print(f'│ %-38s | %-40s │ %-15s │' % (ip, 'NONE', timer.__time__))
    print(f'+----------------------------------------+------------------------------------------+-----------------+')
 if open_ports:
    lens = str(open_ports).lstrip('[').rstrip(']')
    print("""\033[0;35m\n""" + r"""
 	|¯¯¯¯¯¯¯   |\      |   /¯¯¯¯¯\   /¯¯¯¯¯\
 	|          | \     |         /         /
 	|          |  \    |        /         /
 	|- - -     |   \   |     - <         /
 	|          |    \  |        \       /
 	|          |     \ |         \     /
 	|_ _ _ _   |      \|   \ _ _ /    /_ _ _
 	BY J0K3R                           V1.0""", '\n')
    print(f'+----------------------------------------+-----------------------------------------+-----------------+')
    print(f'│                 ADRESS:                │               OPEN PORTS:               │      TIME:      │')
    print(f'+----------------------------------------+-----------------------------------------+-----------------+')
    print(f'│ %-38s | %-39s │ %-15s │' % (ip, lens, timer.__time__))
    print(f'+----------------------------------------+-----------------------------------------+-----------------+')
 
if __name__ == "__main__":
  main()
 
