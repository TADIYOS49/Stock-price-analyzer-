from fastapi import FastAPI


from app.api.endpoints import hello_route, chat_agent



def create_api():

    api = FastAPI()

    api.include_router(hello_route.router)
    api.include_router(chat_agent.router)

    return api