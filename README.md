For Backend : 

1. cd backend
2. python -m venv myenv
3. myenv\Scripts\activate (for windows)
4. pip install -r requirements.txt
5. uvicorn app.main:app --reload

It will start the backend application :
http://127.0.0.1:8000/
{
    "message": "Welcome to the Translation API"
}


For Frontend :
1. cd frontend
2. npm install -g @angular/cli
3. npm install
4. ng serve

It will start frobtend application 
http://localhost:4200

