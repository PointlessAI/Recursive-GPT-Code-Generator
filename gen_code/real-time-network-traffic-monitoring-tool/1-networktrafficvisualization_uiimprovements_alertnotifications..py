```python
import tkinter as tk
import random

def update_traffic():
    # Simulating network traffic data
    received = random.randint(0, 100)
    transmitted = random.randint(0, 100)
    label_received.config(text=f"Received: {received} KB/s")
    label_transmitted.config(text=f"Transmitted: {transmitted} KB/s")
    root.after(1000, update_traffic)

root = tk.Tk()
root.title("Real-Time Network Traffic Monitoring Tool")

label_received = tk.Label(root, font=('Helvetica', 16))
label_received.pack()

label_transmitted = tk.Label(root, font=('Helvetica', 16))
label_transmitted.pack()

update_traffic()

root.mainloop()
```
