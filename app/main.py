import sys
sys.path.append('D:\\DataBase\\new\\group_lab_back')

from fastapi import FastAPI
from app.database import Base, engine
from app.routes.testRroute import *
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="GLBACK", debug=True)

origins = [
    "*",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

app.include_router(user)
app.include_router(category)
app.include_router(course)
app.include_router(chapter)
app.include_router(material)
app.include_router(assignment)
app.include_router(submission)
app.include_router(test)
app.include_router(question)
app.include_router(option)
app.include_router(user_progress_router)
app.include_router(rating_router)
@app.get("/")
def read_root():
    return {"message": "GLBACK"}
