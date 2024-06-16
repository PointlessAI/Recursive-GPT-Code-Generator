import os
import subprocess
import sys
import mimetypes

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

        self.file_details_button = QPushButton("File Details")
        self.file_details_button.clicked.connect(self.show_file_details)

        self.search_button = QPushButton("Search Files")
        self.search_button.clicked.connect(self.search_files)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tree)
        self.layout.addWidget(self.create_button)
        self.layout.addWidget(self.file_details_button)
        self.layout.addWidget(self.search_button)

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

    def show_file_details(self):
        selected_file_info = self.model.fileInfo(self.tree.currentIndex())
        file_path = selected_file_info.absoluteFilePath()
        file_size = os.path.getsize(file_path)
        file_type, _ = mimetypes.guess_type(file_path)
        file_details = f"File Size: {file_size} bytes\nFile Type: {file_type}"
        
        QMessageBox.information(self, "File Details", file_details)

    def search_files(self):
        search_text, ok = QInputDialog.getText(self, 'Search Files', 'Enter search keyword:')
        if ok and search_text:
            search_text = search_text.lower()
            for index in range(self.model.rowCount()):
                file_info = self.model.fileInfo(self.model.index(index, 0))
                if search_text in file_info.fileName():
                    tree_index = self.model.index(index, 0)
                    self.tree.setCurrentIndex(tree_index)
                    break

def main():
    app = QApplication(sys.argv)
    file_manager = FileManager()
    file_manager.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
