import os
import mimetypes
import shutil

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTreeView, QFileSystemModel, QVBoxLayout, 
    QPushButton, QWidget, QInputDialog, QMessageBox
)

class FileManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Local File Manager")
        self.setGeometry(100, 100, 800, 600)

        self.model = QFileSystemModel()
        self.model.setRootPath("")

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(""))

        self.create_button = QPushButton("Create Folder")
        self.create_button.clicked.connect(self.create_folder)

        self.rename_button = QPushButton("Rename File/Folder")
        self.rename_button.clicked.connect(self.rename_file_folder)

        self.delete_button = QPushButton("Delete File/Folder")
        self.delete_button.clicked.connect(self.delete_file_folder)

        self.file_details_button = QPushButton("File Details")
        self.file_details_button.clicked.connect(self.show_file_details)

        self.search_button = QPushButton("Search Files")
        self.search_button.clicked.connect(self.search_files)

        self.compress_button = QPushButton("Compress Files")
        self.compress_button.clicked.connect(self.compress_files)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tree)
        self.layout.addWidget(self.create_button)
        self.layout.addWidget(self.rename_button)
        self.layout.addWidget(self.delete_button)
        self.layout.addWidget(self.file_details_button)
        self.layout.addWidget(self.search_button)
        self.layout.addWidget(self.compress_button)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

    def create_folder(self):
        folder_name, ok = QInputDialog.getText(self, 'Create Folder', 'Enter folder name:')
        if ok and folder_name:
            current_path = self.model.fileInfo(self.tree.currentIndex()).absoluteFilePath()
            new_folder_path = os.path.join(current_path, folder_name)
            os.makedirs(new_folder_path)
            self.model.setRootPath("")  
            self.tree.setRootIndex(self.model.index(""))

    def rename_file_folder(self):
        file_item = self.model.fileInfo(self.tree.currentIndex())
        old_path = file_item.absoluteFilePath()
        new_name, ok = QInputDialog.getText(self, 'Rename File/Folder', 'Enter new name:')
        if ok and new_name:
            new_path = os.path.join(os.path.dirname(old_path), new_name)
            os.rename(old_path, new_path)
            self.model.setRootPath("")  
            self.tree.setRootIndex(self.model.index(""))

    def delete_file_folder(self):
        file_item = self.model.fileInfo(self.tree.currentIndex())
        file_path = file_item.filePath()
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        else:
            os.remove(file_path)
        self.model.setRootPath("")  
        self.tree.setRootIndex(self.model.index(""))

    def show_file_details(self):
        selected_file_info = self.model.fileInfo(self.tree.currentIndex())
        file_path = selected_file_info.filePath()
        file_size = os.path.getsize(file_path)
        file_last_modified = os.path.getmtime(file_path)
        file_type, _ = mimetypes.guess_type(file_path)
        file_details = f"File Size: {file_size} bytes\nLast Modified: {file_last_modified}\nFile Type: {file_type}"
        
        QMessageBox.information(self, "File Details", file_details)

    def search_files(self):
        search_text, ok = QInputDialog.getText(self, 'Search Files', 'Enter search keyword:')
        if ok and search_text:
            search_text = search_text.lower()
            for index in range(self.model.rowCount()):
                file_info = self.model.fileInfo(self.model.index(index, 0))
                if search_text in file_info.fileName().lower():
                    tree_index = self.model.index(index, 0)
                    self.tree.setCurrentIndex(tree_index)
                    break

    def compress_files(self):
        files_to_compress = QFileDialog.getOpenFileNames(None, "Select Files to Compress")[0]
        save_path, _ = QFileDialog.getSaveFileName(None, "Save Compressed File As", "", "Compressed File (*.zip)")
        
        with zipfile.ZipFile(save_path, 'w') as zipf:
            for file_path in files_to_compress:
                zipf.write(file_path, os.path.basename(file_path))

def main():
    app = QApplication(sys.argv)
    file_manager = FileManager()
    file_manager.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
