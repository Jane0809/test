import RPi.GPIO as GPIO
from flask import Flask
from flask import request
import threading
import time

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def job():
    my_led_status = request.args.get('value')
    
    if my_led_status == "0":
        GPIO.output(25, GPIO.LOW)
        return 'LED_OFF'
    elif my_led_status == "1":
        GPIO.output(25, GPIO.HIGH)
        return 'LED_ON'
    else:
        while 7 == 7:
            GPIO.output(25, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(25, GPIO.LOW)
            time.sleep(1)
        return 'LED_string'
    return my_led_status

t = threading.Thread(target = job)

t.start()

for i in range(3):
    print("Main thread:",i)
    time.sleep(1)
    
t.join()

print("Done.")



if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)
    app.run()
