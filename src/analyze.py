import os

log_dir = "logs"
report_file = "error_report.txt"

with open(report_file, "w") as report:
    for filename in os.listdir(log_dir):
        if filename.endswith(".log"):
            with open(os.path.join(log_dir, filename)) as f:
                for line in f:
                    if "ERROR" in line or "WARNING" in line:
                        report.write(f"{filename}: {line}")
print("✅ Log analysis done. See error_report.txt")


