# Config Merger

## Description
It's a litte script to write one big config file from small pieces, so you can exchange parts of the config with a special config piece for your device.

## How it works
You store your config files in one directory with the extension .conf or .<hostname>. 

At build it will take each \*.conf file and build it together, except there is a config file with your hostname as extension.

## Usage

```
Config Merger
    -d directory with input files
    -o output config file

./config-merger.sh -d ~/.config/i3/conf.d -o ~/.config/i3/config
```
