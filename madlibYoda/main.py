import json
import os  

class MadLibs:
    
    def __init__(self, word_descriptions, template):
        self.template = template
        self.word_descriptions = word_descriptions
    
    @classmethod
    def from_json(cls, name, path="./template"):
        fpath = os.path.join(path, name)
        with open(fpath, "r") as f:
            data = json.load(f)
        mad_lib = cls(**data)
        return mad_lib



def get_words_from_user(word_descriptions):
    words = []
    print("Please provide the following words: ")
    for desc in word_descriptions:
        user_input = input(desc + " ")
        words.append(user_input)
    return words

def build_story(template, words):
    story = template.format(*words)
    return story



temp_name = "starwars_yoda.json"
mad_lib = MadLibs.from_json(temp_name)
words = get_words_from_user(mad_lib.word_descriptions)
story = build_story(mad_lib.template, words)

print(story)




# madlib used https://i.pinimg.com/originals/fd/23/66/fd23666f50c74cb02407a6b5c5ff282d.jpg
# Teacher Kevin Fortier "https://www.youtube.com/channel/UCU1XO9F7XpXC6Z9QbiKTZCQ"
