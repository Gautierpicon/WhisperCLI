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

MODELS = {
    "1": "openai/gpt-oss-120b:free",
    "2": "qwen/qwen3-235b-a22b:free",
    "3": "cognitivecomputations/dolphin-mistral-24b-venice-edition:free",
    "4": "google/gemma-3-27b-it:free",
}

def ask_api(model, messages):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": model,
        "messages": messages
    }

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

    console.print("[bold cyan]=== Choose your AI model ===[/bold cyan]")
    for key, model in MODELS.items():
        console.print(f"[bold]{key}.[/bold] {model}")

    choice = typer.prompt("Model number")
    model = MODELS.get(choice)

    if not model:
        console.print("[red]Invalid model[/red]")
        raise typer.Exit()

    console.print(f"\n[green]Selected model: {model}[/green]\n")

    messages = []
    console.print("[bold yellow]Conversation started. Type 'exit' to quit.[/bold yellow]")

    while True:
        user_prompt = typer.prompt("\n[You]")
        if user_prompt.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_prompt})
        response = ask_api(model, messages)

        if response:
            console.print(Markdown(response))
            messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    app()