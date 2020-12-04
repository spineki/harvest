import os


def splitter(filename, MAX_SIZE=7):
    """
    filename to split: 
    MAX_SIZE en MO: default 7, adapted for discord
    """

    MAX_SIZE = MAX_SIZE * 1024 * 1024

    start_index = 0
    
    data = None

    nb_fichier = 0

    with open(filename, "rb") as fin:
        while data != b'':
            fin.seek(start_index)
            data = fin.read(MAX_SIZE)

            if data == b'':
                break

            start_index += MAX_SIZE

            with open(str(start_index) + "_" + filename, "wb") as ouput:
                ouput.write(data)
            nb_fichier += 1
    print("Finis!! en ", nb_fichier, " fichiers")


def binder(folder_name, output_name="output.exe"):
    files = os.listdir(folder_name)

    files = sorted(files, key=lambda x: int(x.split("_")[0]))

    for file in files:
        print(file)

    with open(output_name, "wb+") as output:

        for file in files:
            with open(os.path.join(folder_name, file), "rb") as input:
                output.write(input.read())
    print("Fini!")


if __name__ == "__main__":
    # Programme principal. Retirer le # devant la ligne pour lancer la commande

    # splitter("Votre nom de fichier avec l'extension")
    # binder("mon nom de dossier", "ouput.exe")
    pass
