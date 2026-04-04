import os
import requests
import typer
from rich.markdown import Markdown
from rich.console import Console
from dotenv import load_dotenv

load_dotenv()

app = typer.Typer()
console = Console()

API_KEY = os.getenv("API_KEY")
URL = "https://openrouter.ai/api/v1/chat/completions"


def ask_api(model, messages):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    data = {"model": model, "messages": messages}

    response = requests.post(URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        console.print(f"[red]API Error {response.status_code}[/red]")
        console.print(response.text)
        return None


@app.command()
def chat():
    """Start a chat with an AI model."""

    model_id = typer.prompt("Model ID (e.g., mistralai/devstral-2512:free)")
    console.print(f"\n[green]Selected model: {model_id}[/green]\n")

    messages = []
    console.print(
        "[bold yellow]Conversation started. Type 'exit' to quit.[/bold yellow]"
    )

    while True:
        user_prompt = typer.prompt("[You]")
        if user_prompt.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_prompt})
        response = ask_api(model_id, messages)

        if response:
            console.print(f"\n[AI]: {response}")
            messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    app()
