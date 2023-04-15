from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response


class Healthz(generics.GenericAPIView):
    """
    This class is just a standard practice to make sure the server is up and running
    """

    def get(self, request: Request) -> Response:
        return Response(
            {"Success": True, "message": "The server is up and running"},
            status=status.HTTP_200_OK,
        )
