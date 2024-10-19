from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

CONTEXT_PATH = "/"
DOCS_YAML = "docs.yaml"
app = FastAPI(
    docs_url=(CONTEXT_PATH + DOCS_YAML)
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


