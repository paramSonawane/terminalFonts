 #!/usr/bin/python
import sys,os
import ANSI_Fonts

Font = ANSI_Fonts.ANSI_Shadow

def printInFont(str):
    theStr = "";
    for i in range(6):
        for j in range(len(str)):
            theStr += Font[ord(str[j])-97][i] + " "
        theStr += "\n"
    return theStr;

def main(arg):
    print(printInFont(arg[0]));


if __name__ == "__main__":
    main(sys.argv[1:])