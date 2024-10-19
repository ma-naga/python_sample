# ローカルでテストを行う場合
uvicorn src.main:app --host 0.0.0.0 --port 8000

## ローカルでアクセス方法
http://0.0.0.0:8000

# cloud run にデプロイする場合
gcloud run deploy fastapi-sample --project st-pg-naga --source . --region asia-northeast1 --platform managed --allow-unauthenticated --concurrency=80 --min-instances=0 --max-instances=1 --service-account=cloud-run-multi@st-pg-naga.iam.gserviceaccount.com 



