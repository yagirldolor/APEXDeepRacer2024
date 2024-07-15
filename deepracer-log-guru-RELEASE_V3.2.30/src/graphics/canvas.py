# v4 UI STATUS - BRAND NEW
# ************************

from abc import abstractmethod

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, \
    QAbstractGraphicsShapeItem


class Canvas(QGraphicsView):
    def __init__(self, background_colour: Qt.GlobalColor):
        super().__init__(None)
        self._background_colour = background_colour
        self._width = self.geometry().width() - 2
        self._height = self.geometry().height() - 2
        self._recreate_scene()

    def paintEvent(self, event):
        new_width = self.geometry().width() - 2
        new_height = self.geometry().height() - 2
        if self._width != new_width or self._height != new_height:
            self._width = new_width
            self._height = new_height
            self._recreate_scene()

        super().paintEvent(event)

    def _recreate_scene(self):
        pixmap = QPixmap(self._width, self._height)
        pixmap.fill(self._background_colour)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        self._paint(painter)
        painter.end()

        scene = QGraphicsScene(0, 0, self._width, self._height)
        scene.addItem(QGraphicsPixmapItem(pixmap))
        for i in self._get_scene_items():
            scene.addItem(i)
        self.setScene(scene)

    @abstractmethod
    def _paint(self, painter: QPainter):
        pass

    @abstractmethod
    def _get_scene_items(self) -> list[QAbstractGraphicsShapeItem]:
        pass
