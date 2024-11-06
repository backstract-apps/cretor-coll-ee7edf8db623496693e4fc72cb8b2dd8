from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - cretor-coll-ee7edf8db623496693e4fc72cb8b2dd8',debug=False,docs_url='/crazy-anusha-fdf98cb49c2511ef83ee0242c0a8a0044/docs',openapi_url='/crazy-anusha-fdf98cb49c2511ef83ee0242c0a8a0044/openapi.json')

app.include_router(router, prefix='/crazy-anusha-fdf98cb49c2511ef83ee0242c0a8a0044/api', tags=['APIs v1'])

def run_h11():
    uvicorn.run('main:app', host='0.0.0.0', port=8008, reload=True)

if __name__ == '__main__':
    run_h11()