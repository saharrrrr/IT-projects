import subprocess
import speedtest
import platform

def check_internet_speed():
    try:
        print("Checking Internet Speed...")
        st = speedtest.Speedtest()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        print(f"Download Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")
        return download_speed, upload_speed  # Return speeds
    except Exception as e:
        print(f"Failed to check internet speed: {e}")
        return None, None  # Return None if speed test fails

def ping_server(server="8.8.8.8"):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ['ping', param, '4', server]  # Send 4 packets
    try:
        print(f"Pinging {server}...")
        output = subprocess.run(command, capture_output=True, text=True)
        print(output.stdout)
        if output.returncode == 0:
            print(f"{server} is reachable")
            return True  # Return True if ping is successful
        else:
            print(f"{server} is unreachable")
            return False  # Return False if ping fails
    except Exception as e:
        print(f"Failed to ping server: {e}")
        return False  # Return False if ping fails

def check_network_issues():
    print("Checking Network Issues...")

    download_speed, upload_speed = check_internet_speed()
    ping_successful = ping_server()

    print("\nTroubleshooting Suggestions:")

    if download_speed is None or upload_speed is None:
        print("- Could not determine internet speed. Check your internet connection and try again.")
    elif download_speed < 10 or upload_speed < 5:  # Example thresholds
        print("- Your internet speed is slow. Try the following:")
        print("  1. Restart your modem and router.")
        print("  2. Check for any network congestion (e.g., many devices using the internet at the same time).")
        print("  3. Contact your internet service provider (ISP).")
    else:
        print("- Your internet speed seems adequate.")

    if not ping_successful:
        print("- The ping test failed. This indicates a problem with network connectivity. Try the following:")
        print("  1. Check your network cables and connections.")
        print("  2. Restart your modem and router.")
        print("  3. Check if there are any outages in your area.")
        print("  4. Contact your ISP.")

    print("- General Suggestions:")
    print("  1. Ensure your Wi-Fi is enabled and connected to the correct network.")
    print("  2. Temporarily disable your firewall to see if it's blocking the connection (re-enable it afterward!).")
    print("  3. Run the Windows Network Troubleshooter (search for it in the Start Menu).")


if __name__ == "__main__":
    print("Auto Network Troubleshooter")
    check_network_issues()