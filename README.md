# Xsummon
Calls windows of specific programs straight to you, kind of how [guake](http://guake-project.org/) works, but for any program. It's intended to be used with gestures/hot-corners/shortcuts (set in your DE settings) for your most frequent programs. If you've got better ideas let me know!



![eyyy](./demo.gif)



This works only for X server, as currently there's no Wayland alternative (with the needed features, afaik) to xdotool.



## Installation

Make sure you have the required packages:

- xdotool
- wmctrl
- python3

Optionally:

- libnotify


Then just download it, make it executable and copy it to /usr/bin/ 

```
git clone https://github.com/Haptein/xsummon && cd xsummon
chmod +x xsummon
sudo cp ./xsummon /usr/bin/
```



## Uninstall

To uninstall just delete the file.
```
sudo rm /usr/bin/xsummon
```



## Usage

```
usage: xsummon [-h] [-a ARGS] [-g] program

Call/hide a specific window.

positional arguments:
  program               name of program

optional arguments:
  -h, --help            show this help message and exit
  -a ARGS, --args ARGS  passed to program if run by xsummon, example: xsummon
                        firefox --args="--fullscreen"
  -g, --go              go to window's desktop instead of summoning it to the
                        active desktop
```
