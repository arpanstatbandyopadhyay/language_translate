# # app/main.py
# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from app.prompt_model import translate_prompt_based

# app = FastAPI()

# # Configure CORS
# origins = [
#     "http://localhost:4200",  # Allow your Angular app
#     # Add more allowed origins as needed
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all HTTP methods
#     allow_headers=["*"],  # Allows all headers
# )

# class TranslationRequest(BaseModel):
#     text: str
#     src_lang: str  # Source language: 'en' for English, 'de' for German
#     tgt_lang: str  # Target language: 'en' or 'de'

# @app.get("/")
# async def root():
#     return {"message": "Welcome to the Translation API"}

# @app.post("/translate/")
# async def translate_text(request: TranslationRequest):
#     try:
#         translation = translate_prompt_based(request.text, request.src_lang, request.tgt_lang)
#         return {"translation": translation}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.prompt_model import translate_prompt_based
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class TranslationRequest(BaseModel):
    text: str
    src_lang: str  # Source language: 'en' for English, 'de' for German
    tgt_lang: str  # Target language: 'en' or 'de'



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend's URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)    

@app.get("/")
async def root():
    return {"message": "Welcome to the Translation API"}

@app.post("/translate/")
async def translate_text(request: TranslationRequest):
    try:
        translation = translate_prompt_based(request.text, request.src_lang, request.tgt_lang)
        return {"translation": translation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

