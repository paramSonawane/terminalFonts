 #!/usr/bin/python
import sys,os
import ANSI_Fonts

Font = ANSI_Fonts.ANSI_Shadow


def printInFont(str) :
    outStr = commentChar;
    for i in range(6):
        for j in range(len(str)):
            outStr += (Font[ord(str[j])-97][i]).rjust(4, 'p');

        outStr += "\n" + commentChar;
    return outStr;

def printHelp():
    print("""

Usage: genearateTFont.py [options] text
Options :
    -c  | --comment     <commentCharacter/(s)>  Comment Character to precede each line with
    -f  | --font        <fontName>              Name of font to be used (see -lf for list of all fonts)
    -h  | --help                                This help menu
    -lf | --list-fonts                          Lists all fonts
    -s  | --spaces      <numberOfSpaces>        Number of spaces to be given between characters
    """
    )

def parseParameters(args):
    for i in range(len(args)) :

        if(args[i] == "-c" or args[i] == "--comment"):
            try:
                commentChar = args[i+1];
                i+=1;
                print("Info : Comment chars detected : " + commentChar);
            except:
                print("\n\nError : No argument provided for " + args[i] + "\nNot preceding with any comment character")

        elif(args[i] == "-s" or args[i] == "--spaces"):
            try:
                for i in range(int(args[i+1])):
                    spaces = spaces + ' ';
                print("Info  : Spaces are " + str(spaces) + " long");
            except ValueError:
                print("\n\nError : Invalid argument at " + args[i] + " " + args[i+1] + "\nSpaces must be defined in Integers, Defaulting to 1 space");
            i+=1;
        elif(args[i] == "-h" or args[i] == "--help"):
            printHelp();
            exit();

def main(args) :
    commentChar = ""
    spaces = ' '
    
    parseParameters(args);

    print(printInFont(args[-1]));

if __name__ == "__main__" :
    if(len(sys.argv) < 2) :
        print("Error : Insufficient Parameters");
        printHelp();
        print("Exiting...");
        exit();
    else :
        main(sys.argv[1:]);
        # print(sys.argv)