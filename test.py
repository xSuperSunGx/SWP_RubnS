
import os

#read file and replace string with new string
def replace(file_path, old_string, new_string):
      #Read contents from file as a single string
        file_handle = open(file_path, 'r')
        file_string = file_handle.read()
        file_handle.close()

        #Replace all occurrences of the required string
        file_string = file_string.replace(old_string, new_string)

        #Write the file out again
        file_handle = open(file_path, 'w')
        file_handle.write(file_string)
        file_handle.close()


if __name__ == '__main__':
    replace("ANA2Punktregelung", ".", ",")


