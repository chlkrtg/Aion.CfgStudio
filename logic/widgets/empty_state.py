"""Хелперы для пустого состояния списков / деревьев."""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QListWidgetItem, QTreeWidgetItem


def add_empty_item(list_widget, text: str):
    """Добавляет невыбираемый placeholder-айтем в QListWidget."""
    item = QListWidgetItem(text)
    item.setFlags(Qt.ItemFlag.NoItemFlags)
    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    item.setForeground(QColor("#555565"))
    list_widget.addItem(item)


def add_empty_node(tree_widget, text: str):
    """Добавляет невыбираемый placeholder-node в QTreeWidget.

    Node растягивается на все колонки (span), текст переносится
    (если tree_widget.setWordWrap(True)).
    """
    node = QTreeWidgetItem([text, ""])
    node.setFlags(Qt.ItemFlag.NoItemFlags)
    node.setTextAlignment(0, Qt.AlignmentFlag.AlignCenter)
    node.setForeground(0, QColor("#555565"))
    tree_widget.addTopLevelItem(node)

    # span на все колонки
    row = tree_widget.indexOfTopLevelItem(node)
    tree_widget.setFirstColumnSpanned(row, tree_widget.rootIndex(), True)