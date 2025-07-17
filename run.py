# run.py
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()  # Loads HOST and PORT from your .env file if available

if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "8000"))

    print(f"🚀 Starting server at http://{host}:{port}")
    uvicorn.run("app.main:app", host=host, port=port, reload=True)
