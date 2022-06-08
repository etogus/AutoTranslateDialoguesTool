import requests

if __name__ == '__main__':
    try:
        IAM_TOKEN = 't1.9euelZrNj5ieyZfPzJiNk4-Sj5WQnO3rnpWazpnLxpaVnYqXlJGPypObzYrl8_cOfgBr-e9tDGJZ_t3z904sfmr5720MYln-.PybmYL0ED3JpwnNrLd7MmLkQUawQoSPtsM2UeYe9Qu7FnEOv0rTvv1Kqc4Tz9va9QJlT7VFgsDhnT5NfQyWaDQ'
        folder_id = 'b1gmoi0vh9lgiadfa59f'
        target_language = 'en'
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {0}".format(IAM_TOKEN)
        }
        ru_file = open('ruRenPy.txt', 'w')
        with open('engRenPy.txt', 'r') as reader:
            line = reader.readline()
            while line != '':
                if 'TODO' in line or 'translate' in line or 'rpy:' in line or len(line) <= 2 and '\n' in line:
                    ru_file.write(line)
                else:
                    if '#' in line:
                        isAuthor = False
                        index = 6
                        name = ""
                        if not line[index].isalpha():
                            isAuthor = True
                        if not isAuthor:
                            while line[index].isalpha():
                                name = name + line[index]
                                index = index + 1
                            index = index + 2
                            edit_line = line[index:].replace('"', "").replace('\n', "")
                        else:
                            edit_line = line[index:].replace('"', "").replace('\n', "")
                        print(line)
                        texts = [edit_line]
                        body = {
                            "targetLanguageCode": target_language,
                            "texts": texts,
                            "folderId": folder_id,
                        }

                        #response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                        #                         json=body,
                        #                         headers=headers
                        #                         )
                        ru_file.write(line)
                        if not isAuthor:
                            ru_file.write(" " + " " + " " + " " + name + " " + '"' + edit_line + '"' + "\n")
                        else:
                            ru_file.write(" " + " " + " " + " " + '"' + edit_line + '"' + "\n")
                line = reader.readline()

    finally:
        ru_file.close()
