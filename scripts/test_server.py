from requests import get, post

if __name__ == "__main__":
    print(get("http://127.0.0.1:8000/").text)
    print(post("http://127.0.0.1:8000/", data={"diff": "test"}).text) # should return "Fix typo"