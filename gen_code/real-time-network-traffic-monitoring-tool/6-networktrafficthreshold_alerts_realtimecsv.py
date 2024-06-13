import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import ttk
import time
import psutil
import threading
import csv

received_data = []
transmitted_data = []
time_points = []
threshold = 1000  # default threshold value

def check_threshold(traffic):
    if traffic > threshold:
        print(f"Alert: Network traffic ({traffic:.2f} KB/s) exceeds set threshold of {threshold} KB/s")

def update_traffic():
    network_stats = psutil.net_io_counters()
    received = network_stats.bytes_recv / 1024
    transmitted = network_stats.bytes_sent / 1024

    received_data.append(received)
    transmitted_data.append(transmitted)
    time_points.append(time.strftime('%H:%M:%S'))

    label_received.config(text=f"Received: {received:.2f} KB/s")
    label_transmitted.config(text=f"Transmitted: {transmitted:.2f} KB/s")

    check_threshold(received)
    check_threshold(transmitted)

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

def save_data():
    with open('network_traffic_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time', 'Received (KB/s)', 'Transmitted (KB/s)'])
        for i in range(len(time_points)):
            writer.writerow([time_points[i], received_data[i], transmitted_data[i]])

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

# Adding feature to enter threshold value
threshold_entry = tk.Entry(root)
threshold_entry.insert(0, str(threshold))
threshold_entry.pack()

def set_threshold():
    global threshold
    threshold = float(threshold_entry.get())

threshold_button = tk.Button(root, text="Set Threshold", command=set_threshold)
threshold_button.pack()

save_button = tk.Button(root, text="Save Data", command=save_data)
save_button.pack()

# Creating a separate thread for monitoring network traffic continuously
monitor_thread = threading.Thread(target=monitor_traffic)
monitor_thread.daemon = True
monitor_thread.start()

root.mainloop()
