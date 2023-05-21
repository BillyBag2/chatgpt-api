#!/bin/python
import secret_api_key

import os
import openai
import pprint

model_name = "gpt-3.5-turbo"
openai.organization = secret_api_key.secret_organization
openai.api_key = secret_api_key.secret_key
#list = openai.Model.list()
#for i in list['data']:
#    print(i['id'])

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)

