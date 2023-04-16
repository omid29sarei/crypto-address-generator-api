from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from wallet_generator.api.serializers import GenerateAddress
from wallet_generator.api import utils


class AddressView(generics.GenericAPIView):
    add_address_serializers = GenerateAddress

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
            Response: The response include a dict object with all the details of an account
        """
        network = request.data.get("network", None)
        accepted_network = ["BTC", "BTG", "BCH", "ETH", "LTC", "DASH", "DOGE"]
        is_network_supported = True if network.upper() in accepted_network else False
        if not is_network_supported:
            return Response(
                {
                    "Success": False,
                    "error": f"Please choose a supported network. Supported networks are: {accepted_network}",
                },
                status=status.HTTP_201_CREATED,
            )
        account_details = utils.wallet_creator(network=network)
        encrypted_account_details = utils.encrypt_sensitive_fields(
            account_details=account_details
        )
        serializer = self.add_address_serializers(data=encrypted_account_details)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "Success": True,
                "message": "New wallet has been created successfully",
                "network": network,
                "account_details": account_details,
            },
            status=status.HTTP_201_CREATED,
        )
