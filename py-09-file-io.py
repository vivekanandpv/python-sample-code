#   Opening a file
#   open(file_name) presumes, encoding, and mode
#   equivalent to open(file_name, 'r', encoding='utf-8')


file_handle = open('sample.txt')

#   reading a file by lines:
for line in file_handle.readlines():
    print(line)

#   close file as it is a system resource

file_handle.close()

# -------------------------------------------

#   context manager approach
with open('sample.txt', 'r', encoding='utf-8') as file_handle:
    for line in file_handle.readlines():
        print(line)

#   for binary files (images, pdf files, word files, multimedia files)
#   use binary mode prefix: rb, wb, etc
#   default mode presumes text
#   note that binary mode doesn't take encoding
with open('horses.jpeg', 'rb') as file_handle:
    for line in file_handle.readlines():
        print(line)

#   writing a text file
#   note the trailing \n character
#   w mode overwrites (opening handle is enough, not need to actually write)
#   also check a mode for appending at the end
content = 'The name that can be named is not the eternal name\n'
with open('content.txt', 'w') as write_file_handle:
    #   experiment with writelines(iterable)
    write_file_handle.write(content)
    write_file_handle.write('Bye bye\n')

#   exercise: write a file copier for text and binary files (solution attached - 02)
#   exercise: read from the attached csv file (MOCK_DATA.csv) and process data as a dictionary (solution attached - 03)
