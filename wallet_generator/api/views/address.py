from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from wallet_generator.api import utils


class AddressView(generics.GenericAPIView):
    def get(self, request) -> Response:
        """Will get a list of generated wallets

        Args:
            request (Request): Request sent by the user

        Returns:
            dict: TO BE FILLED LATER
        """
        return Response(
            {"Success": True, "data": []},
            status=status.HTTP_200_OK,
        )

    def post(self, request) -> Response:
        """This endpoint will create a wallet based on the acronym passed

        Args:
            request (Request): Request sent by the user

        Returns:
            Response: TO BE FILLED LATER
        """
        acronym = request.data.get("acronym", None)
        account_addr = utils.acronym_handler(acronym)
        return Response(
            {
                "Success": True,
                "message": "New wallet has been created successfully",
                "account_address": account_addr,
            },
            status=status.HTTP_201_CREATED,
        )
