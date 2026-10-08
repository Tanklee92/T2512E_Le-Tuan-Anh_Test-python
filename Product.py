from abc import abstractmethod


class DataFrame:

    product = []

    def __init__(self):
        pass

    def print_product_list(self):
        for product in self.product_list:
            print(product)


    @abstractmethod
    def read_file_to_get_product_list():
        pass

    