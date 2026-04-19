import os
import re
import platform
from datetime import datetime

def measure_delay(host):
    print("\n=======================================")
    print("   ADVANCED NETWORK ANALYSIS TOOL")
    print("=======================================\n")

    print(f"Target Host : {host}")
    print(f"Start Time  : {datetime.now()}\n")

    print("Sending 5 packets...\n")

    # OS-based ping command
    if platform.system().lower() == "windows":
        cmd = f"ping -n 5 {host}"
    else:
        cmd = f"ping -c 5 {host}"

    response = os.popen(cmd).read()

    print("----------- RAW OUTPUT -----------")
    print(response)

    # Extract latency values
    times = re.findall(r'time[=<]\s?(\d+)', response)
    times = [int(t) for t in times]

    # Extract packet loss
    loss = 0
    loss_match = re.search(r'(\d+)%\s*loss', response)
    if loss_match:
        loss = int(loss_match.group(1))

    print("\n----------- ANALYSIS -----------")

    if times:
        avg_latency = sum(times) / len(times)

        # Jitter calculation
        jitter = 0
        if len(times) > 1:
            diffs = [abs(times[i] - times[i-1]) for i in range(1, len(times))]
            jitter = sum(diffs) / len(diffs)

        print(f"Latency (Avg) : {avg_latency:.2f} ms")
        print(f"Jitter        : {jitter:.2f} ms")
        print(f"Packet Loss   : {loss} %")
        print("Status        : SUCCESS ✅")
    else:
        print("Could not extract metrics ❌")

    print("\nEnd Time :", datetime.now())
    print("=======================================\n")


if __name__ == "__main__":
    host = input("Enter host (e.g., google.com): ")
    measure_delay(host)