from fastapi import FastAPI


app=FastAPI()


@app.get("/")
def read_root():
    return {"hello":"word"}


@app.get("/items/{item_id}")    
def read_item(item_id:int):
    return {"item_id":item_id}

#web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app