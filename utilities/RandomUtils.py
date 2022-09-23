import random
import string


class RandomUtils:

    @staticmethod
    def get_random_text():
        random_text = ''.join(random.choices(string.ascii_lowercase, k=7))
        return random_text

