import requests

if __name__ == '__main__':
    try:
        IAM_TOKEN = 't1.9euelZrOyI-MxomPzpaOlY2cnZvPlO3rnpWazpnLxpaVnYqXlJGPypObzYrl8_dZUnxq-e9uOjEY_t3z9xkBemr57246MRj-.-cHdb7LvSaFmTJk-blrNeWUtwwsbBSRpOyqIPljBeuA0oZbTfsFrDYpnLjftzpGkiSrGIWUB1crrqk_QhYSfBw'
        folder_id = 'b1gmoi0vh9lgiadfa59f'
        target_language = 'ru'
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
                        #print(line)
                        texts = [edit_line]
                        body = {
                            "targetLanguageCode": target_language,
                            "texts": texts,
                            "folderId": folder_id,
                        }

                        response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                                                 json=body,
                                                 headers=headers
                                                 )
                        ru_file.write(line)
                        #print(response.text)
                        text_index = response.text.find("text")
                        #print(text_index)
                        text_index = text_index + 8
                        #print(text_index)
                        #print(response.text[text_index:])
                        end_index = response.text[text_index:].find('"')
                        #print(end_index)
                        result_text = response.text[text_index:text_index+end_index]
                        #print(result_text)
                        if not isAuthor:
                            ru_file.write(" " + " " + " " + " " + name + " " + '"' + result_text + '"' + "\n")
                        else:
                            ru_file.write(" " + " " + " " + " " + '"' + result_text + '"' + "\n")
                line = reader.readline()

    finally:
        ru_file.close()
