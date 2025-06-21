import runpod


def process(input):
    job_input = input["input"]
    image_url = job_input["image_url"]

    result_image = {
        "image_url": "image_url",
        "filename": "filename"
    }

    return result_image


def main():
    runpod.serverless.start({ "handler": process })


if __name__ == "__main__":
    main()