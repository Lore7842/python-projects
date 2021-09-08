from plyer import notification
import time


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C:\\Users\\lollo\\Downloads\\clock.ico"
    )

timer = int(input('Secondi di timer: '))

time.sleep(timer)

notifyMe('Timer scaduto', 'Sono passati {} secondi'.format(timer))

