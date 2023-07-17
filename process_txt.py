import json
import re
import subprocess


def split_into_sentences(text):
    # split the text into sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return sentences


def create_prompt_completion_pairs(sentences):
    # create prompt-completion pairs using sentences
    pairs = []
    for i in range(len(sentences) - 3):
        prompt = sentences[i]
        completion = sentences[i+1:i+4]  # next three sentences
        pairs.append({"prompt": prompt, "completion": completion})
    return pairs


def write_jsonl(file_path, pairs):
    # write to a JSONL file
    with open(file_path, "w", encoding="utf-8") as f_out:
        for pair in pairs:
            json.dump(pair, f_out, ensure_ascii=False)
            f_out.write("\n")


def prepare_data(local_file):
    command = ["openai", "tools", "fine_tunes.prepare_data", "-f", local_file]
    subprocess.run(command, check=True)


input_txt_file = "clean_plurality.txt"
output_jsonl_file = "training_data.jsonl"

with open(input_txt_file, "r", encoding="utf-8") as f_in:
    book_text = f_in.read()

# split the book text into sentences
sentences = split_into_sentences(book_text)

# create prompt-completion pairs
pairs = create_prompt_completion_pairs(sentences)

# write the pairs
write_jsonl(output_jsonl_file, pairs)

# prepare the data
prepare_data(output_jsonl_file)
