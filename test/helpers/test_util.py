from os import getenv


class TestUtil:

    @staticmethod
    def get_key():
        return getenv('HUDAI_API_SECRET_KEY')
