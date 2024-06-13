import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import ttk
import time
import psutil
import threading

received_data = []
transmitted_data = []
time_points = []

def update_traffic():
    network_stats = psutil.net_io_counters()
    received = network_stats.bytes_recv / 1024
    transmitted = network_stats.bytes_sent / 1024

    received_data.append(received)
    transmitted_data.append(transmitted)
    time_points.append(time.strftime('%H:%M:%S'))

    label_received.config(text=f"Received: {received:.2f} KB/s")
    label_transmitted.config(text=f"Transmitted: {transmitted:.2f} KB/s")
    
    treeview.insert("", "end", values=(time.strftime('%H:%M:%S'), received, transmitted))

    plt.clf()
    plt.figure(figsize=(6, 4))
    plt.plot(time_points, received_data, label='Received', color='blue')
    plt.plot(time_points, transmitted_data, label='Transmitted', color='orange')
    plt.xlabel('Time')
    plt.ylabel('Traffic (KB/s)')
    plt.legend()
    plt.draw()

    root.after(1000, update_traffic)

def monitor_traffic():
    while True:
        update_traffic()
        time.sleep(1)

root = tk.Tk()
root.title("Real-Time Network Traffic Monitoring Tool")

label_received = tk.Label(root, font=('Helvetica', 16))
label_received.pack()

label_transmitted = tk.Label(root, font=('Helvetica', 16))
label_transmitted.pack()

columns = ('Time', 'Received (KB/s)', 'Transmitted (KB/s)')
treeview = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    treeview.heading(col, text=col)
treeview.pack()

# Creating a separate thread for monitoring network traffic continuously
monitor_thread = threading.Thread(target=monitor_traffic)
monitor_thread.daemon = True
monitor_thread.start()

root.mainloop()
