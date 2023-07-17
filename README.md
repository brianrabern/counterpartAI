# counterpartAI

counterpartAI is a project that leverages OpenAI's 'currie' model to create an AI assistant capable of engaging in philosophical discussions as if it were the philosopher David Lewis -- currently it is limited to his book "The Plurality of Worlds".

## Introduction

The AI has been fine-tuned on a specific model called "curie:ft-personal-2023-07-17-20-07-10".

The system uses OpenAI's Python library for API interactions and leverages NLP techniques to generate context-aware responses.

## Installation

1. Clone the CounterpartAI repository from GitHub:

   ```bash
   git clone https://github.com/your-username/counterpartAI.git
   cd counterpartAI
   ```

2. Install the required packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:

   - Sign up for an OpenAI account and obtain your API key.
   - Create a `.env` file in the project root directory.
   - Add your API key to the `.env` file as follows:

     ```python
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## Usage

To interact with CounterpartAI and receive responses run the provided Python script:

```bash
python lewis_bot.py
```

## Fine-Tuning

If you want to fine-tune the model further or experiment with different datasets, you can follow these steps:

1. Prepare your training data in JSONL format with prompt-completion pairs. You can use the provided clean_txt.py and then process_txt.py scripts to clean up and create the JSONL file from a plain text file. This will create a JSONL file named "training_data_prepared.jsonl" containing prompt-completion pairs, ready for fine-tuning.
2. Fine-tune the AI model using the OpenAI API:

   ```bash
   python fine_tune.py
   ```

## Limitations

- So far I've essentially just connected the wires to see if it would even work.
- The quality and accuracy of the responses generated heavily depend on the training data and the fine-tuning process, and at the moment this is not even close to optimized.

## Contributing

Contributions to counterpartAI are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

# CounterpartAI

CounterpartAI is an AI project that harnesses the power of OpenAI's language models to create an assistant capable of engaging in philosophical discussions as if it were the philosopher David Lewis. Currently, counterpartAI's knowledge is trained on Lewis' book "The Plurality of Worlds."

## Introduction

CounterpartAI is built on a fine-tuned version of the "curie" model, specifically tailored to replicate David Lewis' philosophical outlook.

The system utilizes OpenAI's Python library to facilitate API interactions and leverages NLP techniques to generate context-aware responses.

## Installation

1. Clone the CounterpartAI repository from GitHub:

   ```bash
   git clone https://github.com/your-username/counterpartAI.git
   cd counterpartAI
   ```

2. Install the required packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:

   - Sign up for an OpenAI account and obtain your API key.
   - Create a `.env` file in the project root directory.
   - Add your API key to the `.env` file as follows:

     ```plaintext
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## Usage

To interact with CounterpartAI and receive responses, run the provided Python script:

```bash
python lewis_bot.py
```

## Fine-Tuning

If you want to fine-tune the AI model further or experiment with different datasets, follow these steps:

1. Prepare your training data in JSONL format with prompt-completion pairs. You can use the provided "clean_txt.py" and "process_txt.py" scripts to clean up and create the JSONL file from a plain text file. This will produce a JSONL file named "training_data_prepared.jsonl" containing prompt-completion pairs, ready for fine-tuning.

2. Fine-tune the AI model using the OpenAI API (toggle the dataset and the model in `fine_tune.py`):

   ```bash
   python fine_tune.py
   ```

## Limitations

- CounterpartAI is still in the early stages, and the current implementation is only a preliminary test to validate its functionality.
- The quality and accuracy of the responses are heavily dependent on the training data and the fine-tuning process, which is a work in progress and far from optimized.

## Contributing

Contributions to counterpartAI are welcome. If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request.
