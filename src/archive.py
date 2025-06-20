import tarfile
import time

timestamp = time.strftime("%Y%m%d-%H%M%S")
archive_name = f"logs_{timestamp}.tar.gz"

with tarfile.open(archive_name, "w:gz") as tar:
    tar.add("logs")
print(f"✅ Logs archived as {archive_name}")