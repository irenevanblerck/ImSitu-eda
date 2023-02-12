import json
import shutil
import pandas as pd

def get_verb_agent(json_file, verb_custom, agent_custom):
    train = json.load(open(json_file))
    verb_value = []
    agent_key = []
    agent_value = []
    file_path = []
    count = 0
    for i in train:
        verb = train[i]['verb']
        if verb == verb_custom:
            frames = train[i]['frames']
            for frame in frames:
                for key, value in frame.items():
                    if key == 'agent':
                        if value in agent_custom:
                            if i not in file_path:
                                agent_key.append(key)
                                agent_value.append(value)
                                file_path.append(i)
                                verb_value.append(verb)
                                count += 1
                        else:
                            continue
                    else:
                        continue
    return(file_path, verb_value, agent_key, agent_value, count)

get_verb_agent('train.json', 'dusting', ['n10787470', 'n10287213'])

def img_to_folder(dirs_original, dirs_destination):
    image_list = get_verb_agent('train.json', 'dusting', ['n10787470', 'n10287213'])[0]
    dirs_list = [(dirs_original, dirs_destination)]
    for img in image_list:
        for source_folder, destination_folder in dirs_list:
            shutil.copy(source_folder+img, destination_folder+img)

img_to_folder("./data/original/", "./data/dusting/train/")

def lists_to_df(dirs_destination, col1_name, col2_name, col3_name):
    col1 = get_verb_agent('train.json', 'dusting', ['n10787470', 'n10287213'])[0]
    col2 = get_verb_agent('train.json', 'dusting', ['n10787470', 'n10287213'])[1]
    col3 = get_verb_agent('train.json', 'dusting', ['n10787470', 'n10287213'])[3]
    df = pd.DataFrame(list(zip(col1, col2, col3)), columns=[col1_name, col2_name, col3_name])
    df.to_csv(dirs_destination, index=False)
    return df

lists_to_df('./data/dusting/train/dusting_train.csv', 'file_name','verb', 'agent')