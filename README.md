# Mookfist LimitlessLED Controller v0.0.1

Intended as a simple wrapper around the LimitlessLED wifi protocol written in python.

Currently only supports version 4 (and possibly version 5) but is designed to support multiple versions.

There are some differences from the original LimitlessLED protocol:

1. Brightness is a percentage between 0 and 100. LimitlessLED protocol's brightness ranges from 2 to 27
2. Color is a value between 0 and 255 and starts and ends with the color red. LimitlesLED protocol's color starts from blue

## Installation

Download the code: https://github.com/mookfist/mookfist-limitlessled-controller/archive/master.zip

```
$ unzip master.zip
$ python setup.py install
$ python lled.py --help
```

## Commands
| Command | Description |
| ------- | ----------- |
| fade <start> <end>   | Fade brightness from <start> to <end>. Values can be between 0 and 100 |
| fadec <start> <end> | Fade the color from <start> to <end>. Values can be between 0 and 255 |
| color <color> | Set color to <color>. Value can be between 0 and 255 |
| brightness <brightness> | Set the brightness to <brightness>. Value can be between 0 and 255 |


## Options
| Argument | Description | Default Value |
| -------- | ----------- | ------------- |
| --repeat-count | Number of times to repeat a command. Increasing this value could improve smoothness, but means it will take a longer time to perform fades | 1 |
| --pause  | Number of milliseconds to pause between sending commands. Decreasing this value below 100ms might mean some commands are not processed | 100 |
| --group  | Group number. Repeat the argument for each group you want to send a command to | n/a |
| --debug  | Turn on debug logging | false |
| --host   | The IP/hostname of the bridge. If omitted the bridge will be automatically scanned down | n/a |
| --port   | The port number of the bridge. | 8899 |
| --version | The version of the LimitlessLED protocol | 4 |


## Examples


Fade light group 1 to 0% brightness

```
python lled.py fade 100 0 --group 1
```

Set color to groups 1 and 2
```
python lled.py color 128 --group 1 --group 2
```

