class ResultReconizer(object):

    def __init__(self, brand, packing, color, label):
        self.brand = brand
        self.packing = packing
        self.color = color
        self.label = label

    def serialize(self):
        return {
            'brand': self.brand,
            'packing': self.packing,
            'color': self.color,
            'label': self.label,
            'brand': self.brand
        }
