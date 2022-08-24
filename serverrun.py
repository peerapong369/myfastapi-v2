import uvicorn

class App:
    ...

app = App()

def run():
    print("server running")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

