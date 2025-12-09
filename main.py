import os
import json
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

def load_models():
    """Load models from external JSON file."""
    try:
        with open("models.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data["models"]
    except FileNotFoundError:
        console.print("[red]Error: models.json file not found[/red]")
        raise typer.Exit()
    except json.JSONDecodeError:
        console.print("[red]Error: Invalid JSON in models.json[/red]")
        raise typer.Exit()

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
    
    models = load_models()

    console.print("[bold cyan]=== Choose your AI model ===[/bold cyan]")
    console.print("[bold]0.[/bold] [magenta]Custom model (enter your own)[/magenta]")
    for key, model_info in models.items():
        console.print(f"[bold]{key}.[/bold] {model_info['name']} - [dim]{model_info['description']}[/dim]")

    choice = typer.prompt("Model number")
    
    if choice == "0":
        model_id = typer.prompt("Enter the model ID (e.g., mistralai/devstral-2512:free)")
        model_name = model_id
        console.print(f"\n[green]Selected custom model: {model_id}[/green]\n")
    else:
        model_info = models.get(choice)
        
        if not model_info:
            console.print("[red]Invalid model[/red]")
            raise typer.Exit()
        
        model_id = model_info["id"]
        model_name = model_info['name']
        console.print(f"\n[green]Selected model: {model_name} ({model_id})[/green]\n")

    messages = []
    console.print("[bold yellow]Conversation started. Type 'exit' to quit.[/bold yellow]")

    while True:
        user_prompt = typer.prompt("\n[You]")
        if user_prompt.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_prompt})
        response = ask_api(model_id, messages)

        if response:
            console.print(Markdown(response))
            messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    app()