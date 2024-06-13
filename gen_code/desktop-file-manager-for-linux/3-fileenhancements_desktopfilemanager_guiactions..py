from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTreeView, QFileSystemModel, QListView, QHBoxLayout, QPushButton, QLineEdit, QLabel

import sys


class FileManager(QWidget):
    def __init__(self):
        super().__init()
        
        self.setWindowTitle("File Manager")
        self.setGeometry(100, 100, 800, 600)
        
        layout = QVBoxLayout()
        
        model = QFileSystemModel()
        model.setRootPath("")
        
        tree_view = QTreeView()
        tree_view.setModel(model)
        tree_view.setRootIndex(model.index(""))
        
        list_view = QListView()
        list_view.setModel(model)
        list_view.setRootIndex(model.index(""))
        
        btn_refresh = QPushButton("Refresh")
        btn_refresh.clicked.connect(self.refresh)
        
        dir_input = QLineEdit()
        
        btn_navigate = QPushButton("Navigate")
        btn_navigate.clicked.connect(lambda: self.navigate(dir_input.text(), model, tree_view, list_view))
        
        label_path = QLabel("Current Path:")
        layout.addWidget(label_path)
        
        search_input = QLineEdit()
        search_input.textChanged.connect(lambda: self.filter(search_input.text(), model))
        
        btn_delete = QPushButton("Delete")
        btn_delete.clicked.connect(lambda: self.delete(tree_view.currentIndex()))
        
        layout.addWidget(dir_input)
        layout.addWidget(btn_navigate)
        layout.addWidget(tree_view)
        layout.addWidget(list_view)
        layout.addWidget(btn_refresh)
        layout.addWidget(search_input)
        layout.addWidget(btn_delete)
        
        self.setLayout(layout)
    
    def refresh(self):
        self.model().refresh()
        
    def navigate(self, path, model, tree_view, list_view):
        index = model.index(path)
        tree_view.setRootIndex(index)
        list_view.setRootIndex(index)
        
    def filter(self, keyword, model):
        directory = model.directory
        keywords = keyword.lower().split()
        for i in range(model.rowCount()):
            if all(keyword in model.fileInfo(model.index(i,0)).fileName().lower() for keyword in keywords):
                dir_files.append(os.path.join(directory(model)[i], model.fileInfo(model.index(i,0)).fileName()))
    
    def delete(self, index):
        file_path = self.model.filePath(index)
        self.model.remove(index)
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileManager()
    window.show()
    sys.exit(app.exec_())
