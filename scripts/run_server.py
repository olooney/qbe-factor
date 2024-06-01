import os
import uvicorn

if __name__ == "__main__":
    port = int(os.getenv('PORT', 8000))
    uvicorn.run("qbe_factor.api:app", host="0.0.0.0", port=port)

