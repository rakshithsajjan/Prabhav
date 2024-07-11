def get_file_names_of_corrupt():
    import os
    file_names = set()
    for filename in os.listdir('data'):
        if filename.endswith('.md'):
            with open(os.path.join('data', filename), 'r') as file:
                content = file.read()
                if "<!DOCTYPE html>" in content or "InsufficientBalanceError" in content or '"data":null' in content or "low down, turbo! You've hit the rate limit" in content:
                    file_names.add(filename[:-3])
                    os.remove(os.path.join('data', filename))

    with open('rescrape.txt', 'w') as output_file:
        for name in file_names:
            output_file.write(name + '\n')


def cross_check_slugs():
    import os
    with open('slugs.txt', 'r') as slugs_file:
        slugs = set(slugs_file.read().splitlines())

    existing_files = {filename[:-3] for filename in os.listdir('data') if filename.endswith('.md')}
    missing_slugs = slugs - existing_files

    with open('rescrape.txt', 'a') as rescrape_file:
        for slug in missing_slugs:
            rescrape_file.write(slug + '\n')


if __name__ == "__main__":
    cross_check_slugs()
