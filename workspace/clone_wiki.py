#!/bin/python

import os
import subprocess

# Define the directory and repository
directory = "the_space.wiki"
repo_url = "https://github.com/cheltenhamhackspace/the_space.wiki.git"

# Check if the directory exists
if os.path.exists(directory):
    # If it exists, navigate into the directory and pull the latest version
    os.chdir(directory)
    print("> git status")
    subprocess.call(["git", "status"])
    print("> git pull")
    subprocess.call(["git", "pull"])
else:
    # If it doesn't exist, clone the repository
    print("> git clone {repo_url}")
    subprocess.call(["git", "clone", repo_url])
    print("> git status")
    subprocess.call(["git", "status"])

