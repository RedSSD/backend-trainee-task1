from django.db import models


class CustomUser(models.Model):

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    funds = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'({self.user_id})  {self.username} - {self.funds} UAN'

    def funds_accural(self, amount: float):
        pass

    def funds_debit(self, amount: float):
        pass

    def funds_send(self, taker_user_id: int, amount: float):
        pass
