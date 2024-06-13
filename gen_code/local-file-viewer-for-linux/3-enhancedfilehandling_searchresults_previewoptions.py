import os
import platform

def search_files(directory, keyword):
    result = []
    if not os.path.exists(directory):
        print("Error: Directory does not exist")
        return result
    
    for dirpath, _, files in os.walk(directory):
        for file in files:
            if keyword in file:
                result.append(os.path.join(dirpath, file))
    return result

def sort_files(directory, criteria):
    if not os.path.exists(directory):
        print("Error: Directory does not exist")
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

def preview_file(file_path, file_viewer='xdg-open'):
    if platform.system() == 'Linux':
        os.system(f'{file_viewer} {file_path}')

def main():
    directory = input("Enter directory path: ")
    while not os.path.exists(directory):
        print("Error: Directory does not exist")
        directory = input("Enter a valid directory path: ")
    
    search_keyword = input("Enter search keyword: ")
    sort_criteria = input("Enter sorting criteria (name/size/date_modified): ")
    
    search_result = search_files(directory, search_keyword)
    
    num_results = int(input("Enter the number of search results to display: "))
    print('Search results:', search_result[:num_results])
    
    sorted_files = sort_files(directory, sort_criteria)
    print('Sorted files:', sorted_files)
    
    file_to_preview = input("Enter file path to preview: ")
    
    file_viewer_choice = input("Choose a file viewer (xdg-open/evince/ImageMagick): ")
    if file_viewer_choice in ['xdg-open', 'evince', 'ImageMagick']:
        preview_file(file_to_preview, file_viewer_choice)
    else:
        print("Invalid file viewer choice. Using default viewer.")
        preview_file(file_to_preview)

if __name__ == '__main__':
    main()
