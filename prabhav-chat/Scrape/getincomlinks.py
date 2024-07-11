def get_file_names():
    import os
    file_names = []
    for filename in os.listdir('data'):
        if filename.endswith('.md'):
            with open(os.path.join('data', filename), 'r') as file:
                content = file.read()
                if "<!DOCTYPE html>" in content or "InsufficientBalanceError" in content:
                    file_names.append(filename[:-3])

    with open('rescrape.txt', 'w') as output_file:
        for name in file_names:
            output_file.write(name + '\n')



if __name__ == "__main__":
    get_file_names()
