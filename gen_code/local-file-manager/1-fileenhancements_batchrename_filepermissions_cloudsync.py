import os
import shutil
import subprocess
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QVBoxLayout, QPushButton, QWidget, QInputDialog

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
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tree)
        self.layout.addWidget(self.create_button)
        
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

def main():
    app = QApplication(sys.argv)
    file_manager = FileManager()
    file_manager.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
