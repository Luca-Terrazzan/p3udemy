class Square():
    """Represents a square
    
    Provides common methods and stores attributes to represent
    a square figure
    """
    category = 'shapes'
    _area = 0
    _2p = 0
    _edge = 0

    def __init__(self, edge):
        if edge <= 0:
            raise Exception('Invalid shape.')
        self._edge = edge

    def area(self):
        return self._area if self._area != 0 else self._edge ** 2

    def perimeter(self):
        return self._2p if self._2p != 0 else self._edge * 4
