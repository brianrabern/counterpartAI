import re


def flatten_text(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f_in:
        content = f_in.read()

    # replace newline characters with spaces
    content = content.replace('\n', ' ')

    # reduce multiple white spaces to one space
    content_on_one_line = re.sub(r'\s+', ' ', content)

    with open(output_file, "w", encoding="utf-8") as f_out:
        f_out.write(content_on_one_line)


input_file = "plurality.txt"


output_file = "clean_plurality.txt"

flatten_text(input_file, output_file)
