from requests import delete

AUTH_TOKEN = {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvaWQiOiIyMDg0IiwidXN1YXJpb2xvZ2luIjoibWFyY2Vsb2x"
             "laXZhc3MiLCJ1c3Vhcmlvbm9tZSI6Ik1hcmNlbG8gTGVpdmFzIn0.FJTrsdoiRt3aaT0nVazf0JEd2ZGhjpGvvDqgdPsQSMM"
}


def clean_data():
    response = delete(
        "http://165.227.93.41/lojinha/dados",
        headers=AUTH_TOKEN
    )
    return response
