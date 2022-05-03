import os
import sys



def main():
    # Get command line arguments
    args = sys.argv[1:]
    fileNameToCreate = args[0]

    # Get current workng directory
    currentDir = os.getcwd()

    creationPath = os.path.join(currentDir, fileNameToCreate)

    os.system(f"type nul > {creationPath}")



if __name__ == '__main__':
	main()