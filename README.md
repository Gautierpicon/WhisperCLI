# OpenRouterCLI [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.md)

Chat with AIs through your terminal while fully respecting your privacy.

> **Legal Disclaimer:** This project is an independent, community-made tool and is not affiliated with, endorsed by, or in any way officially connected to [OpenRouter](https://openrouter.ai/) or any of its subsidiaries. The [OpenRouter](https://openrouter.ai/) name and logo are trademarks of their respective owners.

No data is collected by the CLI.
Please note: some AIs such as [openai/gpt-oss](https://openrouter.ai/openai/gpt-oss-120b:free) still collect your prompts and responses to train their AIs and/or publish them in public datasets (source: [openrouter.ai/settings/privacy](https://openrouter.ai/settings/privacy)).

## Features

- Mmanually enter the ID of a custom model
- Markdown support

## Requirements

- [Python](https://www.python.org/)
- An [OpenRouter](https://openrouter.ai/) account
- [uv](https://docs.astral.sh/uv/)

## Run Locally

Clone the project

```bash
git clone https://github.com/Gautierpicon/OpenRouterCLI
```

Go to the project directory

```bash
cd OpenRouterCLI
```

Install dependencies

```bash
uv sync
```

Run OpenRouterCLI

For certain models such as [openai/gpt-oss](https://openrouter.ai/openai/gpt-oss-120b:free), enable ‘Enable free endpoints that may train on inputs’ and ‘Enable free endpoints that may publish prompts’ in the [OpenRouter settings](https://openrouter.ai/settings/privacy).

```bash
uv run python main.py
```

## Environment Variables

To run this project, you will need to add the following openrouter environment variable to a .env file:

```bash
  API_KEY=your_api_key_here
```

## Feedback

Feedback are welcome! Feel free to open an [issue](https://github.com/Gautierpicon/OpenRouterCLI/issues) or a [pull request](https://github.com/Gautierpicon/OpenRouterCLI/pulls) on the GitHub repository.
