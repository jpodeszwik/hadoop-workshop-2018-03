#!/usr/bin/env python2

from time import sleep
from datetime import datetime, timedelta
import fileinput
import random
import socket
import sys

accounts = [line.strip() for line in fileinput.input('accounts')]
host = sys.argv[1]
port = int(sys.argv[2])
minus_days = int(sys.argv[3]) if len(sys.argv) >= 4 else 0

def generate_random_transfer():
    src = random.choice(accounts)
    dst = random.choice(accounts)
    
    amount = random.randint(1, 1000000)

    date = (datetime.today() - timedelta(days=minus_days)).isoformat(' ')

    return '{},{},{},{}\n'.format(src, dst, amount, date)

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send(generate_random_transfer())
        s.close()
    except Exception as e:
        print(e)

    sleep(1)
