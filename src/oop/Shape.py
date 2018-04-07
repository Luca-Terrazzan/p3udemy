class Square():
    """Represents a square
    
    Provides common methods and stores attributes to represent
    a square figure
    """
    category = 'shapes'
    _area = 0
    _edge = 1

    def __init__(self, edge):
        self._edge = edge

    def area(self):
        if self._area != 0:
            return self._area
        self._area = self._edge ** 2
        return self._area
