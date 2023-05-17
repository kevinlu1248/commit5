import subprocess
import typer
import requests
import docker

app = typer.Typer(name="commit5")
client = docker.from_env()
image_location = "kevinlu1248/commit5"
image_name = "commit5"

@app.command()
def download():
    "Pulls commit5 docker container"
    client.images.pull(image_location)

@app.command()
def start():
    "Starts commit5 docker container in background"
    client.containers.run(image_name, ports={"1729": "1729"}, detach=True)

@app.command()
def stop():
    "Stops commit5 docker container in background"
    for container in client.containers.list():
        if f"{image_name}:latest" in container.image.tags:
            container.stop()
            break

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
    message = requests.post("http://0.0.0.0:1729/", json={"diff": diff}).text
    print(message)
    return message

@app.command()
def commit():
    diff = subprocess.run(["git", "diff"]).stdout.decode("utf-8")
    message = generate(diff)
    subprocess.run(["git", "commit", "-m", message])

if __name__ == '__main__':
    app()