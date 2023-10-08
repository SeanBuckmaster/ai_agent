

import openai

openai.api_key = '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'

try:
    response = openai.Engine.list()
    print(response)
except Exception as e:
    print("Error:", str(e))


