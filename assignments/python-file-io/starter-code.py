def read_text_file(path):
    """Read a text file and return its contents."""
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def count_lines_words_chars(text):
    """Count lines, words, and characters in the given text."""
    lines = text.splitlines()
    words = text.split()
    characters = len(text)
    return len(lines), len(words), characters


def write_report(path, report_text):
    """Write the report text to a file."""
    with open(path, 'w', encoding='utf-8') as file:
        file.write(report_text)


if __name__ == '__main__':
    input_path = 'sample-text.txt'
    output_path = 'report.txt'

    text = read_text_file(input_path)
    lines, words, characters = count_lines_words_chars(text)

    summary = (
        f'File report for {input_path}\n'
        f'Lines: {lines}\n'
        f'Words: {words}\n'
        f'Characters: {characters}\n'
    )

    print(summary)
    write_report(output_path, summary)
    print(f'Report saved to {output_path}')
