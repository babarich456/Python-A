import pyautogui
import time

def autoclicker(interval, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        pyautogui.click()
        time.sleep(interval)

if __name__ == "__main__":
    interval = float(input("Her tıklama arasındaki saniye cinsinden bekleme süresini girin: "))
    duration = float(input("Autoclicker'ın kaç saniye boyunca çalışacağını girin: "))
    print("Autoclicker başlatılıyor...")
    autoclicker(interval, duration)
    print("Autoclicker durduruldu.")