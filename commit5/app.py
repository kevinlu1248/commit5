import typer
import requests
import docker

app = typer.Typer(name="commit5")
client = docker.from_env()
image_name = "kevinlu1248/commit5"

@app.command()
def install():
    "Pulls commit5 docker container"
    client.pull(image_name)

@app.command()
def start():
    "Starts commit5 docker container in background"
    client.run(image_name, expose_ports=["1729:1729"])

@app.command()
def stop():
    "Stops commit5 docker container in background"
    client.stop(image_name)

@app.command()
def test():
    "Tests commit5 docker image"
    try:
        requests.get("http://0.0.0.0:1729/")
    except:
        print("Docker is not running. Try running 'commit5 start'.")
        exit(1)
    else:
        print("Docker is running.")

@app.command()
def generate(diff: str):
    message = requests.get("http://0.0.0.0:1729/", json={"diff": diff})
    print(message)

if __name__ == '__main__':
    app()