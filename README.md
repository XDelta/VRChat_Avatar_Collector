# VRChat_Avatar_Collector
Script used to collect/archive your currently worn public avatar from vrchat.

## Install
```bash
$ pip install -r requirements.txt
```
## Usage
Change directory to the location of the script
Edit config.json with your vrchat username and password
Run VRChat_Avatar_Collector.py

Then every 60 seconds the script will poll vrchat api to check your current avatar,
if you haven't gotten it before it will download the thumbnail and name it with the avatar id

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0
International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg