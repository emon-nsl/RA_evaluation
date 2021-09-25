class LaptopBrand:
    def __init__(self):
        self.name_lst = {}

    def __setitem__(self, serial_number, data):
        self.name_lst[serial_number] = data
    
    def __getitem__(self, serial_number):
        return self.name_lst[serial_number]


# we can do this
laptopBrand = LaptopBrand()
# but how can i do this
laptopBrand[0] = 'DELL'
laptopBrand[1] = 'HP'
laptopBrand[2] = 'New'
print(laptopBrand[0])
print(laptopBrand[1], '\n', laptopBrand[2])