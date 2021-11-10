import os

#   executing system commands
os.system('ls -la')

#   current working directory
print(os.getcwd())

#   creating path ()
temp_path = os.path.join('.', 'temp')

#   creating a directory
# os.mkdir(temp_path)

#   creating nested directories
#   os specific
nested_path = os.path.join('.', 'foo', 'bar', 'baz')
# os.makedirs(nested_path)

#   listing directories
bin_dir_list = os.listdir(os.path.join(os.sep, 'usr', 'bin'))

#   for removing file os.remove()
# os.remove(os.path.join('.', 'h2.jpeg'))
#   for removing directory os.rmdir()
# os.rmdir(os.path.join('.', 'foo', 'bar', 'baz'))

#   does this path exist?
print(os.path.exists(os.path.join(os.sep, 'usr')))  # /usr exists on unix

#   get the size
print(os.path.getsize(os.path.join(os.sep, 'usr', 'bin', 'clang++')))
