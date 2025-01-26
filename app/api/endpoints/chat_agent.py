from fastapi import APIRouter


router = APIRouter()


@router.get('/chat')
def hello():
    return {'chat here'}

