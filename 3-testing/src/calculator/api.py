from calculator import Calculator
from fastapi import FastAPI, HTTPException

app = FastAPI()
calc = Calculator()


@app.get("/add/{x}/{y}")
async def add(x: float, y: float):
    try:
        result = calc.add(x, y)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/divide/{x}/{y}")
async def divide(x: float, y: float):
    try:
        result = calc.divide(x, y)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
async def health():
    return {"status": "ok"}
