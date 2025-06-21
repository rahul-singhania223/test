def handler(event):
    input = event["input"]
    image_url = input["image_url"]


    return { "output": image_url}