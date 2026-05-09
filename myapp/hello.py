import fire


GREETINGS = {
    "morning": "Good morning",
    "afternoon": "Good afternoon",
    "evening": "Good evening",
}


def hello(name="World", greeting="morning", repeat=1, shout=False):
    """A friendly CLI greeter powered by Python Fire.

    Args:
        name: Who to greet.
        greeting: Time of day — morning, afternoon, or evening.
        repeat: How many times to greet.
        shout: SHOUT THE GREETING if True.
    """
    prefix = GREETINGS.get(greeting, "Hello")
    message = f"{prefix}, {name}! Welcome to the Jenkins pipeline."

    if shout:
        message = message.upper()

    for i in range(repeat):
        print(f"[{i + 1}] {message}")


if __name__ == "__main__":
    fire.Fire(hello)
