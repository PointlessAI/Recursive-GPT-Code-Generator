import tkinter as tk
import random
import matplotlib.pyplot as plt
from tkinter import ttk
import time

received_data = []
transmitted_data = []
time_points = []

def update_traffic():
    received = random.randint(0, 100)
    transmitted = random.randint(0, 100)
    
    received_data.append(received)
    transmitted_data.append(transmitted)
    time_point = len(received_data)
    
    label_received.config(text=f"Received: {received} KB/s")
    label_transmitted.config(text=f"Transmitted: {transmitted} KB/s")
    
    treeview.insert("", "end", values=(time.strftime('%H:%M:%S'), received, transmitted))
    
    plt.figure(figsize=(6, 4))
    plt.plot(time_points, received_data, label='Received', color='blue')
    plt.plot(time_points, transmitted_data, label='Transmitted', color='orange')
    plt.xlabel('Time')
    plt.ylabel('Traffic (KB/s)')
    plt.legend()
    
    plt.pause(0.1)

    root.after(1000, update_traffic)

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

update_traffic()

root.mainloop()
