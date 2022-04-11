from models.orders import Order, TableOrder, TableOrderReturn

from .mysql_db import BaseMySqlDatasource


class OrdersDatasource(BaseMySqlDatasource):
    SCHEMA = "restaurant"

    def add_item_to_table(self, new_order: Order):
        fields, values = list(zip(*new_order.dict().items()))

        query = f"""
            INSERT INTO `{self.SCHEMA}`.orders ({','.join(fields)}) 
            VALUES ({','.join(['%s']*len(values))})
        """

        self.execute_single_statement(
            query=query,
            query_params=values,
        )

    def get_items_for_table(self, table_number: int):
        query = f"""
            SELECT {','.join(TableOrder.__fields__.keys())}
            FROM `{self.SCHEMA}`.orders
            WHERE table_number = %s
        """

        results = self.run_single_query(
            query=query,
            query_params=(table_number,),
        )

        return TableOrderReturn(orders=results)

    def get_specific_item_at_table(
        self,
        item_name: str,
        table_number: int,
    ):
        query = f"""
            SELECT {','.join(TableOrder.__fields__.keys())}
            FROM `{self.SCHEMA}`.orders
            WHERE table_number = %s 
                AND item_name = %s 
        """

        results = self.run_single_query(
            query=query,
            query_params=(
                table_number,
                item_name,
            ),
        )

        return TableOrderReturn(orders=results)

    def delete_table_item(self, order_id: str):
        query = f"""
            DELETE FROM `{self.SCHEMA}`.orders
            WHERE id=%s
        """

        self.execute_single_statement(
            query=query,
            query_params=(order_id,),
        )


orders_datasource = OrdersDatasource()
