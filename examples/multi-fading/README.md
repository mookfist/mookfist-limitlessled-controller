Multi Fading Examples
=====================

These two examples show how you can fade different groups at different speeds.

Version 4 and version 6 bridges can handle this differently. Version 4 must
send all commands in sequence, while version 6 can send different commands
to different groups in different threads.

Usage
-----

```
$ ./multi-fade-ver4.py --bridge-ip=192.168.1.100
$ ./multi-fade-ver6.py --bridge-ip=192.168.1.101
```
