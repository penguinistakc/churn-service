import httpx

url = 'http://localhost:9696/predict'

customer = {
  "gender": "male",
  "seniorcitizen": 0,
  "partner": "no",
  "dependents": "yes",
  "phoneservice": "no",
  "multiplelines": "no_phone_service",
  "internetservice": "dsl",
  "onlinesecurity": "no",
  "onlinebackup": "yes",
  "deviceprotection": "no",
  "techsupport": "no",
  "streamingtv": "no",
  "streamingmovies": "no",
  "contract": "month-to-month",
  "paperlessbilling": "yes",
  "paymentmethod": "electronic_check",
  "tenure": 6,
  "monthlycharges": 29.85,
  "totalcharges": 179.1
}

response = httpx.post(url, json=customer)
churn = response.json()

print('response:', churn)

if churn['churn'] >= 0.5:
    print('Send email with promo')
else:
    print('Do nothing')

# if __name__ == "__main__":
#     main()
