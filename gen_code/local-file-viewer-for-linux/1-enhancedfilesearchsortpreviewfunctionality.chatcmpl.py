# Add a search functionality
def search_files(directory, keyword):
    result = []
    for dirpath, _, files in os.walk(directory):
        for file in files:
            if keyword in file:
                result.append(os.path.join(dirpath, file))
    return result

# Sort files and directories
def sort_files(directory, criteria):
    files = os.listdir(directory)
    if criteria == 'name':
        return sorted(files)
    elif criteria == 'size':
        return sorted(files, key=lambda x: os.path.getsize(os.path.join(directory, x)))
    elif criteria == 'date_modified':
        return sorted(files, key=lambda x: os.path.getmtime(os.path.join(directory, x)))

# Preview function
def preview_file(file_path):
    if platform.system() == 'Linux':
        os.system('xdg-open '+file_path)

# Main program
def main():
    directory = '/path/to/directory'

    # Search files
    search_keyword = 'keyword'
    search_result = search_files(directory, search_keyword)
    print('Search results:', search_result)

    # Sort files
    sort_criteria = 'name'
    sorted_files = sort_files(directory, sort_criteria)
    print('Sorted files:', sorted_files)

    # Preview file
    file_to_preview = '/path/to/file'
    preview_file(file_to_preview)

if __name__ == '__main__':
    main()
