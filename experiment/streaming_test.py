from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.responses import StreamingResponse
from typing import List
from openai import OpenAI
from helper import *
import logging
import json
import uvicorn
import asyncio

logging.basicConfig(level=logging.DEBUG)  # Set to DEBUG to see detailed logs

app = FastAPI()

class Message(BaseModel):
    role: str
    content: str

class InferenceRequest(BaseModel):
    model: str = GPT4
    messages: List[Message]
    stream: bool

client = OpenAI(api_key=api_key)  # Replace with your actual OpenAI API key

@app.post("/openai_streaming")
async def openai_streaming(request: InferenceRequest):
    try:
        completion = client.chat.completions.create(
            model=request.model,
            messages=[{"role": msg.role, "content": msg.content} for msg in request.messages],
            stream=True
        )

        async def async_generator():
            for chunk in completion:
                logging.debug(f"Received chunk: {chunk}")
                
                response_data = {
                    "id": chunk.id,
                    "object": chunk.object,
                    "created": chunk.created,
                    "model": chunk.model,
                    "system_fingerprint": chunk.system_fingerprint,
                    "choices": [
                        {
                            "index": chunk.choices[0].index,
                            "delta": {
                                "content": getattr(chunk.choices[0].delta, 'content', None)
                            },
                            "finish_reason": chunk.choices[0].finish_reason
                        }
                    ]
                }
                
                await asyncio.sleep(0)
                yield f"{json.dumps(response_data['choices'][0]['delta'].get("content",None))}"

        return StreamingResponse(async_generator(), media_type="text/event-stream")

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)