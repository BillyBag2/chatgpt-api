#!/bin/python

# Create a secret_api_key.py file...
#   secret_organization = "org-..."
#   secret_key = "sk-..."
import os
import subprocess
import openai

def count_letters(input_string):
    return sum(c.isalpha() for c in input_string)

max_letters = 3500 * 4

# Secret keys for the ChatGPT API
import secret_api_key

# Banner
import banner
# Git clone the wiki locally. Pull to get latest.
import clone_wiki

# Concatenate all files in the wiki directory
concatenated_wiki = ""
header = "==== Markdown File: {filename} ====\n"

exclude_files = [ 
        "_Sidebar.md",
        "Covid-Shield-Making-Rota.md", 
        "DCS-FS12-NV7.md",
        "Membership-and-access.md",
        "PcbEngraver.md"
    ]

for filename in os.listdir():
    if os.path.isfile(filename) and filename not in exclude_files:
        with open(filename, 'r') as file:
            concatenated_wiki += header.format(filename=filename)
            concatenated_wiki += file.read() + "\n"

# Create a system
system_content = """
You are a helpful assistant that provides information about the cheltenham hackspace.
Some of the information may be provided in Cheltenham hackspace's  wiki.
The wiki is a in markdown format on github.
The URL to the wiki is https://github.com/cheltenhamhackspace/the_space/wiki/ . 
The contents of the wiki are listed below.
"""

system_content = system_content + concatenated_wiki

# print(concatenated_wiki)

model_name = "gpt-3.5-turbo"
openai.organization = secret_api_key.secret_organization
openai.api_key = secret_api_key.secret_key

#print(system_content)
#completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": system_content}])
#completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "How many rooms are there in cheltenham hackspace?"}])

messages=[{"role": "system", "content": system_content}]
print("READY")

while True:
    user_input = input("INPUT: ")
    messages.append({"role": "user", "content": user_input })
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    response = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": response })
    print("OUTPUT: %s" % response)
    letter_count = 0
    for mess in messages:
        letter_count = letter_count + count_letters(mess["content"])
    while  letter_count > max_letters:
        print("(Forgetting older parts of this conversation.)")
        del messages[1]
        del messages[1]
        for mess in messages:
            letter_count = letter_count + count_letters(mess["content"])



