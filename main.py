from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

model = "local/path/to/Hermes-2-Pro-Llama-3-8B-Q8_0.gguf"
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
# Add route
add_routes(
    app,
    prompt | model,
    path="/joke",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)