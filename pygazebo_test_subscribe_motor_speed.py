import trollius
from trollius import From

import pygazebo
import pygazebo.msg.MotorSpeed_pb2

def callback(data):
    message = pygazebo.msg.MotorSpeed_pb2.MotorSpeed.FromString(data)
    print('Received message:', message.motor_speed)

@trollius.coroutine
def subscribe_loop():
    manager = yield From(pygazebo.connect(('localhost', 11345)))

    subscriber = manager.subscribe('/gazebo/default/typhoon_h480/motor_speed/0',
                      'mav_msgs.msgs.MotorSpeed',
                      callback)

    while True:
        yield From(trollius.sleep(1.0))


def listen_loop():
    loop = trollius.get_event_loop()
    loop.run_until_complete(subscribe_loop())


if __name__ == "__main__":
    listen_loop()
