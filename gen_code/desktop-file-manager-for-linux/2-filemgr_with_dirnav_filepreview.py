from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTreeView, QFileSystemModel, QListView, QHBoxLayout, QPushButton, QLineEdit

import sys

class FileManager(QWidget):
    def __init__(self):
        super().__init__()

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

        layout.addWidget(dir_input)
        layout.addWidget(btn_navigate)
        layout.addWidget(tree_view)
        layout.addWidget(list_view)
        layout.addWidget(btn_refresh)

        self.setLayout(layout)

    def refresh(self):
        self.model().refresh()

    def navigate(self, path, model, tree_view, list_view):
        index = model.index(path)
        tree_view.setRootIndex(index)
        list_view.setRootIndex(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileManager()
    window.show()
    sys.exit(app.exec_())
