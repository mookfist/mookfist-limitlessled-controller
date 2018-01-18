#!/usr/bin/env python
"""Multifader Version 4

This example will fade different groups at different speeds.

Warning: There is no easy way to do this with version 4 bridges due to
limitations of its protocol. You must first issue a command to switch to a
group, then issue a separate command to perform an action on that group. As
such, to fade multiple groups at different rates, you must prepare a list of
commands like so:

1. switch to group 1
2. set brightness to 100
3. switch to group 2
4. set brightness to 100
5. switch to group 1
6. set brightness to 99
7. switch to group 1
8. set brightness to 99

Because of this pattern, fading different groups at different rates is not
always going to be smooth. You can use the 'all' group to fade all groups
simultaneously at the same speed.

Version 6 bridges do not have this limitation.

Usage:
    multi-fade-ver4.py [options]

Options:
    --bridge-ip=HOST    Bridge IP address
    --bridge-port=PORT  Bridge port (default 5987)
    --pause=PAUSE       Time to pause between commands in ms (default 100)
    --repeat=REPEAT     Number of times to repeat a command (default 1)
    --debug             Debug logging
"""
import logging
from docopt import docopt

from mookfist_lled_controller.cli import configure_logger
from mookfist_lled_controller import create_bridge

try:
    from itertools import izip_longest as zip_longest
except ImportError:
    from itertools import zip_longest


def main():
    arguments = docopt(__doc__)
    configure_logger(arguments['--debug'])

    log = logging.getLogger('lled')

    ip = arguments['--bridge-ip']

    if arguments['--bridge-port']:
        port = int(arguments['--bridge-port'])
    else:
        port = 8899

    if arguments['--pause']:
        pause = int(arguments['--pause'])
    else:
        pause = 100

    if arguments['--repeat']:
        repeat = int(arguments['--repeat'])
    else:
        repeat = 1


    group_cmds = (range(100,0,-1), range(100,0,3), range(100,0,5), range(100,0,10))

    fade_out_commands = zip_longest(range(100,0,-1), range(100,0,-3), range(100,0,-5), range(100,0,-10))
    fade_in_commands = zip_longest(range(0,100,1), range(0,100,3), range(0,100,5), range(0,100,10))

    bridge = create_bridge(4, ip, port, pause=pause, repeat=repeat)

    for cmd in fade_out_commands:
        for group in range(1,4):
            if (cmd[group-1] != None):
                bridge.brightness(cmd[group-1], group)

    for cmd in fade_in_commands:
        for group in range(1,4):
            if (cmd[group-1] != None):
                bridge.brightness(cmd[group-1], group)

    log.info('end')

if __name__ == '__main__':
    main()
