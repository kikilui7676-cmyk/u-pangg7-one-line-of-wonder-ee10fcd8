import os

LINE = "The sunlight on your face left the sun eight minutes ago, crossing 150 million kilometres of dark \u2014 you are never warmed by the present, only by a past that came all that way for you."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
