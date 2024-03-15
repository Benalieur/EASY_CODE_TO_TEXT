import os
import fnmatch


# Dictionnaire des extensions de fichier et de leur langage de programmation associé
EXTENTION_LANGUAGE = {
    '.py': 'py',
    '.js': 'js',
    '.html': 'html',
    '.css': 'css',
    '.java': 'java',
    '.yml': 'yml',
}


def read_ignore_patterns(ignore_file_path):
    with open(ignore_file_path, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]


def is_ignored(path, ignore_patterns, root):
    for pattern in ignore_patterns:
        # Construire le chemin relatif pour le test et pour les motifs de dossier
        rel_path = os.path.relpath(path, root)
        if fnmatch.fnmatch(rel_path, pattern) or fnmatch.fnmatch(os.path.basename(path), pattern):
            return True
    return False


def read_and_combine_files(input_directory, output_file, ignore_file_path):
    input_directory = os.path.abspath(input_directory)
    ignore_patterns = read_ignore_patterns(ignore_file_path)

    if not os.path.isdir(input_directory):
        print(f"Le répertoire spécifié n'existe pas : {input_directory}")
        return
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(input_directory, topdown=True):
            # Filtrer les dossiers ignorés
            dirs[:] = [d for d in dirs if not is_ignored(os.path.join(root, d), ignore_patterns, input_directory)]

            for file in files:
                file_path = os.path.join(root, file)
                if is_ignored(file_path, ignore_patterns, input_directory):
                    continue  # Ignorer le fichier
                
                relative_path = os.path.relpath(file_path, input_directory)
                _, extension = os.path.splitext(file)
                language = EXTENTION_LANGUAGE.get(extension, '')

                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(f"---\nChemin: {relative_path}\nLangage: {language}\n---\n")
                        outfile.write(f"```{language}\n")
                        outfile.write(content)
                        outfile.write("\n```\n\n")
                except Exception as e:
                    print(f"Impossible de lire le fichier {file_path}: {e}")



if __name__ == '__main__':

    project_path = '.'
    output_file = './code_to_text_project.txt'
    ignore_file = './CodeToTextIgnore.txt'

    read_and_combine_files(project_path, output_file, ignore_file)