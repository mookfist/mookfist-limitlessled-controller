#!/usr/bin/env python
"""Multifader

This example will fade different groups at different speeds
simultaneously.

Usage:
    multi-fade-ver6.py [options]

Options:
    --bridge-ip=HOST    Bridge IP address
    --bridge-port=PORT  Bridge port (default 5987)
    --pause=PAUSE       Time to pause between commands in ms (default 100)
    --repeat=REPEAT     Number of times to repeat a command (default 1)
    --debug             Debug logging
"""
import logging
import threading
import time
import random
from docopt import docopt

from mookfist_lled_controller.cli import configure_logger
from mookfist_lled_controller import WifiBridge

class FadeWorker(threading.Thread):
    def __init__(self, *args, **kwargs):
        self.host = kwargs.get('host')
        self.port = int(kwargs.get('port', 5987))
        self.version = int(kwargs.get('version', 6))
        self.pause  = int(kwargs.get('pause', 100))
        self.repeat = int(kwargs.get('repeat', 1))
        self.group = int(kwargs.get('group'))
        self.fade_from = kwargs.get('fade_from', 100)
        self.fade_to   = kwargs.get('fade_to', 0)

        self.logger = logging.getLogger('lled')
        self.steps = int(kwargs.get('steps', 1))

        threading.Thread.__init__(self)

    def run(self):
        bridge = WifiBridge(self.host, self.port, self.version, self.pause, self.repeat)

        start = self.fade_from
        end   = self.fade_to

        self.logger.info('Fading group %s from %s to %s in %s steps' % (self.group, start, end, self.steps))

        if start > end:
            steps = -self.steps
        else:
            steps = self.steps

        for brightness in range(start, end, steps):
            bridge.brightness(brightness, self.group)

        bridge.brightness(end, self.group)



def main():
    arguments = docopt(__doc__)
    configure_logger(arguments['--debug'])

    log = logging.getLogger('lled')

    log.info('Welcome to the Mookfist LimitlessLED Pattern Controller')

    ip = arguments['--bridge-ip']

    if arguments['--bridge-port']:
        port = int(arguments['--bridge-port'])
    else:
        port = 5987

    if arguments['--pause']:
        pause = int(arguments['--pause'])
    else:
        pause = 100

    if arguments['--repeat']:
        delay = int(arguments['--repeat'])
    else:
        delay = 100

    workers = []

    steps = (1, 3, 5, 10)

    log.info('Fading out lights.')

    for i in range(1,4):
        worker = FadeWorker(
            host=ip,
            port=port,
            group=i,
            pause=pause,
            delay=delay,
            fade_from=100,
            fade_to=0,
            steps=steps[i-1]
        )

        worker.start()
        workers.append(worker)

    for i in range(0,3):
        workers[i].join()

    log.info('Fading in lights')

    workers = []

    for i in range(1,4):
        worker = FadeWorker(
            host=ip,
            port=port,
            group=i,
            pause=pause,
            delay=delay,
            fade_from=0,
            fade_to=100,
            steps=steps[i-1]
        )

        worker.start()
        workers.append(worker)

    for i in range(0,3):
        workers[i].join()


    log.info('end')

if __name__ == '__main__':
    main()
