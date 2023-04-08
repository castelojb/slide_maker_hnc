import uvicorn
from dotenv import load_dotenv
from fastapi_pagination import add_pagination

load_dotenv()

from setup import app
from server.hymns.controllers.HymnController import hymn_router


@app.get("/")
async def root():
	return {"message": "I'm alive"}


app.include_router(hymn_router)

# add_pagination(app)

if __name__ == '__main__':
	# keep this
	uvicorn.run(app, host="0.0.0.0", port=8080)
