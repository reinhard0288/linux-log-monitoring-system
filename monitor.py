print("Linux Server LOG MONITORING STARTED")
log_file = "sample_log.txt"
with open (log_file,"r") as file:
    lines = file.readlines()
failed_attempts = 0
for line in lines:
    if "Failed password" in line:
        failed_attempts += 1
    print(f"Total Failed Login Attempts: {failed_attempts}")
    if failed_attempts > 2:
        print("ALERT: Suspicious Activity Detected!")
    with open("report.txt", "w") as report:
        report.write(f"Failed Login Attempts: {failed_attempts}\n")
        if failed_attempts > 2:
            report.write("ALERT: Suspicious Activity Detected!\n")
    print("Report saved in report.txt")