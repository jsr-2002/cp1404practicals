"""
Word Occurrences
Estimate: 30 minutes
Actual:   TODO
"""

def main():
    text = input("Text: ").strip()
    # Split on whitespace
    words = text.split()
    counts = {}
    for word in words:
        word = word.lower()
        counts[word] = counts.get(word, 0) + 1

    # Sort by word (alphabetical)
    items = sorted(counts.items())

    # Find the longest word for alignment
    max_len = max((len(word) for word, _ in items), default=0)
    for word, count in items:
        print(f"{word:{max_len}} : {count}")


if __name__ == "__main__":
    main()
