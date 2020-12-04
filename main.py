import os
from typing import List


def splitter(file_name: str, MAX_SIZE: int = 7):
    """
    Take file_name as input an split it in chucks of size MAX_SIZE. 

    file_name to split: 
    MAX_SIZE: MB size: default 7 MB
    """

    # convertion to MB
    MAX_SIZE = MAX_SIZE * 1024 * 1024

    # index go throught the bit stream
    start_index: int = 0

    # harvested data
    data: bytes = None

    created_files: int = 0

    with open(file_name, "rb") as input_stream:
        # while we didn't go out the file
        while data != b'':
            # we place the cursor at start index
            input_stream.seek(start_index)
            # read a chunk of size MAX_SIZE bytes
            data = input_stream.read(MAX_SIZE)

            if data == b'':
                break
            # then we open an output file
            with open(str(start_index) + "_" + file_name, "wb") as ouput_stream:
                # A write the related chunk in it
                ouput_stream.write(data)

            created_files += 1

            # we translate the cursor
            start_index += MAX_SIZE

    print("Done! ", created_files, " files created")


def binder(folder_name: str, output_name: str = "output.exe", verbose=True):
    """
    Merge all the files from folder_name into a file output_name. Display additional data if verbose=True
    """

    # we get all the files from the given  folder
    files: List[str] = os.listdir(folder_name)

    if files == []:
        print(" No file in ", folder_name, " folder")
        return

    # we sort then by comparing the concatenated number
    files = sorted(files, key=lambda x: int(x.split("_")[0]))

    if verbose:
        print("encoutered {} files:".format(len(files)))
        for file in files:
            print(file)

    # we open an output stream
    with open(output_name, "wb+") as output_stream:
        # And for every gathered files
        for file in files:
            with open(os.path.join(folder_name, file), "rb") as input:
                # we add it at the end of the document
                output_stream.write(input.read())

    print("Done!")


if __name__ == "__main__":
    # Programme principal. Retirer le # devant la ligne pour lancer la commande

    # splitter("Votre nom de fichier avec l'extension")
    # binder("mon nom de dossier", "ouput.exe", verbose=True)
    pass
