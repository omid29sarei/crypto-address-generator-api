import logging
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import get_object_or_404
from wallet_generator.api.serializers import GenerateAddress
from wallet_generator.api import utils
from wallet_generator.api.models import Address

logger = logging.getLogger(__name__)


class AddressView(generics.GenericAPIView):
    add_address_serializers = GenerateAddress

    def prepare_list_queryset(self):
        query_set = Address.objects.all()
        account_details = []
        for address in query_set:
            address_object = {}
            address_object["id"] = address.id
            address_object["coin"] = address.coin
            address_object["seed"] = address.seed
            address_object["private_key"] = address.private_key
            address_object["public_key"] = address.public_key
            address_object["address"] = address.address
            address_object["created_at"] = address.created_at
            account_details.append(address_object)
        return account_details

    def prepare_get_address_by_id(self, wallet_id):
        retrieved_address_object = get_object_or_404(Address, pk=wallet_id)
        address_object = {}
        address_object["coin"] = retrieved_address_object.coin
        address_object["seed"] = retrieved_address_object.seed
        address_object["private_key"] = retrieved_address_object.private_key
        address_object["public_key"] = retrieved_address_object.public_key
        address_object["address"] = retrieved_address_object.address
        address_object["created_at"] = retrieved_address_object.created_at
        return address_object

    def get(self, request: Request) -> Response:
        """Will get a list of generated wallets or single wallet info based on based on the input

        Args:
            request (Request): Request sent by the user

        Returns:
            dict: TO BE FILLED LATER
        """
        wallet_id = request.GET.get("wallet_id", None)
        if wallet_id:
            account_details = self.prepare_get_address_by_id(wallet_id=wallet_id)
            logger.info(f"Account details with id {wallet_id} object has been prepared")
        else:
            account_details = self.prepare_list_queryset()
            logger.info("Account details object has been prepared for list addresses")

        logger.info("All addresses are retrieved successfully!")
        return Response(
            {
                "Success": True,
                "message": "All addresses are retrieved successfully!",
                "account_details": account_details,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request: Request) -> Response:
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
            logger.info(f"Unsupported acronym {network} was passed! ")
            return Response(
                {
                    "Success": False,
                    "error": f"Please choose a supported network. Supported networks are: {accepted_network}",
                },
                status=status.HTTP_201_CREATED,
            )
        account_details = utils.wallet_creator(network=network)
        logger.info(f"An wallet has been generated for {network}")
        encrypted_account_details = utils.encrypt_sensitive_fields(
            account_details=account_details
        )
        logger.info(f"All the sensitive fields are encrypted!")
        serializer = self.add_address_serializers(data=encrypted_account_details)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info(
            f"Serializers data is validated and the new address is being generated and saved within DB"
        )
        return Response(
            {
                "Success": True,
                "message": "New wallet has been created successfully",
                "coin": network,
                "account_details": account_details,
            },
            status=status.HTTP_201_CREATED,
        )
