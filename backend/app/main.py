from fastapi import FastAPI, HTTPException  # Import FastAPI for creating the web app and HTTPException for error handling
from pydantic import BaseModel  # Import BaseModel from Pydantic for data validation
from app.prompt_model import translate_prompt_based  # Import the translation function from the prompt_model module
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware to handle cross-origin requests

# Create an instance of the FastAPI application
app = FastAPI()

# Define a Pydantic model for the translation request
class TranslationRequest(BaseModel):
    text: str                # The text to be translated
    src_lang: str           # Source language: 'en' for English, 'de' for German
    tgt_lang: str           # Target language: 'en' or 'de'

# Add CORS middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # Allow requests from any origin (update this in production)
    allow_credentials=True,  # Allow cookies and credentials in cross-origin requests
    allow_methods=["*"],     # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],     # Allow all headers in requests
)    

# Define the root endpoint for the application
@app.get("/")  
async def root():
    return {"message": "Welcome to the Translation API"}  # Returns a welcome message in JSON format

# Define the translation endpoint that handles POST requests
@app.post("/translate/")  
async def translate_text(request: TranslationRequest):
    """
    Translate text from the source language to the target language.
    :param request: TranslationRequest object containing the text and language info
    :return: JSON response with the translated text
    """
    try:
        # Call the translate function with the request data and store the result
        translation = translate_prompt_based(request.text, request.src_lang, request.tgt_lang)
        return {"translation": translation}  # Return the translation in JSON format
    except Exception as e:
        # Raise an HTTPException with status code 500 if an error occurs during translation
        raise HTTPException(status_code=500, detail=str(e))
