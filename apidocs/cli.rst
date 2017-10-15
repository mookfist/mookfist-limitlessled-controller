.. CLI documentation

Command Line Interface
======================

The lled.py script allows you to control your lights from the command line.

Usage
-----

First scan for available bridges:

    | $ ./lled.py scan --bridge-version=4
    | 0:00:00.000130 [INFO    ] Welcome to the Mookfist LimitlessLED Controller
    | 0:00:00.000231 [INFO    ] Scanning for bridge...
    | 0:00:05.473138 [INFO    ] Found 1 bridge(s)
    | 0:00:05.473543 [INFO    ] --- Bridge Details
    | 0:00:05.473964 [INFO    ] Version: 4
    | 0:00:05.474373 [INFO    ] IP: 192.168.1.181

You can then use the IP address of the bridge for other commands. For example, to change the color of all groups you can do:

    $ ./lled.py color 255 --bridge-ip=192.168.1.181 --bridge-version=4 --group all

While it's faster to provide the IP address, you can omit it. lled.py will
for the first available bridge it can find and use that.


Commands
--------

+---------------------+--------------------------------------------------------+
| Command             | Description                                            |
+---------------------+--------------------------------------------------------+
| fade <start> <end>  | Fade brightness from <start> to <end>. Valus can be    |
|                     | between 0 and 100                                      |
+---------------------+--------------------------------------------------------+
| facec <start> <end> | Fade color from <start> to <end>. Values can be between|
|                     | 0 and 255                                              |
+---------------------+--------------------------------------------------------+
| color <color>       | Set color to <color>. Values can be between 0 and 255  |
+---------------------+--------------------------------------------------------+
| brightness <value>  | Set brightness to <value>, between 0 and 100           |
+---------------------+--------------------------------------------------------+
| on                  | Turn on a group of lights                              |
+---------------------+--------------------------------------------------------+
| off                 | Turn off a group of lights                             |
+---------------------+--------------------------------------------------------+
| rgb <r> <b> <g>     | Set color of lights using RGB values, each between     |
|                     | 0 and 100                                              |
+---------------------+--------------------------------------------------------+
| scan                | Scan for available bridges                             |
+---------------------+--------------------------------------------------------+

Options
-------

+---------------------+--------------------------------------------------------+
| Argument            | Description                                            |
+---------------------+--------------------------------------------------------+
| --repeat            | Number of times to repeat a command.                   |
+---------------------+--------------------------------------------------------+
| --pause             | Number of milliseconds to pause between sending        |
|                     | commands.                                              |
+---------------------+--------------------------------------------------------+
| --group             | Group number. Repease the argument for each command you|
|                     | want to send the command to. Use 'all' for all groups  |
+---------------------+--------------------------------------------------------+
| --debug             | turn on debug logging                                  |
+---------------------+--------------------------------------------------------+
| --bridge-ip         | IP or hostname of the bridge                           |
+---------------------+--------------------------------------------------------+
| --bridge-port       | Bridge port. Leave blank for default.                  |
+---------------------+--------------------------------------------------------+
| --bridge-version    | Bridge version. Supported versions are 4, 5 and 6      |
+---------------------+--------------------------------------------------------+

Examples
--------

Fade group 1 to 0% brightness

    $ ./lled.py fade 100 0 --group -1

Set color to groups 1 and 2

    $ ./lled.py color 128 -g 1 -g 2

Set brightness to 50% for group 3

    $ ./lled.py brightness 50 -g 3


