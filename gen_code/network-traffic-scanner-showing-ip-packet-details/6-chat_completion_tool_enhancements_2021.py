import tkinter as tk
import scapy.all as scapy

def capture_packets():
    packets = scapy.sniff(count=10)
    print_output([str(packet) for packet in packets])

def filter_packets(source_ip=None, destination_ip=None, protocol=None):
    filter_str = ""
    if source_ip:
        filter_str += f"src {source_ip} and "
    if destination_ip:
        filter_str += f"dst {destination_ip} and "
    if protocol:
        filter_str += f"proto {protocol}"

    packets = scapy.sniff(filter=filter_str, count=10)
    print_output([str(packet) for packet in packets])

def start_capture():
    capture_packets()

def filter_capture():
    source_ip = source_ip_entry.get()
    destination_ip = destination_ip_entry.get()
    protocol = protocol_entry.get()
    filter_packets(source_ip, destination_ip, protocol)

def clear_output():
    output_text.delete('1.0', tk.END)

def print_output(content):
    output_text.configure(state='normal')    
    for line in content:
        output_text.insert(tk.END, line + '\n')
    output_text.configure(state='disabled')

root = tk.Tk()
root.title("Network Traffic Scanner")

capture_button = tk.Button(root, text="Capture Packets", command=lambda: [clear_output(), start_capture()])
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

output_text = tk.Text(root, height=10, width=50)
output_text.pack()

root.mainloop()
