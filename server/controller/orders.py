from datasources.orders import orders_datasource
from models.orders import Order, TableOrderReturn


class OrdersController:
    def add_item_to_table(
        self,
        table_number: int,
        item_name: str,
        cook_time: int,
    ) -> Order:
        new_order = Order.without_id(
            table_number=table_number,
            item_name=item_name,
            time_to_cook=cook_time,
        )

        orders_datasource.add_item_to_table(new_order=new_order)

        return new_order

    def get_items_for_table(self, table_number: int) -> TableOrderReturn:
        return orders_datasource.get_items_for_table(table_number=table_number)

    def get_specific_item_at_table(
        self, table_number: int, item_name: str
    ) -> TableOrderReturn:
        return orders_datasource.get_specific_item_at_table(
            table_number=table_number,
            item_name=item_name,
        )

    def delete_table_item(self, order_id: str) -> None:
        orders_datasource.delete_table_item(order_id=order_id)


orders_controller = OrdersController()
