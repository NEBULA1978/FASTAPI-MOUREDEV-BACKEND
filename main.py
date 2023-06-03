from fastapi import FastAPI

app = FastAPI()

@app.get("/")
# Siempre que llamemos al servidor asimcronamente
async def root():
    return "Hello World"

@app.get("/url")
# Siempre que llamemos al servidor asimcronamente
async def url():
    return {"url_curso":"https://mouredev.com/python3"}
