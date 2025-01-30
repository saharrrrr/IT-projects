import subprocess
import speedtest
import platform

def check_internet_speed():
    try:
        print("Checking Internet Speed...")
        st = speedtest.Speedtest()
        download_speed = st.download() / 1_000_000 # Convert to Mbps
        upload_speed = st.upload() / 1_000_000 # Convert to Mbps
        print(f"Download Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")
    except Exception as e:
        print(f"failed to check internet speed: {e}")

def ping_server(server="8.8.8.8"):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ['ping', param, '4', server] #send 4 packets
    try:
        print(f"Pinging {server}...")
        output = subprocess.run(command, capture_output=True ,text=True)
        print(output.stdout)
        if output.returncode == 0:
            print(f"{server} is reachable")
        else:
            print(f"{server} is unreachable")
    except Exception as e:
        print(f"failed to ping server: {e}")


def check_network_issues():
    print("Checking Network Issues...")
    check_internet_speed()
    ping_server()

if __name__ == "__main__":
    print("Auto Network Troubleshooter")
    check_network_issues()