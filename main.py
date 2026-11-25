import os

LINE = (
    "The elevator's close-door button is a placebo installed by cowards. "
    "I have pressed it 4,000 times and the doors have never once obeyed. "
    "They close when they feel like it: never when I'm late, always when "
    "someone sprints over with coffee. It is the only button in my life "
    "that lies to my face daily, and I still press it, because hope is the "
    "last thing this elevator hasn't taken from me."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
