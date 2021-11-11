#   create an empty map
data_for_processing = {}    # this creates an empty map

#   open file
with open('MOCK_DATA.csv', 'r') as file_handle:
    #   get the first row which contains comma-separated headers
    #   using list comprehension with string splitting
    header_row = [header for header in file_handle.readline().split(',')]

    #   using enumerate and tuple unpacking just in case you need index for some reason
    #   readlines() skips the header row as it is already read above
    for index, line in enumerate(file_handle.readlines()):
        #   this is dictionary comprehension
        #   zip() returns the tuple containing corresponding elements of header and line
        #   for example, if you zip([1, 2, 3], ['a', 'b', 'c']) you get (1, 'a'), (2, 'b'), ...
        #   for map comprehension I used entry[0] as the key and entry[1] as the value
        entry = {entry[0]: entry[1]
                 for entry in zip(header_row, line.split(','))}

        #   for every entry (a dictionary itself), I am creating an k-v pair in my main dictionary
        #   for key I chose email
        #   This may not be prudent in all cases, as you may have duplicates in some context
        #   in such cases, you may use index defined earlier as the key

        #   Thus data_for_processing essentially becomes a dictionary of dictionaries
        data_for_processing[entry['email']] = entry

print(len(data_for_processing))
