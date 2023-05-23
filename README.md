# chatgpt-api

# Docker image

The docker image provides a suitable environment to run the contained python scripts.
The scripts can also be run outside docker if the host is setup correctly.

## Building the docker container

With docker installed run the script `docker-build.sh`

## Running in the image.

Use the script `api-development.sh` to launch the docker container. Scripts and files in the `workspace` directory are available in the container at `/workspace`.

## Docker image tools

* figlet is available in the docker image.

# Scripts

`cd` to  the workspace shared between the host and the docker container.

```
cd /workspace
```

Run `chs-chat.py` to run the Cheltenham Hackspace HackBot.

```
./chs-chat.py
```

This will run the `clone_wiki.py` 
script to get the latest copy of the Cheltenham Hackspace wiki to the `/workspace/the_space_wiki directory`.

```
===============================================================================
  ____ _          _ _             _                     
 / ___| |__   ___| | |_ ___ _ __ | |__   __ _ _ __ ___  
| |   | '_ \ / _ \ | __/ _ \ '_ \| '_ \ / _` | '_ ` _ \    
| |___| | | |  __/ | ||  __/ | | | | | | (_| | | | | | |
 \____|_| |_|\___|_|\__\___|_| |_|_| |_|\__,_|_| |_| |_|
 _   _            _                             
| | | | __ _  ___| | _____ _ __   __ _  ___ ___ 
| |_| |/ _` |/ __| |/ / __| '_ \ / _` |/ __/ _ \    
|  _  | (_| | (__|   <\__ \ |_) | (_| | (_|  __/
|_| |_|\__,_|\___|_|\_\___/ .__/ \__,_|\___\___|
                          |_|                   
 _   _            _    ____        _   
| | | | __ _  ___| | _| __ )  ___ | |_ 
| |_| |/ _` |/ __| |/ /  _ \ / _ \| __|
|  _  | (_| | (__|   <| |_) | (_) | |_ 
|_| |_|\__,_|\___|_|\_\____/ \___/ \__|
===============================================================================

> git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
> git pull
Already up to date.
READY
INPUT: 
```

