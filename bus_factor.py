import requests
import os

# GraphQL code from: https://gist.github.com/gbaman/b3137e18c739e0cf98539bf4ec4366ad
# This code returns the number of forks a repo has to then be used to calculate the bus factor

# def getBusFactor

# Not sure how this will work on eceprog, waiting to hear back on piazza
headers = {"Authorization": "Bearer" + " " + os.environ.get('GITHUB_TOKEN')}

def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

        
# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.       
query = """
{
  repository(owner:"cloudinary", name:"cloudinary_npm") {
    forkCount
  }
}
"""

result = run_query(query) # Execute the query
print(result["data"]["repository"]["forkCount"])

