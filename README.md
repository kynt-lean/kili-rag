# kili-rag

## Developed environment

Install poetry packages manager if it has not existed yet

```bash
pip install -U poetry
# enable poetry tab completion for bash
poetry completions bash >> ~/.bash_completion
# or for zsh
poetry completions zsh > ~/.zfunc/_poetry # specify the folder included in $fpath
```

Configure poetry virtualenvs settings

```bash
poetry config virtualenvs.in-project true
```

Install workspace dependencies

```bash
poetry install
```

Activate vscode python interpreter

```cmd
focus on server.py
MacOS: Cmd + Shift + P
Others OS: Ctrl + Shift + P
>Python: Select interpreter
Select: ./.venv/bin/python
```

## Serving or debugging

Serve langchain server from command line

```bash
poetry run langchain serve --port 3100
# or directly using uvicorn
poetry run uvicorn app.server:app --port 3100 --reload
```

Configure launch.json to debug

```json
"configurations": [
    {
        "name": "Langchain Serve",
        "type": "debugpy",
        "request": "launch",
        "cwd": "${workspaceFolder}",
        "program": "${workspaceFolder}/.venv/bin/langchain",
        "args": [
            "serve",
            "--port",
            "3100",
        ],
    },
    {
        "name": "Uvicorn Serve",
        "type": "debugpy",
        "request": "launch",
        "cwd": "${workspaceFolder}",
        "program": "${workspaceFolder}/.venv/bin/uvicorn",
        "args": [
            "app.server:app",
            "--port",
            "3100",
            "--reload"
        ],
    }
]
```

## Adding templates (pre-built Runnable as editable package)

```bash
# add template
poetry run langchain app add --no-pip $TEMPLATE_NAME
# example:
>poetry run langchain app add --no-pip openai-functions-agent
>poetry run langchain app add --no-pip git+ssh://git@github.com/efriis/simple-pirate.git

# install dependencies of template
poetry update $TEMPLATE_NAME
# example:
>poetry update openai-functions-agent

# expose template api following by ./packages/$TEMPLATE_NAME/README.md
# example:
>code ./packages/openai-functions-agent/README.md

# restart language server to recognize added template module
focus on server.py
MacOS: Cmd + Shift + P
Others OS: Ctrl + Shift + P
>Python: Restart Language Server
```

## Removing templates

```bash
# remove dependencies of template
poetry remove $TEMPLATE_NAME
# example:
>poetry remove openai-functions-agent

# remove editable package
poetry run langchain app remove $TEMPLATE_NAME
# example:
>poetry run langchain app remove openai-functions-agent

# remove template api endpoint from server.py
```

## Running in Docker

This project folder includes a Dockerfile that allows you to easily build and host your LangServe app.

### Building the Image

To build the image, you simply:

```shell
docker build . -t kili-rag
```

If you tag your image with something other than `kili-rag`,
note it for use in the next step.

### Running the Image Locally

To run the image, you'll need to include any environment variables
necessary for your application.

In the below example, we inject the `OPENAI_API_KEY` and `TAVILY_API_KEY` environment
variable with the value set in my local environment
(`$OPENAI_API_KEY`, `$TAVILY_API_KEY`)

We also expose port 8080 with the `-p 8080:8080` option.

```shell
docker run -e OPENAI_API_KEY=$OPENAI_API_KEY -e TAVILY_API_KEY=$TAVILY_API_KEY -p 8080:8080 kili-rag
```
