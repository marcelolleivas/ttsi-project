def before_all(context):
    userdata = context.config.userdata
    context.lojinha_service_url = userdata.get("lojinha_url", "")
    print(f"testandoooo: {context.lojinha_service_url}")
