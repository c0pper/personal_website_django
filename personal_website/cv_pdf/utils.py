import requests

def download_file(url, filename):
    resp = requests.get(url) # making requests to server
    with open(filename, "wb") as f: # opening a file handler to create new file
        f.write(resp.content) # writing content to file