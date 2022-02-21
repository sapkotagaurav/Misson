
from fastapi import FastAPI
from typing import Optional

countries = {"NPL":{"name":"NEPAL","Currency":"Rupees"}
,"IND":{"name":"INDIA","Currency":"Rupees"}


}


app = FastAPI()
@app.get("/")

async def read_root():
	return {"Hello":"World"}

@app.get("/countries/{item_id}")

async def readitem(item_id:int,q:Optional[str]=Path(None,description="Hello")):
	return {"item_id":item_id,"q":countries[q]}
