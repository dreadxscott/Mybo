#dictionary_parser_service
import csv
import xml.etree.ElementTree as ET
import pandas as pd

class LoadDictionary():
    def parse_kanji_dictionary(self, file_path):
        # Store kanji entries as dictionaries in a list
        kanji_entries = []

        # Set up iterparse to process the file incrementally
        context = ET.iterparse(file_path, events=("start", "end"))
        _, root = next(context)  # Get the root element of the XML

        current_kanji = {}
        in_reading_meaning = False  # Track if we're inside a reading_meaning section

        # Iterate over each element in the XML file
        for event, elem in context:
            if event == 'start':
                # If it's a new kanji entry, initialize the dictionary
                if elem.tag == "character":
                    current_kanji = {
                        "kanji": "",
                        "onyomi": [],
                        "kunyomi": [],
                        "meaning": [],
                        "nanori": [],
                        "frequency": None
                    }
                elif elem.tag == "reading_meaning":
                    in_reading_meaning = True  # Now inside a reading/meaning section

            elif event == 'end':
                if elem.tag == "literal":
                    current_kanji["kanji"] = elem.text

                # Capture onyomi (Chinese readings)
                elif elem.tag == "reading" and elem.attrib.get("r_type") == "ja_on":
                    current_kanji["onyomi"].append(elem.text)

                # Capture kunyomi (Japanese readings)
                elif elem.tag == "reading" and elem.attrib.get("r_type") == "ja_kun":
                    current_kanji["kunyomi"].append(elem.text)

                # Capture meanings (default assumed to be English)
                elif elem.tag == "meaning" and "m_lang" not in elem.attrib:
                    current_kanji["meaning"].append(elem.text)

                # Capture nanori (name readings)
                elif elem.tag == "nanori":
                    current_kanji["nanori"].append(elem.text)

                # Capture frequency of the kanji (if available)
                elif elem.tag == "freq":
                    current_kanji["frequency"] = int(elem.text)

                # End of a kanji entry, append it to the list
                elif elem.tag == "character":
                    kanji_entries.append(current_kanji)
                    root.clear()  # Clear elements we've already processed to save memory

        return kanji_entries

# Example usage
if __name__ == "__main__":
    file_path = r"C:\Users\colli\Downloads\kanjidic2.xml\kanjidic2.xml"  # Replace with the actual path to your kanji dictionary file
    LD = LoadDictionary()
    kanji_data = LD.parse_kanji_dictionary(file_path)

    # Print a sample of parsed kanji entries
    for entry in kanji_data[:5]:
        print(f"Kanji: {entry['kanji']}, Onyomi: {entry['onyomi']}, Kunyomi: {entry['kunyomi']}, "
              f"Meanings: {entry['meaning']}, Nanori: {entry['nanori']}, Frequency: {entry['frequency']}")
        
        dict_df = pd.DataFrame(kanji_data).to_csv(r'C:\Users\colli\Python\Mybo\data\kanjidic2.csv',index=False)
