from django.db import models


# Item name for databse
class Donation(models.Model):
    name = models.CharField(max_length=100)
    # stripe uses ids for names (since were only using one we hardcode it)
    stripe_product_id = models.CharField(
        default="prod_LNbJHMjBBddmyy", max_length=100)

    def __str__(self):
        return self.name


# price fields for item names
class Price(models.Model):
    product = models.ForeignKey(Donation, on_delete=models.CASCADE)
    # stripe uses product price id for prices, cannot be set here
    # specified id are in stripe dashboard and assigned in backend of sql
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
