from fastapi import FastAPI

app = FastAPI(
    title="API DB Automation Project",
    description="A FastAPI backend with database automation.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to API DB Automation Project",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }