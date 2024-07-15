from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from openai_functions_agent import agent_executor as openai_functions_agent_chain, agent_gmail_executor as openai_functions_agent_gmail_chain

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
add_routes(app, openai_functions_agent_chain, path="/openai-functions-agent")

add_routes(app, openai_functions_agent_gmail_chain, path="/openai-functions-agent-gmail")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
