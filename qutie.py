import weakref

from PyQt5 import QtCore, QtGui, QtWidgets, QtChart

def tr(value):
    return value

class IdProperty:

    __ids = weakref.WeakValueDictionary()

    def get(self, id):
        """Get item by ID, returns None if ID is not used."""
        return self.__ids.get(id)

    @property
    def id(self):
        """Returns item ID."""
        return self._.objectName()

    @id.setter
    def id(self, value):
        """Set item ID."""
        if value is not None:
            cls = self.__class__
            if value in cls.__ids:
                raise KeyError(value)
            cls.__ids[value] = self
        self._.setObjectName(value)

class EnabledProperty:

    @property
    def enabled(self):
        return self._.isEnabled()

    @enabled.setter
    def enabled(self, value):
        self._.setEnabled(value)

class VisibleProperty:

    @property
    def visible(self):
        return self._.isVisible()

    @visible.setter
    def visible(self, value):
        self._.setVisible(value)

class WindowTitleProperty:

    @property
    def window_title(self):
        return self._.windowTitle()

    @window_title.setter
    def window_title(self, value):
        self._.setWindowTitle(value)

class TextProperty:

    @property
    def text(self):
        return self._.text()

    @text.setter
    def text(self, value):
        return self._.setText(value)

class Object(IdProperty):

    ReflectionType = QtCore.QObject

    def __init__(self, id=None):
        self.__reflection = self.__class__.ReflectionType()
        self.id = id

    @property
    def _(self):
        """Returns underlying Qt5 object."""
        return self.__reflection

class Layout(Object):

    pass

class Row(Layout):

    ReflectionType = QtWidgets.QHBoxLayout

    def __init__(self, *children):
        super().__init__()
        self.__children = []
        for child in children:
            self.append(child)

    def append(self, child):
        if isinstance(child, Layout):
            self._.addLayout(child._)
        elif isinstance(child, Widget):
            self._.addWidget(child._)
        else:
            raise ValueError("Unsupported type", child)
        self.__children.append(child)

class Column(Row):

    ReflectionType = QtWidgets.QVBoxLayout

class Widget(Object, EnabledProperty, VisibleProperty, WindowTitleProperty):

    ReflectionType = QtWidgets.QWidget

    def __init__(self, layout=None, id=None):
        super().__init__(id=id)
        if layout: self.layout = layout
        self.visible = True

    @property
    def layout(self):
        return self.__layout

    @layout.setter
    def layout(self, value):
        self.__layout = value
        self._.setLayout(value._)

class Button(Widget, TextProperty):

    ReflectionType = QtWidgets.QPushButton

    def __init__(self, id=None, text=None, clicked=None):
        super().__init__(id)
        self.text = text
        self.clicked = clicked
        self._.clicked.connect(self.__clicked)

    def __clicked(self):
        if callable(self.clicked):
            self.clicked()

class List(Widget):

    ReflectionType = QtWidgets.QListView

    def __init__(self, model, id=None):
        super().__init__(id=id)
        self.model = QtCore.QStringListModel()
        self.model.setStringList(model)
        self._.setModel(self.model)

class Window(Widget):

    ReflectionType = QtWidgets.QMainWindow

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._.setCentralWidget(QtWidgets.QWidget())

    @property
    def layout(self):
        return self.__layout

    @layout.setter
    def layout(self, value):
        self.__layout = value
        self._.centralWidget().setLayout(value._)

class Plot(Widget):

    ReflectionType = QtChart.QChartView

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._axes = {}
        self._series = {}
        chart = QtChart.QChart()
        chart.layout().setContentsMargins(0, 0, 0, 0)
        chart.setBackgroundRoundness(0)
        chart.legend().setAlignment(QtCore.Qt.AlignRight)
        self._.setRubberBand(QtChart.QChartView.RectangleRubberBand)
        self._.setChart(chart)
        # Custom context menu
        self._.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self._.customContextMenuRequested.connect(self.__chartMenu)

    def __chartMenu(self, pos):
        """Custom context menu for chart."""
        menu = QtWidgets.QMenu(tr("Plot menu"), self._)
        resetAction = QtWidgets.QAction(tr("&Reset Zoom"))
        resetAction.triggered.connect(self._.chart().zoomReset)
        zoomInAction = QtWidgets.QAction(tr("Zoom &In"))
        zoomInAction.triggered.connect(self._.chart().zoomIn)
        zoomOutAction = QtWidgets.QAction(tr("Zoom &Out"))
        zoomOutAction.triggered.connect(self._.chart().zoomOut)
        menu.addAction(resetAction)
        menu.addAction(zoomInAction)
        menu.addAction(zoomOutAction)
        menu.exec_(self._.mapToGlobal(pos))

    def add_axis(self, name, align, r=[0, 1], type='value'):
        axis = {'value':QtChart.QValueAxis, 'datetime':QtChart.QDateTimeAxis}[type]()
        axis.setRange(*r)
        self._.chart().addAxis(axis, {'left': QtCore.Qt.AlignLeft, 'bottom': QtCore.Qt.AlignBottom, 'top': QtCore.Qt.AlignTop, 'right': QtCore.Qt.AlignRight}[align])
        self._axes[name] = axis

    def add_series(self, name, x, y, type='line'):
        series = {'line': QtChart.QLineSeries, 'scatter': QtChart.QScatterSeries, 'spline': QtChart.QSplineSeries}[type](self._)
        series.setUseOpenGL(True)
        series.setName(format(name))
        series.x = self._axes.get(x)
        series.y = self._axes.get(y)
        series.range_x = [0, 1]
        series.range_y = [0, 1]
        self._.chart().addSeries(series)
        series.attachAxis(series.x)
        series.attachAxis(series.y)
        self._series[name] = series

    def __resetSeries(self, series):
        series.x.setRange(min(series.x.min(), series.range_x[0]), max(series.x.max(), series.range_x[1]))
        series.y.setRange(min(series.y.min(), series.range_y[0]), max(series.y.max(), series.range_y[1]))

    def append(self, name, x, y):
        series = self._series[name]
        series.append(x, y)
        series.range_x[0] = min(x, series.range_x[0])
        series.range_x[1] = max(x, series.range_x[1])
        series.range_y[0] = min(y, series.range_y[0])
        series.range_y[1] = max(y, series.range_y[1])
        if not self._.chart().isZoomed():
            self.__resetSeries(series)

    @QtCore.pyqtSlot()
    def reset(self):
        for series in self._series.values():
            self.__resetSeries(series)
        self._.chart().zoomReset()
