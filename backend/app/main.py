from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FBR E-Invoicing Backend is running"}
