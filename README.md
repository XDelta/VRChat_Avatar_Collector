# VRChat_Avatar_Collector
Script used to collect/archive your currently worn public avatar from vrchat.

## Prerequisite
Python 3.8

## Install
Download the [Latest Release](https://github.com/XDelta/VRChat_Avatar_Collector/releases/latest)<br>
Unzip and navigate to the unzipped folder<br>
```bash
$ pip install -r requirements.txt
```
## Usage
Change directory to the location of the script<br>
Edit config.json with your vrchat username and password<br>
Run VRChat_Avatar_Collector.py<br>
<br>
Then every 60 seconds the script will poll vrchat api to check your current avatar,<br>
if you haven't gotten it before it will download the thumbnail and name it with the avatar id<br>

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
