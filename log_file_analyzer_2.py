# Log File Analyzer for Suspicious Activity

# Dictionary to store failed attempts
failed_attempts = {}

# Open log file
with open("sample.log", "r") as file:
    for line in file:
        if "Failed login" in line:
            # Extract IP address (last word in line)
            ip = line.strip().split()[-1]
            
            # Count failed attempts
            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

print("🔍 Log Analysis Report\n")

# Check for suspicious IPs (3 or more failed attempts)
for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"⚠ Suspicious IP Detected: {ip} - {count} Failed Attempts")