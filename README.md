# WhisperCLI

Chat with AIs via your terminal while fully respecting your privacy. 

No data is collected by the CLI. 
Please note: some AIs such as [openai/gpt-oss](https://openrouter.ai/openai/gpt-oss-120b:free) still collect your prompts and responses to train their AIs and/or publish them in public datasets (source: [openrouter.ai/settings/privacy](https://openrouter.ai/settings/privacy)). For greater privacy, use [dolphin-mistral-24b-venice-edition:free](https://openrouter.ai/cognitivecomputations/dolphin-mistral-24b-venice-edition:free).

## Features

- Choose the AI you want to chat with
- Markdown support

## Requirements

- [Python](https://www.python.org/)
- An [OpenRouter](https://openrouter.ai/) account

## Run Locally

Clone the project

```bash
git clone https://github.com/Gautierpicon/WhisperCLI
```

Go to the project directory

```bash
cd WhisperCLI
```

Create a virtual environment:
```bash
python3 -m venv venv
```

Activate the virtual environment:
```bash
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate     # On Windows
```

Install requirements

```bash
pip install -r requirements.txt
```

Run WhisperCLI
For certain models such as [openai/gpt-oss](https://openrouter.ai/openai/gpt-oss-120b:free), enable ‘Enable free endpoints that may train on inputs’ and ‘Enable free endpoints that may publish prompts’ in the [OpenRouter settings](https://openrouter.ai/settings/privacy).

```bash
python main.py
```
## Environment Variables

To run this project, you will need to add the following openrouter environment variable to a .env file:

```bash
  API_KEY=your_api_key_here
```
## Feedback

Feedback are welcome! Feel free to open an [issue](https://github.com/Gautierpicon/WhisperCLI/issues) or a [pull request](https://github.com/Gautierpicon/WhisperCLI/pulls) on the GitHub repository.