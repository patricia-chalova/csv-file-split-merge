# csv-file-split-merge

## Split
Function `def splitter` will split given csv file by chosen split type and the variable to split by. Split types are: rows, size, nums. **Rows** - takes an integer argument to indicate the number of rows in the new files. **Size** file will be split into multiple files with maximum given size. **Nums** will split the file into x files where x is provided as an argument.

Arguments: splitter(file location, header present ['yes', 'no'], split type ['rows, 'size', 'nums'], split variable int, size unit ['B', 'KB', 'MB', 'GB', 'TB'], destination folder, file name)

### Rows 
Let's say we want to split file.csv of 10K rows by 2000 rows, so that each files has no more than 200 rows

Calling `splitter(r'C:\path\to\file.csv', 'yes', 'rows', 2000, 'none' , r'C:\path\to\folder', 'my_new_file')` will create 5 new files each containing max 2000 rows.
```
result in C:\path\to\folder
my_new_file_1.csv
my_new_file_2.csv
my_new_file_3.csv
my_new_file_4.csv
my_new_file_5.csv
```

### Size

Calling `splitter(r'C:\path\to\file.csv', 'yes', 'size', 100, 'KB', r'C:\path\to\folder', 'my_new_file')` will split the file by 100KB

### Nums

Calling `splitter(r'C:\path\to\file.csv', 'yes', 'nums', 5, 'none', r'C:\path\to\folder', 'my_new_file')` will create 5 files


## Merge
Function `def merge` merges files located in the same directory into one file.

Arguments: merge(source location, destination folder, new file name)

### Example

Calling `merge(r'C:\path\to\folder', r'C:\path\to\folder', 'new_file')` will merge all files in C:\path\to\folder and create a new_file.csv in C:\path\to\folder
