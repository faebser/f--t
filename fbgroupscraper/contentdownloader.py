from facepy import GraphAPI

group_id = "290537284306690"
access_token = "YOUR_ACCESS_TOKEN"

graph = GraphAPI(access_token)

# https://facepy.readthedocs.org/en/latest/usage/graph-api.html
data = graph.get(group_id + "/feed", page=False, retry=3, limit=800)

print data