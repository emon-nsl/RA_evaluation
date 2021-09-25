class Layer:
    def __init__(self, name):
        self.name = name
    def __call__ (self, image_name):
        pass
layer = Layer("custom layer name")
y = layer('image')