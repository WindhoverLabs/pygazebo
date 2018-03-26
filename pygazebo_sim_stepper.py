import trollius
from trollius import From

import pygazebo
import pygazebo.msg.world_control_pb2
import pygazebo.msg.world_stats_pb2

from arte_client import ArteClient
import time

# Gazebo must be started in paused mode -u command line option.
# Alternative send a pause command before stepping.

@trollius.coroutine
def publish_loop(arte_client):
    manager = yield From(pygazebo.connect(('localhost', 11345)))
    
    name_of_world = 'default'

    # Publishing the gazebo world control message
    publisher = yield From(
        manager.advertise('/gazebo/' + name_of_world + '/world_control',
                          'gazebo.msgs.WorldControl'))

    message = pygazebo.msg.world_control_pb2.WorldControl()
    message.multi_step = 2

    while True:
        arte_client.send_ready()
        arte_client.receive_response()
        yield From(publisher.publish(message))


def step_loop(arte_client):
    loop = trollius.get_event_loop()
    loop.run_until_complete(publish_loop(arte_client))


if __name__ == "__main__":
    IP, PORT = "localhost", 9999
    client = ArteClient(IP, PORT)
    time.sleep(5)
    step_loop(client)
