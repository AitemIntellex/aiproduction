from django.db import models

class Candle(models.Model):
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    close_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Open: {self.open_price}, High: {self.high_price}, Low: {self.low_price}, Close: {self.close_price}"
