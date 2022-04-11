from models.orders import Item, Offer, OfferType, Operators


def apply_item_offer(item_offer: Offer, item_occurences: int, item_data: Item) -> float:
    # Covering here only the current case of item offers, which is total price
    # (More variations can be added here. the database already accomodates it)
    if all(
        [
            item_offer.operator == Operators.equal,
            item_offer.offer_type == OfferType.total_price,
        ]
    ):
        subtotal = (item_occurences // item_offer.operand) * item_offer.offer_apply + (
            item_occurences % item_offer.operand
        ) * item_data.price

        return subtotal

    # Case item offer is not recognized, do not apply
    return item_occurences * item_data.price


def apply_basket_offer(basket_offer: Offer, subtotal: float):
    # Covering here only the current case of basket offer, which is an absolute discount for gte subbtotal
    # (More variations can be added here. the database already accomodates it)
    if all(
        [
            basket_offer.offer_type == OfferType.discount,
            basket_offer.operator == Operators.gt,
            subtotal > basket_offer.operand,
        ]
    ):
        subtotal = subtotal - basket_offer.offer_apply

        return subtotal

    # Case basket offer is not recognized, do not apply
    return subtotal
