import tkinter as tk
import random
import matplotlib.pyplot as plt

received_data = []
transmitted_data = []
time_points = []

def update_traffic():
    received = random.randint(0, 100)
    transmitted = random.randint(0, 100)
    
    received_data.append(received)
    transmitted_data.append(transmitted)
    time_points.append(len(received_data))
    
    label_received.config(text=f"Received: {received} KB/s")
    label_transmitted.config(text=f"Transmitted: {transmitted} KB/s")
    
    plt.figure(figsize=(10, 5))
    plt.plot(time_points, received_data, label='Received', color='blue')
    plt.plot(time_points, transmitted_data, label='Transmitted', color='orange')
    plt.xlabel('Time')
    plt.ylabel('Traffic (KB/s)')
    plt.legend()
    plt.show()

    root.after(1000, update_traffic)

root = tk.Tk()
root.title("Real-Time Network Traffic Monitoring Tool")

label_received = tk.Label(root, font=('Helvetica', 16))
label_received.pack()

label_transmitted = tk.Label(root, font=('Helvetica', 16))
label_transmitted.pack()

update_traffic()

root.mainloop()
