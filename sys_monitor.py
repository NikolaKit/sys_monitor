import time
import psutil
from win10toast import ToastNotifier

# Initialize Windows Toast Notifier
toaster = ToastNotifier()


def send_alert(title, message):
    # threaded=True allows the script to continue running without blocking
    toaster.show_toast(title, message, duration=3, threaded=True)


def check_system_resources():
    cpu_usage = psutil.cpu_percent(interval=1)

    ram_info = psutil.virtual_memory()
    ram_usage = ram_info.percent
    ram_used_gb = round(ram_info.used / (1024**3), 2)
    ram_total_gb = round(ram_info.total / (1024**3), 2)

    print("--- SYSTEM STATUS ---")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"RAM Usage: {ram_usage}% ({ram_used_gb} GB / {ram_total_gb} GB)")

    # Send notification if CPU usage exceeds threshold
    if cpu_usage > 80:
        print("HIGH CPU USAGE DETECTED!")
        send_alert("High CPU Usage!", f"CPU load is at {cpu_usage}%!")

    # Send notification if RAM usage exceeds threshold
    if ram_usage > 85:
        print("HIGH RAM USAGE DETECTED!")
        send_alert("High RAM Usage!", f"RAM load is at {ram_usage}%!")


if __name__ == "__main__":
    print("Starting PC System Monitor... Press Ctrl+C to stop.\n")
    try:
        while True:
            check_system_resources()
            print("-" * 25)
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")