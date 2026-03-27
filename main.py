import ollama, shutil, os
from pathlib import Path

def main(pathFile, count_all, count, error_first):
    print(f"analizing: {pathFile} {count}/{count_all}")

    response = ollama.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': 'Identify if the primary object in the image is a product, note, book, or similar. Respond with the character Y or N.',
            'images': [pathFile]
        }]
    )

    logic(response, pathFile, error_first, count_all, count)


def logic(response, pathFile, error_first, count_all, count):

    if response['message']['content'] == "N":

        print(f"proceded with {pathFile} to N")
        move_files(pathFile, "photos_trash")

    elif response['message']['content'] == "Y":

        print(f"proceded with {pathFile} to Y")
        move_files(pathFile, "photos_output")

    else:
        if error_first:

            print(f"Error in response for {pathFile}. Response was: {response['message']['content']} first time. Retrying...")
            main(pathFile, count_all, count, False)

        else:

            print(f"Error in response for {pathFile}. Response was: {response['message']['content']} second time. Moving to error folder.")
            move_files(pathFile, "photos_error")


def move_files(pathFile, adress):

    shutil.move(pathFile, f"{adress}/{pathFile.name}")

    if os.path.exists(f"photos_input/{pathFile.stem}.MOV"):
        shutil.move(f"photos_input/{pathFile.stem}.MOV", f"{adress}/{pathFile.stem}.MOV")
    
    if os.path.exists(f"photos_input/{pathFile.stem}.mov"):
        shutil.move(f"photos_input/{pathFile.stem}.mov", f"{adress}/{pathFile.stem}.mov")
    
    if os.path.exists(f"photos_input/{pathFile.stem}.CR2"):
        shutil.move(f"photos_input/{pathFile.stem}.CR2", f"{adress}/{pathFile.stem}.CR2")

    if os.path.exists(f"photos_input/{pathFile.stem}.cr2"):
        shutil.move(f"photos_input/{pathFile.stem}.cr2", f"{adress}/{pathFile.stem}.cr2")