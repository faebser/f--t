from facepy import GraphAPI
import json

group_id = "290537284306690"
access_token = "YOUR_ACCESS_TOKEN"

graph = GraphAPI(access_token)

'''
some notes:
- you have to use pagination to get all the posts from a group, fb won't give you all the post in one request
- I would write a json-chunk to the disk after each pagination so the script can iterate over them after finishing the requests to fb
- The script can also use the json-files to see if there was an error and restart with a certain file
- I think that this script should be run repeated times so it needs a mechanism to check which posts it already has saved to the db
- Use some multi-threaded processing, it's super easy -> https://medium.com/building-things-on-the-internet/40e9b2b36148

'''

# https://facepy.readthedocs.org/en/latest/usage/graph-api.html
data = graph.get(group_id + "/feed", page=False, retry=3, limit=800)

with open('content.json', 'w') as outfile:
  json.dump(data, outfile, indent = 4)