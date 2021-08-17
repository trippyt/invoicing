from PyQt5.QtCore import Qt, QDate
from PyQt5.QtCore import QPoint, QRectF
from PyQt5.QtWidgets import QCalendarWidget, QApplication
from PyQt5.QtGui import QPalette, QTextCharFormat
from loguru import logger as log


class MyCalendar(QCalendarWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.daysWorked = []
        self.selected_dates = set()

        self.highlight_format = QTextCharFormat()
        self.highlight_format.setBackground(self.palette().brush(QPalette.Highlight))
        self.highlight_format.setForeground(self.palette().color(QPalette.HighlightedText))

        log.debug(self.dateTextFormat())

    """def format_range(self, format):
        if self.begin_date and self.end_date:
            d0 = min(self.begin_date, self.end_date)
            d1 = max(self.begin_date, self.end_date)
            log.debug('DATE RANGE: ', d0, d1)
            while d0 <= d1:
                self.setDateTextFormat(d0, format)
                d0 = d0.addDays(1)"""

    def clear_selection(self):
        self.selected_dates.clear()
        self.setDateTextFormat(QDate(), QTextCharFormat())

    def date_is_clicked(self, date):
        # Reset highlighting of previously selected date range if Shift is not pressed
        if not QApplication.instance().keyboardModifiers() & Qt.ShiftModifier:
            self.clear_selection()

        self.selected_dates.add(date)
        for selected_date in self.selected_dates:
            self.setDateTextFormat(selected_date, self.highlight_format)

        # self.setCurrentPage(date.year(), date.month())

        log.debug(f"IF: {list(self.dateTextFormat())}")

    def paintCell(self, painter, rect, date):
        # log.debug(self.daysWorked[0].toString())
        super().paintCell(painter, rect, date)
        if date in self.daysWorked:
            painter.setBrush(Qt.red)
            painter.drawEllipse(rect.topLeft() + QPoint(8, 7), 3, 3)
