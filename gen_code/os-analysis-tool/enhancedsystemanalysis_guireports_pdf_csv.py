import psutil
import platform
import tkinter as tk
from tkinter import messagebox

def display_analysis():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    network = psutil.net_io_counters()

    messagebox.showinfo("System Analysis",
                        f"CPU Usage: {cpu_usage}%\n"
                        f"Memory Usage: {memory.percent}%\n"
                        f"Disk Usage: {disk.percent}%\n"
                        f"Total Network Bytes Sent: {network.bytes_sent}\n"
                        f"Total Network Bytes Received: {network.bytes_recv}")

def generate_report(file_format):
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    network = psutil.net_io_counters()

    if file_format == 'PDF':
        with open('report.pdf', 'w') as f:
            f.write(f"CPU Usage: {cpu_usage}%\n"
                    f"Memory Usage: {memory.percent}%\n"
                    f"Disk Usage: {disk.percent}%\n"
                    f"Total Network Bytes Sent: {network.bytes_sent}\n"
                    f"Total Network Bytes Received: {network.bytes_recv}")
    elif file_format == 'CSV':
        with open('report.csv', 'w') as f:
            f.write("Category, Usage\n"
                    f"CPU, {cpu_usage}\n"
                    f"Memory, {memory.percent}\n"
                    f"Disk, {disk.percent}\n"
                    f"Network Sent, {network.bytes_sent}\n"
                    f"Network Received, {network.bytes_recv}")

def main():
    root = tk.Tk()
    root.title("OS Analysis Tool")

    button_analyze = tk.Button(root, text="Display Analysis", command=display_analysis)
    button_analyze.pack(pady=20)

    button_report_pdf = tk.Button(root, text="Generate PDF Report", command=lambda: generate_report('PDF'))
    button_report_pdf.pack(pady=10)

    button_report_csv = tk.Button(root, text="Generate CSV Report", command=lambda: generate_report('CSV'))
    button_report_csv.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
