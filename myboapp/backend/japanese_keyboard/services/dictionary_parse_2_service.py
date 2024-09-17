#dictionary parser 2
import xml.etree.cElementTree as ET
import pandas as pd

class ParseDictionary():
    
    def parse_jmdict(self, file_path):
        # List to store the parsed entries
        parsed_entries = []

        # Set up iterparse to process the file incrementally
        context = ET.iterparse(file_path, events=("start", "end"))
        _, root = next(context)  # Get the root element

        current_entry = {}
        in_sense = False  # Track if we're inside a <sense> element

        # Iterate over each element in the XML file
        for event, elem in context:
            if event == 'start':
                # Start a new entry when encountering <entry>
                if elem.tag == "entry":
                    current_entry = {
                        "ent_seq": None,
                        "kanji": [],
                        "reading": [],
                        "part_of_speech": [],
                        "gloss": [],
                        "source_lang": [],
                        "sense_info": []
                    }

            elif event == 'end':
                if elem.tag == "ent_seq":
                    current_entry["ent_seq"] = elem.text

                # Capture kanji elements
                elif elem.tag == "keb":
                    current_entry["kanji"].append(elem.text)

                # Capture reading elements (kana readings)
                elif elem.tag == "reb":
                    current_entry["reading"].append(elem.text)

                # Capture part of speech information
                elif elem.tag == "pos":
                    current_entry["part_of_speech"].append(elem.text)

                # Capture English glosses (default)
                elif elem.tag == "gloss":
                    lang = elem.attrib.get('{http://www.w3.org/XML/1998/namespace}lang', "eng")
                    if lang == "eng":
                        current_entry["gloss"].append(elem.text)
 
                # Capture sense information (s_inf)
                elif elem.tag == "s_inf":
                    current_entry["sense_info"].append(elem.text)

                # Capture loanword source language (English is default, others may be indicated)
                elif elem.tag == "lsource":
                    lang = elem.attrib.get("xml:lang", "eng")
                    source_word = elem.text
                    if lang != "eng" and source_word:
                        current_entry["source_lang"].append((lang, source_word))

                # End of an entry, append to the list and clear the root
                elif elem.tag == "entry":
                    parsed_entries.append(current_entry)
                    root.clear()  # Clear the processed elements to save memory

        return parsed_entries
    
    def find_lang(self, file_path):
        # Set up iterparse to process the file incrementally
        context = ET.iterparse(file_path, events=("start", "end"))
        _, root = next(context)  # Get the root element

        # Iterate over each element in the XML file
        for event, elem in context:
            if event == 'end' and elem.tag == 'gloss':
                # Check if xml:lang attribute is missing (implying it's English)
                lang = elem.attrib.get('{http://www.w3.org/XML/1998/namespace}lang', "eng")
                if lang == "eng":
                    print(f"English gloss: {elem.text}")

            # Clear root after processing an element
            if event == 'end' and elem.tag == "entry":
                root.clear()  # Clear processed elements to save memory



# Example usage
if __name__ == "__main__":
    file_path = r"C:\Users\colli\Downloads\JMdict\jmdict.xml"  # Replace with the actual path to the JMdict file
    PD =ParseDictionary()
    jmdict_data = PD.parse_jmdict(file_path)

    # Print a sample of parsed entries
    for entry in jmdict_data[100:200]:
        print(f"Entry: {entry['ent_seq']}")
        print(f"Kanji: {entry['kanji']}")
        print(f"Reading: {entry['reading']}")
        print(f"Part of Speech: {entry['part_of_speech']}")
        print(f"Glosses (English): {entry['gloss']}")
        print(f"Source Languages: {entry['source_lang']}")
        print(f"Sense Info: {entry['sense_info']}")
    

    #dict_df = pd.DataFrame(jmdict_data).to_csv(r'C:\Users\colli\Python\Mybo\data\jmdict.csv',index=False)


