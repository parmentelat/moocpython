#!/usr/bin/env python3

from pathlib import Path
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


# comme on ne peut plus ranger les titres de chapitre dans Python.tex
# on les met dans un fichier à part

def read_title(target_week):
    with open("00-chapter-names.txt") as feed:
        for line in feed:
            week, title = line.split(':')
            iweek = int(week)
            if iweek == target_week:
                return title.strip()
    return f"Titre pas trouvé pour semaine {target_week}"


# on retrouve les noms des notebooks appartenant à une semaine
# grâce à un simple pattern matching sur les w<i>-s*.tex
def notebook_names(target_week):
    pattern = f"w{target_week}-s*.tex"
    for nbpath in Path('.').glob(pattern):
        yield nbpath.stem


# créer le fichier .tex qui contient ce qu'on veut montrer
def write_output(w_from, w_to, outputname):
    with open(outputname, "w") as output:
        for index, week in enumerate(range(w_from, w_to+1)):
            title = read_title(week)

            # index == 0 correspond au premier chapitre dans le .tex
            if index == 0:
                # ajuter le numéro du chapitre = numéro de semaine
                output.write(rf"\setcounter{{chapter}}{{{w_from-1}}}" "\n")
            output.write("\n" rf"\chapter{{{title}}}" "\n")
            if index == 0:
                output.write(r"\pagestyle{plain}" "\n")
                output.write(r"\setcounter{page}{1}" "\n")

            # les notebooks du chapitre
            for notebook in notebook_names(week):
                output.write(rf"\input{{{notebook}}}" "\n")


# ya plus qu'à
def main():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--from', dest='w_from', type=int, default=1,
                        help='first week')
    parser.add_argument('-t', '--to', dest='w_to', type=int, default=9,
                        help='last week')
    parser.add_argument('-o', '--output', default="contenu.tex",
                        help='output tex')

    args = parser.parse_args()
    write_output(args.w_from, args.w_to, args.output)


if __name__ == '__main__':
    main()
