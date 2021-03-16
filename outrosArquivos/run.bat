@ECHO OFF
start cmd.exe /C "cd condominioIpe && C:\Users\tofol\PycharmProjects\temCorrespondencia\venv\Scripts\python.exe manage.py runserver"
start C:\"Program Files (x86)"\Google\Chrome\Application\chrome.exe "http://127.0.0.1:8000/"