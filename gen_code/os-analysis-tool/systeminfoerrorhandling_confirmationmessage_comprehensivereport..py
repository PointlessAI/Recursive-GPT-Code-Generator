import psutil
import platform
import tkinter as tk
from tkinter import messagebox
import os

def display_analysis():
    try:
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
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while retrieving system information: {str(e)}")

def generate_report(file_format):
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        network = psutil.net_io_counters()

        if os.path.exists(f"report.{file_format.lower()}"):
            overwrite = messagebox.askyesno("File Exists", "Report file already exists. Do you want to overwrite it?")
            if not overwrite:
                return

        with open(f"report.{file_format.lower()}", 'w') as f:
            f.write(f"CPU Usage: {cpu_usage}%\n"
                    f"Memory Usage: {memory.percent}%\n"
                    f"Disk Usage: {disk.percent}%\n"
                    f"Total Network Bytes Sent: {network.bytes_sent}\n"
                    f"Total Network Bytes Received: {network.bytes_recv}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while writing to the file: {str(e)}")

def clear_reports():
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to clear the reports?")
    if confirmation:
        if os.path.exists("report.pdf"):
            os.remove("report.pdf")
        if os.path.exists("report.csv"):
            os.remove("report.csv")
        messagebox.showinfo("Reports Cleared", "Existing report files have been cleared.")

def main():
    root = tk.Tk()
    root.title("OS Analysis Tool")

    button_analyze = tk.Button(root, text="Display Analysis", command=display_analysis)
    button_analyze.pack(pady=20)

    button_report_pdf = tk.Button(root, text="Generate PDF Report", command=lambda: generate_report('PDF'))
    button_report_pdf.pack(pady=10)

    button_report_csv = tk.Button(root, text="Generate CSV Report", command=lambda: generate_report('CSV'))
    button_report_csv.pack(pady=10)

    button_clear_reports = tk.Button(root, text="Clear Reports", command=clear_reports)
    button_clear_reports.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
