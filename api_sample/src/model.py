from pydantic import BaseModel

# データモデルの作成
class TestItem(BaseModel):
    name: str
