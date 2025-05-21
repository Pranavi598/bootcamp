from pranavi_hello import say_hello
import typer

app = typer.Typer()

@app.command()
def hello(name: str = "world"):
    print(say_hello(name))

if __name__ == "__main__":
    app()
