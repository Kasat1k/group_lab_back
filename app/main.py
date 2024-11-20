from fastapi import FastAPI
from app.database import Base, engine
from app.routes.testRroute import test_router
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="GLBACK")

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

app.include_router(test_router)

@app.get("/")
def read_root():
    return {"message": "GLBACK"}
