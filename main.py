import os

ENTRY_TEXT = "All services are down. I cannot reach any server to check what failed, so I don't know the cause or when they will return."


def validated_text(text):
    """Check the entry against the gate: UTF-8, 1-160 chars, not only
    whitespace, exactly one line. The trailing newline is the file's
    line terminator, not part of the entry text."""
    encoded = text.encode("utf-8")
    decoded = encoded.decode("utf-8")
    assert decoded == text, "entry is not clean UTF-8"
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, gate is 1-160"
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text, "entry must be a single line"
    return text


def main():
    text = validated_text(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    with open(path, "rb") as f:
        written = f.read()
    assert written.decode("utf-8") == text + "\n", "written bytes differ"


if __name__ == "__main__":
    main()
