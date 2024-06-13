import tkinter as tk
import scapy.all as scapy

def capture_packets():
    packets = scapy.sniff(count=10)  # Capture 10 packets as an example
    for packet in packets:
        print(packet.summary())  # Display summarized packet details

def filter_packets(source_ip=None, destination_ip=None, protocol=None):
    packets = scapy.sniff(filter=f"src {source_ip} and dst {destination_ip} and proto {protocol}", count=10)
    for packet in packets:
        print(packet.summary())

def start_capture():
    capture_packets()

def filter_capture():
    source_ip = source_ip_entry.get()
    destination_ip = destination_ip_entry.get()
    protocol = protocol_entry.get()
    filter_packets(source_ip=source_ip, destination_ip=destination_ip, protocol=protocol)

root = tk.Tk()
root.title("Network Traffic Scanner")

capture_button = tk.Button(root, text="Capture Packets", command=start_capture)
capture_button.pack()

source_ip_label = tk.Label(root, text="Source IP:")
source_ip_label.pack()
source_ip_entry = tk.Entry(root)
source_ip_entry.pack()

destination_ip_label = tk.Label(root, text="Destination IP:")
destination_ip_label.pack()
destination_ip_entry = tk.Entry(root)
destination_ip_entry.pack()

protocol_label = tk.Label(root, text="Protocol:")
protocol_label.pack()
protocol_entry = tk.Entry(root)
protocol_entry.pack()

filter_button = tk.Button(root, text="Filter Packets", command=filter_capture)
filter_button.pack()

root.mainloop()
