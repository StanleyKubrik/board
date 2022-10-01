import logging


class UserLog:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logging.basicConfig(filename='log.log', format='%(name)s - %(levelname)s - %(message)s')
        logging.debug('test')

        response = self.get_response(request)

        return response
