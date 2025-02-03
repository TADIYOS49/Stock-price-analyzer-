from fastapi import APIRouter

from app.api.service.agent_service import create_agent


router = APIRouter()


@router.post('/chat')
def hello(query):
    response = create_agent(query)
    return response

