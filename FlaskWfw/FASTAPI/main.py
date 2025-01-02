"""from typing import Union # union means ya to str ya none
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q":q}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}"""

# for template
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Model data
from sqlalchemy import Column,BIGINT,VARCHAR
from db_setup import Base

# Create Table
class Employee(Base):
    __tablename__ = "employee_details"
    employee_id =Column(BIGINT, primary_key=True)
    employee_name = Column(VARCHAR(40))
    employee_contact_no = Column(BIGINT)
    
# Then migration create
Base.Meta()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )


