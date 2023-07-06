from decimal import Decimal

from apps.base.utils.classmethod import DjangoModel
from apps.payment_accounts.models import Account, Owner
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models


class TransferHistoryManager(models.Manager):
    def create_transfer_history(
        self,
        *,
        account_from: DjangoModel,
        account_to: DjangoModel,
        amount: Decimal,
    ):
        allowed_models = [Owner, Account]

        account_to_model = type(account_to)
        account_from_model = type(account_from)
        if account_to_model not in allowed_models or account_from_model not in allowed_models:
            allowed_model_names = ', '.join(klass.__name__ for klass in allowed_models)
            raise ValidationError(
                f'Not valid model type passed it could be only type of {allowed_model_names}',
            )

        ct_account_to_type = ContentType.objects.get_for_model(account_to_model)
        ct_account_from_type = ContentType.objects.get_for_model(account_from_model)

        transfer_history = self.create(
            account_from_type=ct_account_from_type,
            account_to_type=ct_account_to_type,
            object_id_from=account_from.pk,
            object_id_to=account_to.pk,
            amount=amount,
        )
        return transfer_history
