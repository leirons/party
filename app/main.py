from fastapi import FastAPI

from routers import users,party


app = FastAPI()

app.include_router(users.router)
app.include_router(party.router)

