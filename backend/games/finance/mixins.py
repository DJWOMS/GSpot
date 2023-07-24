from finance.models.offer import Offer, ProductOffer


class PricePackSeriazerMixin:
    def get_price(self, obj):
        try:
            offer = ProductOffer.objects.filter(product=obj).latest('id')
            price = Offer.objects.get(id=str(offer.offer_id)).price
            result = {'amount': price.amount, 'currency': price.currency}
            return result
        except (ProductOffer.DoesNotExist, Offer.DoesNotExist):
            return None
