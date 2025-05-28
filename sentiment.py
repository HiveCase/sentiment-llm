# consolidated skeleton code
#  Python program that uses httpx to send a POST request to OpenAI's API to analyze the sentiment of this (meaningless) text into GOOD, BAD or NEUTRAL
import httpx
text = '7bch3HkLboJSd Cy9SY8J j9vVugK8yqygNhJXa sR HT 4 rU'
response = httpx.post('http://aiproxy.sanand.workers.dev/openai/v1/chat/completions',
                      headers={"Authorization":"Bearer dummy_api_key"},
                      json={
                          "model":"gpt-4o-mini",
                          "messages":[
                              {"role":"system","content":"classify large volumes of unstructured feedback and text data from various sources as either GOOD, BAD, or NEUTRAL"},
                              {"role":"user","content":text}
                          ]
                      })
response.json()['choices'][0]['message']['content']
