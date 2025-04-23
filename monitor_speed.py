import speedtest
import time
from datetime import datetime

def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download = st.download() / 1_000_000  # Convert to Mbps
    upload = st.upload() / 1_000_000      # Convert to Mbps
    ping = st.results.ping
    return download, upload, ping

log_file = "log_kecepatan_internet.txt"

while True:
    try:
        download, upload, ping = test_speed()
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        hasil = f"[{waktu}] Download: {download:.2f} Mbps | Upload: {upload:.2f} Mbps | Ping: {ping:.0f} ms"
        print(hasil)

        with open(log_file, "a") as f:
            f.write(hasil + "\n")

    except Exception as e:
        print("Gagal tes kecepatan:", e)

    # Ulangi tiap 5 menit
    time.sleep(300)