#   making use of function abstraction
#   using default arguments
#   don't handle the exceptions inside the function! why?
def copy_file(src_file_name, tgt_file_name, is_binary=False):
    '''This function copies file'''  # doc string must be the first line
    mode = 'b' if is_binary else ''  # this is ternary expression

    #   multiple resources handled by the same context manager
    #   \ allows to put the continuation on next line (indentation doesn't matter)
    #   making use of formatted strings
    with open(src_file_name, f'r{mode}') as src_file_handle,\
            open(tgt_file_name, f'w{mode}') as tgt_file_handle:
        #   writelines takes any iterable
        tgt_file_handle.writelines(src_file_handle.readlines())


copy_file('sample.txt', 's2.txt')   # text file copy
copy_file('horses.jpeg', 'h2.jpeg', is_binary=True)  # binary file copy
