import requests

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def get_word_data(word):
    try:
        response = requests.get(API_URL + word)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None

def display_word_details(word_data):
    if not word_data:
        print("No information available for this word.")
        return

    meanings = word_data[0].get('meanings', [])
    print(f"\nWord: {word_data[0]['word'].capitalize()}\n")

    for meaning in meanings:
        print(f"Part of Speech: {meaning['partOfSpeech']}")
        definitions = meaning['definitions']
        for index, definition in enumerate(definitions, 1):
            print(f"  {index}. Definition: {definition['definition']}")
            if 'example' in definition:
                print(f"     Example: {definition['example']}")
            if 'synonyms' in definition:
                print(f"     Synonyms: {', '.join(definition['synonyms'])}")
        print("\n")

def main():
    print("Welcome to KiruuDefine.")
    while True:
        word = input("\nPlease enter a word (or type 'exit' to terminate): ").strip()
        if word.lower() == 'exit':
            print("Thank you for using KiruuDefine. Goodbye.")
            break

        word_data = get_word_data(word)
        if word_data:
            display_word_details(word_data)
        else:
            print(f"Unable to retrieve data for '{word}'.")

if __name__ == "__main__":
    main()
