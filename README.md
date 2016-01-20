# Config Merger

## Description
It's a litte script to write one big config file from small pieces, so you can exchange parts of the config with a special config piece for your device.

## How it works
You store your config files in one directory with the extension .conf or .<hostname>. 

At build it will take each \*.conf file and build it together, except there is a config file with your hostname as extension.

## Usage

```
usage: config-merger.py [-h] [--verbose] confd_directory output_filename

merge configs from one dir to one great config file

positional arguments:
  confd_directory  conf.d directory with configfiles
  output_filename  output config filename

optional arguments:
  -h, --help       show this help message and exit
  --verbose        print verbose output

config-merger.py ~/.config/i3/conf.d ~/.config/i3/config
```
