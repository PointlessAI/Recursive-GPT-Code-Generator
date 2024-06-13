import os
import platform

def search_files(directory, keyword):
    result = []
    if not os.path.exists(directory):
        return result
    for dirpath, _, files in os.walk(directory):
        for file in files:
            if keyword in file:
                result.append(os.path.join(dirpath, file))
    return result

def sort_files(directory, criteria):
    if not os.path.exists(directory):
        return []
    
    files = os.listdir(directory)
    if criteria not in ['name', 'size', 'date_modified']:
        raise ValueError("Invalid sorting criteria")
    
    if criteria == 'name':
        return sorted(files)
    elif criteria == 'size':
        return sorted(files, key=lambda x: os.path.getsize(os.path.join(directory, x)))
    elif criteria == 'date_modified':
        return sorted(files, key=lambda x: os.path.getmtime(os.path.join(directory, x)))

def preview_file(file_path):
    if platform.system() == 'Linux':
        os.system('xdg-open '+file_path)

def main():
    directory = input("Enter directory path: ")
    search_keyword = input("Enter search keyword: ")
    sort_criteria = input("Enter sorting criteria (name/size/date_modified): ")
    
    search_result = search_files(directory, search_keyword)
    print('Search results:', search_result)
    
    sorted_files = sort_files(directory, sort_criteria)
    print('Sorted files:', sorted_files)
    
    file_to_preview = input("Enter file path to preview: ")
    preview_file(file_to_preview)

if __name__ == '__main__':
    main()
