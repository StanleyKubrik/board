import logging


class UserLog:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        method = request.method
        url = request.build_absolute_uri()
        logging.basicConfig(filename='logs.log', filemode='a'
                            , format=f'%(asctime)s - %(message)s'
                            , datefmt='%Y-%b-%d %H:%M:%S'
                            , level=logging.DEBUG)
        logging.debug(f'{url} - {method}')

        response = self.get_response(request)

        return response
