DEFAULT_HEADERS = {"Content-Type": "application/json"}

VALID_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvaWQiOiIyMDg0IiwidXN1YXJpb2xvZ2luIjoibWFyY2Vsb2xlaXZhc" \
              "3MiLCJ1c3Vhcmlvbm9tZSI6Ik1hcmNlbG8gTGVpdmFzIn0.FJTrsdoiRt3aaT0nVazf0JEd2ZGhjpGvvDqgdPsQSMM"

VALID_CREATE_USER_PAYLOAD = {
    "usuarionome": "Lorem ipsum",
    "usuariologin": "loremipsum",
    "usuariosenha": "lorem12345",
}


VALID_USER_PAYLOAD = {
    "usuariologin": "marceloleivass",
    "usuariosenha": "marcelo123"
}

INVALID_USER_PAYLOAD = {
    "usuariologin": "marceloleivass",
    "usuariosenha": "123456"
}

VALID_PRODUCT_PAYLOAD = {
    "produtonome": "MacBook Pro 13",
    "produtovalor": 7000,
    "produtocores": [
        "cinza"
    ],
    "componentes": [
        {
            "componentenome": "carregador",
            "componentequantidade": 1
        }
    ]
}

VALID_PRODUCT_PAYLOAD_2 = {
    "produtonome": "Playstation 5",
    "produtovalor": 2500,
    "produtocores": [
        "preto"
    ],
    "componentes": [
        {
            "componentenome": "controle",
            "componentequantidade": 2
        }
    ]
}

