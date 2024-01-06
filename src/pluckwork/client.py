import asyncio
from pydantic import BaseModel
import httpx

class Input(BaseModel):
    id: str
    input: bytes

class Client():
    url: str = ""
    _client: httpx.AsyncClient = None

    def __init__(self, url: str):
        self.url = url
        self._client = httpx.AsyncClient()

    async def enqueue_job(self, input: bytes, topic: str) -> str:
        response = await self._client.post(self.url, content=input)
        return str(response.content)

    async def dequeue_job(self, topic: str) -> Input | None:
        response = await self._client.get(self.url + "/task")
        result = response.content
        return Input(**result) if result is not None else None

    async def submit_result(self, id: str, output: bytes) -> None:
        await self._client.post(self.url + "/task", params={"id": id}, content=output)

    async def retrieve_result(self, id: str) -> bytes | None:
        result = await self._client.get(self.url, params={"id": id})
        return result.content
    
    async def call(self, input: bytes, topic: str) -> bytes:
        id = await self.enqueue_job(input, topic)
        result = None
        while result is None:
            result = await self.retrieve_result(id)
            if result is None:
                await asyncio.sleep(30)
        return result