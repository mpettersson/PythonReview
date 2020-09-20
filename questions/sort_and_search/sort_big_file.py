"""
    SORT BIG FILE (CCI 10.6)

    Imagine you have a 20 GB file with one string per line.  Explain how you would sort the file.
"""
import os


# External Sort Approach:  Break the source file into temp files of size (bytes) limit, sort each temp file, then merge
# the lines into the dest file.
def sort_big_file(limit, source_file_name, dest_file_name, temp_file_name_prefix):
    if source_file_name is not None and os.path.isfile(source_file_name):
        source = open(source_file_name, mode='r')
        dest = open(dest_file_name, mode='w')
        temp_files = []
        text = source.readlines(limit)                  # Reads (at most) limit size from source.
        while len(text) > 0:                            # store sorted chunks into files of size n
            text.sort()
            temp_files.append(open(temp_file_name_prefix + str(len(temp_files)), mode='w+', encoding='utf-8'))
            temp_files[-1].writelines(text)
            temp_files[-1].seek(0)
            text = source.readlines(limit)
        min_list = [f.readline() for f in temp_files]   # List of first (smallest) lines
        while min_list:                                 # merge into dest
            c = min(min_list)
            dest.write(c)
            i = min_list.index(c)
            t = temp_files[i].readline()
            if t:
                min_list[i] = t
            else:
                del min_list[i]
                file_to_remove = temp_files[i].name
                temp_files[i].close()
                del temp_files[i]
                os.remove(file_to_remove)
        source.close()
        dest.close()


