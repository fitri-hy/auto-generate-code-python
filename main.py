import requests
from datetime import datetime

def generate_project(language, keyword):
    url = f"https://api.hy-tech.my.id/api/gemini/Write only the code in 1 file:{language}-{keyword}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        language_extensions = {
            "html": "html",
            "javascript": "js",
            "css": "css",
            "scss": "scss",
            "php": "php",
            "ejs": "ejs",
            "python": "py",
            "java": "java",
            "c": "c",
            "cpp": "cpp",
            "ruby": "rb",
            "swift": "swift",
            "typescript": "ts",
            "c#": "cs",
            "go": "go",
            "rust": "rs",
            "perl": "pl",
            "kotlin": "kt",
            "scala": "scala",
            "shell": "sh",
            "r": "r",
            "sql": "sql",
            "lua": "lua",
            "groovy": "groovy",
            "dart": "dart",
            "matlab": "m",
            "haskell": "hs",
            "assembly": "asm",
            "objective-c": "m",
            "fortran": "f90",
            "elixir": "ex",
            "clojure": "clj",
            "erlang": "erl",
            "scheme": "scm",
            "ocaml": "ml",
            "vb.net": "vb",
            "coffee-script": "coffee",
            "cobol": "cbl",
            "pascal": "pas",
            "lisp": "lisp",
            "prolog": "pl",
            "racket": "rkt",
            "d": "d",
            "apex": "cls",
            "julia": "jl",
            "ada": "ada",
            "dylan": "dylan",
            "smalltalk": "st",
            "abap": "abap",
            "forth": "forth",
            "vhdl": "vhdl",
            "verilog": "v",
            "awk": "awk",
            "sed": "sed",
            "actionscript": "as",
            "autohotkey": "ahk",
            "cmake": "cmake",
            "crystal": "cr",
            "makefile": "mk",
            "rexx": "rexx",
            "sas": "sas",
            "graphql": "graphql",
            "protobuf": "proto",
            "markdown": "md",
            "xml": "xml",
            "json": "json",
            "yaml": "yaml",
            "svg": "svg",
            "less": "less",
            "stylus": "styl",
            "pug": "pug",
            "handlebars": "hbs",
            "twig": "twig",
            "smarty": "tpl",
            "liquid": "liquid",
            "jade": "jade",
            "haml": "haml",
            "q#": "qs",
            "xbase": "prg"
        }
        if language in language_extensions:
            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            extension = language_extensions[language]
            filename = f"project_{current_time}.{extension}"
            with open(filename, "w") as file:
                file.write("\n".join([line for line in data["text"].split("\n") if not line.startswith("```")]))
            print(f"Hasil proyek telah disimpan dalam file {filename}")
        else:
            print("Ekstensi file untuk bahasa yang dipilih tidak ditemukan")
    else:
        print("Gagal mengakses API")

languages = [
             'html', 'javascript', 'css', 'scss',
             'php', 'ejs', 'python', 'java',
             'c', 'cpp', 'ruby', 'swift',
             'typescript', 'c#', 'go', 'rust',
             'perl', 'kotlin', 'scala', 'shell',
             'r', 'sql', 'lua', 'groovy',
             'dart', 'matlab', 'haskell', 'assembly',
             'objective-c', 'fortran', 'elixir', 'clojure',
             'erlang', 'scheme', 'ocaml', 'vb.net',
             'coffee-script', 'cobol', 'pascal', 'lisp',
             'prolog', 'racket', 'd', 'apex',
             'julia', 'ada', 'dylan', 'smalltalk',
             'abap', 'forth', 'vhdl', 'verilog',
             'awk', 'sed', 'actionscript', 'autohotkey',
             'cmake', 'crystal', 'makefile', 'rexx',
             'sas', 'graphql', 'protobuf', 'markdown',
             'xml', 'json', 'yaml', 'svg',
             'less', 'stylus', 'pug', 'handlebars',
             'twig', 'smarty', 'liquid', 'jade',
             'haml', 'q#', 'xbase'
]

# Fungsi untuk mencetak tabel dengan 4 kolom
def print_table(data, num_columns=4):
    max_length = max(len(item) for item in data)
    column_width = max_length + 4
    num_items = len(data)
    num_rows = -(-num_items // num_columns)  # Ceiling division

    for i in range(num_rows):
        row_items = data[i*num_columns:(i+1)*num_columns]
        row_formatted = [f"{i*num_columns+j+1}. {item:<{column_width}}" for j, item in enumerate(row_items)]
        print("".join(row_formatted))

print("Pilih bahasa untuk proyek:")
print_table(languages)

choice = int(input("Masukkan nomor bahasa: "))
if choice >= 1 and choice <= len(languages):
    chosen_language = languages[choice - 1]
    keyword = input("Jelaskan proyek Anda: ")
    generate_project(chosen_language, keyword)
else:
    print("Pilihan tidak valid")
