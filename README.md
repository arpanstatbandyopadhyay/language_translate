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

This is the UI

![image](https://github.com/user-attachments/assets/91a6016d-1696-467d-bc57-af9c8a7a3e55)

Here you can translate from German to English and Visa-versa

