import uvicorn
from emp.controller.main import app

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
