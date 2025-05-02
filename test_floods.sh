#!/bin/bash

echo "=== SniffGuard Flood Test Script ==="
echo "Make sure your SniffGuard is running on the 'lo' interface!"
echo "This will perform ICMP, SYN, and UDP flood locally on 127.0.0.1"
echo "====================================="
sleep 2

# ICMP Flood
echo "[1/3] Launching ICMP flood using ping..."
ping -f 127.0.0.1 -c 500 &
PING_PID=$!
sleep 3
kill $PING_PID

# SYN Flood
echo "[2/3] Launching SYN flood using hping3..."
sudo hping3 -S 127.0.0.1 -p 80 --flood --count 1000 &
SYN_PID=$!
sleep 3
kill $SYN_PID

# UDP Flood
echo "[3/3] Launching UDP flood using hping3..."
sudo hping3 --udp -p 53 127.0.0.1 --flood --count 1000 &
UDP_PID=$!
sleep 3
kill $UDP_PID

echo "=== All flood tests completed ==="
