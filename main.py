import openai
from os import environ as env

# Load the API key

APIKEY = env['APIKEY']
openai.api_key = APIKEY

# Set the prompt for what we want to be generated

Number_of_photos = 4
response = openai.Image.create(
  prompt="cow with 7 legs jumping over the moon",
  n=4,
  size="1024x1024"
)

# Set up some optical aspects

num = 1
print('The links are as follows:\n')

# Create loop for every image

for i in range(0, 4):
  image_url = response['data'][i]['url']
  print(f'{num}. {image_url}')
  num += 1


