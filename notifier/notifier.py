from plyer import notification
import time


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C:\\Users\\lollo\\Downloads\\clock.ico",
        timeout=0.5
    )


if __name__ == '__main__':
    while True:
        notifyMe('Hei, fai una pausa!',
                 'Se vuoi ottimizzare la tua produttività, fai una pausa ora!')
        time.sleep(1)
