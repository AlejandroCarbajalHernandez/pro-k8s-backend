from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FUNCIONA"}

@app.get("/health")
def health():
    return {"status": "ok"}