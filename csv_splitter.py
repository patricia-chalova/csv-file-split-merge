import pandas as pd
import math
import os
import subprocess


def splitter(file_loc, header, split_type, split_var, size_unit,new_file_loc, new_file_name):

    header = header.lower()
    split_type = split_type.lower()
    split_var = split_var
    size_unit = size_unit.lower()
    new_file_loc = new_file_loc.lower()
    new_file_name = new_file_name.lower()

    if header == 'no':
        df1 = pd.read_csv(file_loc, header=None, skiprows=1)
    else:
        df1 = pd.read_csv(file_loc)

    if split_type == 'size':
        file_size = os.path.getsize(file_loc)
        byte_dict = {'B': 1, 'KB': 1024, 'MB': 1024 ^ 2, 'GB': 1024 ^ 3, 'TB': 1024 ^ 4}
        byte_var = byte_dict[size_unit]
        split_var = math.ceil(file_size / (byte_var*split_var))

    if split_type in ('nums', 'size'):
        split_var = math.floor(df1.shape[0] / split_var)

    split_var = int(split_var)
    start = 0
    end = split_var
    it_counter = 0

    while end <= df1.shape[0]:
        df_split = df1[start:end]
        start = end
        if end + split_var > df1.shape[0] or (end + 1) + split_var > df1.shape[0]:
            end = df1.shape[0]
        else:
            end = (start + 1) + split_var
        it_counter += 1

        df_split.to_csv(new_file_loc + '\\' + new_file_name + '_' + str(it_counter) + '.csv', index=False)

        if start == df1.shape[0]:
            break

    return subprocess.Popen(f'explorer {new_file_loc}')


def merge(source_loc, final_dest, new_file_name):

    source_loc = source_loc.lower()
    final_dest = final_dest.lower()
    new_file_name = new_file_name.lower()


    os.chdir(source_loc)

    df_from_each_file = (pd.read_csv(f) for f in os.listdir(source_loc))

    concatenated_df = pd.concat(df_from_each_file, ignore_index=True)
    concatenated_df.to_csv(final_dest + '\\' + new_file_name + '_merge' + '.csv')


    return subprocess.Popen(f'explorer {final_dest}')

