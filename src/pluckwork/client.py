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
    
    async def pull(self) -> Input | None:
        response = await self._client.get(self.url + "/task")
        result = await response.json()
        return Input(**result) if result is not None else None

    async def push(self, id: str, output: bytes) -> None:
        await self._client.post(self.url + "/task", params={"id": id}, content=output)