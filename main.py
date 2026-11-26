import os

SENTENCE = "You left it in my patrol route, so I cleared the route; hire a guard if you want the table defended."


def main() -> None:
    sentence = SENTENCE
    assert sentence.strip() != "", "sentence must not be blank"
    assert sentence == sentence.strip(), "sentence must not have leading/trailing padding"
    assert "\n" not in sentence and "\r" not in sentence, "sentence must be single-line"
    assert 1 <= len(sentence) <= 200, "sentence must be between 1 and 200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as handle:
        handle.write(sentence.encode("utf-8"))


if __name__ == "__main__":
    main()
