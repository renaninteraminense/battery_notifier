import psutil
from plyer import notification
import time

battery = psutil.sensors_battery()

while True:
    percent = battery.percent

    notification.notify(
        title="Battery Percentage",
        message=str(round(percent, 2))+"% Battery remaining",
        timeout=10
    )

# After every 60 min it will show the Battery percentage
    time.sleep(60*60)
