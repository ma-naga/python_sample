try:
    from app import app, CONTEXT_PATH
    from model import TestItem
except Exception:
    from .app import app, CONTEXT_PATH
    from .model import TestItem

@app.get(CONTEXT_PATH)
async def read_root():
    return {"Hello": "root"}

@app.post(CONTEXT_PATH + "test")
async def read_test(item: TestItem):
    return {"ret_name": item.name}
