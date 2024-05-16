import os
import deepl

GLOSSARY_NAME = "Glossary"
# Words to translate in a specific way: Left -> Original, Right -> Translation
GLOSSARY_ENTRIES = {
    'Aheradin' : 'Aheradin',
}

# Get all files in folder with the .srt extension
def get_srt_files(folder_path):
    srt_files = []
    for file in sorted(os.listdir(folder_path)):
        if file.endswith(".srt"):
            srt_files.append(file)
    return srt_files

# Read and return the subtitles
def read_SRT(file_path):
    print("Reading subtitles...")
    subtitlesData = []
    with open(file_path, 'r', encoding='utf-8') as file:
        subtitle_content = file.read().strip()
        # Split array wherever there're double new line characters
        subtitle_blocks = subtitle_content.split('\n\n')
        for block in subtitle_blocks:
            # Separate the array by new lines
            lines = block.strip().split('\n')
            if len(lines) >= 3:
                index = lines[0]
                timing = lines[1]
                text = ' '.join(lines[2:]) # Joins the remaining ones
                subtitlesData.append({
                    'index': index,
                    'timing': timing,
                    'text': text,
                    'text_lines': len(lines) - 2
                })
    return subtitlesData

def split_string_by_words(input_string, num_parts):
    # Split the input string into words
    words = input_string.split()
    # Calculate the number of words per part
    words_per_part = (len(words) + num_parts - 1) // num_parts
    # Split the words into the desired number of parts
    parts = [words[i:i+words_per_part] for i in range(0, len(words), words_per_part)]
    # Join the words in each part into strings
    parts = [' '.join(part) for part in parts]
    return parts

# Translate the subtitles
def translate_subtitles(subtitles, translator, glossary, source_language, target_language):
    print("Starting translation...")
    for i, subtitle in enumerate(subtitles):
        print(f"Translating subtitle {i}")
        if(subtitle is not None):
            subtitles[i]['text'] = translator.translate_text(subtitle['text'], target_lang=target_language, glossary=glossary, formality=deepl.Formality.LESS, source_lang=source_language).text
    print("Translation completed!")
    return subtitles

# Write the subtitles in the output_file
def write_SRT(subtitlesData, output_file):
    if not os.path.exists(output_file):
        os.makedirs(output_file)
        print("Created output folder...")
        return

    print("Writing new subtitles...")
    with open(output_file, 'w', encoding='utf-8') as file:
        for subtitleData in subtitlesData:
            file.write(subtitleData['index'] + '\n')
            file.write(subtitleData['timing'] + '\n')

            subtitle_text = subtitleData['text']
            text_lines = subtitleData['text_lines']

            if text_lines > 1:
                parts = split_string_by_words(subtitle_text, text_lines)
                filtered_text = '\n'.join(parts)
            else:
                filtered_text = subtitle_text

            file.write(filtered_text + '\n\n')

def main():
    # Init paths
    script_path = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_path, "Input/")
    output_path = os.path.join(script_path, "Output/")

    # Read variables

    # Make at least a free account (500.000 free characters by month)
    # https://www.deepl.com/es/pro-api
    # Get your key down here and paste it in aut_key.txt
    # https://www.deepl.com/es/your-account/keys
    DEEPL_AUTH_KEY = open('api_key.txt', 'a+').read()
    # Check the list and set your desired languages before starting
    # https://developers.deepl.com/docs/api-reference/languages
    SOURCE_LANGUAGE = open('source_language.txt', 'a+').read()
    TARGET_LANGUAGE = open('target_language.txt', 'a+').read()

    # Create input folder
    if not os.path.exists(input_path):
        os.makedirs(input_path)
        print("Created input folder, please add there the subtitles to translate and run again...")
        return

    # Init translator
    print("Started!")
    translator = deepl.Translator(DEEPL_AUTH_KEY)
    glossary = translator.create_glossary(name=GLOSSARY_NAME, source_lang=SOURCE_LANGUAGE, target_lang=TARGET_LANGUAGE, entries=GLOSSARY_ENTRIES)

    srt_files = get_srt_files(input_path)
    for srt_file in srt_files:
        print(f"Starting process for {srt_file}...")
        # Read Subtitle
        subtitlesData = read_SRT(os.path.join(input_path, srt_file))
        # Translate Subtitle
        subtitlesData = translate_subtitles(subtitlesData, translator, glossary, SOURCE_LANGUAGE, TARGET_LANGUAGE)
        # Save Translation
        write_SRT(subtitlesData, os.path.join(output_path, srt_file))
    print("Finished!")

if __name__ == "__main__":
    main()