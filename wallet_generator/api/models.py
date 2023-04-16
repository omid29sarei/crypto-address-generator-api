from django.db import models

# Create your models here.


class Address(models.Model):
    # TODO:Adding user account after adding the authentication layer +
    # Linking the wallet to a user profile
    coin = models.CharField(max_length=4)
    seed = models.CharField(max_length=255)
    private_key = models.CharField(max_length=255, blank=False)
    public_key = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.address

    def get_all_addresses(self):
        self.objects.all()
