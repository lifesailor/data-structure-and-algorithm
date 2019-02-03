"""
Bag Client
"""
from bag import Bag
import math


class Client:
    def test(self, args):
        numbers = Bag()

        while args:
            item = args.pop(0)
            assert isinstance(item, float) or isinstance(item, int)

            numbers.add(item)
        n = numbers.size()

        sum = 0
        for number in numbers:
            sum += number
        mean = sum / n

        sum = 0
        for number in numbers:
            sum += (number - mean) ** 2
        std = math.sqrt(sum / (n - 1))

        print("Mean: {0:.2f}".format(mean))
        print("Std dev: {0:.2f}".format(std))


if __name__ == "__main__":
    bag_client = Client()
    numbers = [100, 99, 101, 120, 98, 107, 109, 81, 101, 90]
    bag_client.test(numbers)