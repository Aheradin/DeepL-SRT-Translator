# Deepl SRT Translator

## Description
This script translates a list of .srt files to the desired language using the [Deepl API](https://www.deepl.com/es/pro-api).
The free tier allows to translate an amount of 500.000characters/month

## Requirements
Before running the code, make sure you have the following:
- Deepl API key: you can create an account [here](https://www.deepl.com/es/pro-api)
- Python: you can install it from [here](https://www.python.org/downloads/).

## Installation
1. Clone this repository to your local machine using `git clone` or download the [latest release](https://github.com/Aheradin/Deepl-SRT-Translator/releases)
   ```
   git clone https://github.com/Aheradin/Deepl-SRT-Translator.git
   ```
2. Open a terminal or command prompt in the directory.
3. Navigate to the project directory using the `cd` command. (or open the command prompt directly on the folder)
4. Install the required dependencies by running:
    ```
    py -m pip install -r requirements.txt
    ```

## How to Run
To run the code, follow these steps:
1. Write [your API key](https://www.deepl.com/es/your-account/keys) on `api_key.txt` file.
2. Write the source language key in `source_language.txt` (Check the available languages and their codes [here](https://developers.deepl.com/docs/api-reference/languages))
3. Write the key of your desired language in `target_language.txt` (Check the available languages and their codes [here](https://developers.deepl.com/docs/api-reference/languages))
    1. (Optional) If you want to add a glossary edit the GLOSSARY_ENTRIES variable in main.py file following the example: written Left -> Original language Right -> Desired translation
4. Open a terminal or command prompt in the directory.
5. Run the following command:
    ```
    py main.py
    ```
4. Enjoy!

## Troubleshooting
- If you encounter any errors or issues during installation or while running the code, please [open an issue](https://github.com/Aheradin/Deepl-SRT-Translator/issues) on GitHub.

## Common Errors
- `ValueError: api_key.txt must not be empty`
    - Go to `api_key.txt` and paste your API key from [here](https://www.deepl.com/es/your-account/keys)
- `deepl.exceptions.DeepLException: Unexpected status code: 401 Unauthorized, content: {"message":"Unauthorized"}.`
    - Ensure your API key is valid.
- `deepl.exceptions.ConnectionException: Unexpected request failure: Invalid header value`
    - Ensure only your key is in the `api_key.txt` file, no whitespaces or new lines.

## License
This project is licensed under the [MIT License](LICENSE).
