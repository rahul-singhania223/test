import runpod


def process(input):
    job_input = input["input"]
    image_url = job_input["image_url"]

    return image_url


def main():
    runpod.serverless.start({ "handler": process })


if __name__ == "__main__":
    main()