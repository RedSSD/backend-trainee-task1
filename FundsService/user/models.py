from django.db import models


class CustomUser(models.Model):

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    funds = models.FloatField(default=0)

    def __str__(self) -> str:
        return f'({self.user_id})  {self.username} - {self.funds} UAN'


    def check_amount(self, amount: str):
        try:
            amount = float(amount)
            if amount <= 0:
                return False
        except ValueError:
            return False
        return True

    def funds_accural(self, amount: str):

        if not self.check_amount(amount):
           return False

        amount = float(amount)
        self.funds += amount
        self.save()
        return True

    def funds_debit(self, amount: str):

        if not self.check_amount(amount):
            return False

        amount = float(amount)

        if self.funds - amount < 0:
            return False

        self.funds -= amount
        self.save()
        return True


