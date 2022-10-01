from django.core.exceptions import PermissionDenied


class IpRequests:
    old_ip = ''
    ip_requests_count = 0

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if self.ip_requests_count >= 5:
            raise PermissionDenied

        if request.META.get('REMOTE_ADDR') == self.old_ip:
            self.ip_requests_count += 1

        response = self.get_response(request)

        self.old_ip = request.META.get('REMOTE_ADDR')

        return response
