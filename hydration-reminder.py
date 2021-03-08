from plyer import notification
import time


def hydration_reminder(title, message):
    notification.notify(
        title = title,
        message = message,
        timeout=10,
    )


if __name__ == '__main__':
    while True:
        hydration_reminder("Remember to stay hydrated!", "Take a break and drink some water.")
        time.sleep(10800)
