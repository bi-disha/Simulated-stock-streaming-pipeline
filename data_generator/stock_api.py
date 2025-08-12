from fastapi import FastAPI
from fastapi.responses import JSONResponse
from data_sim_generator import generate_all_stocks  # import your generator function

app = FastAPI()

@app.get("/stocks")
def get_stock_data():
    data = generate_all_stocks()
    return JSONResponse(content=data)