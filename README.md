# kili-rag

## Developed environment

Install poetry packages manager if it has not existed yet

```bash
pip install -U poetry
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
```

Configure launch.json to debug

```json
"configurations": [
    {
        "name": "LangServe",
        "type": "debugpy",
        "request": "launch",
        "cwd": "${workspaceFolder}",
        "program": "${workspaceFolder}/.venv/bin/langchain",
        "args": [
            "serve",
            "--port",
            "3100",
        ],
        "jinja": true
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

# use template and expose api
from $TEMPLATE_NAME import $Runnable
add_routes(app, $Runnable, path="/$TEMPLATE_NAME") // could expose any path
# example:
>from openai_functions_agent import agent_executor as openai_functions_agent_chain
>add_routes(app, openai_functions_agent_chain, path="/openai-functions-agent")

# restart language server to recognize added template module
focus on server.py
MacOS: Cmd + Shift + P
Others OS: Ctrl + Shift + P
>>Python: Restart Language Server
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

In the below example, we inject the `OPENAI_API_KEY` environment
variable with the value set in my local environment
(`$OPENAI_API_KEY`)

We also expose port 8080 with the `-p 8080:8080` option.

```shell
docker run -e OPENAI_API_KEY=$OPENAI_API_KEY -p 8080:8080 kili-rag
```
