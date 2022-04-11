
interface TableOrder {
    id: string,
    time_to_cook: number,
    item_name: string,
}

interface TableOrderReturn {
    orders: TableOrder[]
}

class OrderDatasource {
    hostname = process.env.NEXT_PUBLIC_ORDER_HOST || ""

    async addItemToTable(tableNumber: number, itemName: string, timeToCook: number) {
        await fetch(`${this.hostname}/orders/tables/${tableNumber}/items`,
            {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    item_name: itemName,
                    cook_time: timeToCook,
                })
            }
        )
    }

    async deleteItemInTable(orderId: string) {
        await fetch(`${this.hostname}/orders/${orderId}`,
            {
                method: 'DELETE',
            }
        )

    }

    async getTableItems(tableNumber: number): Promise<TableOrder[]> {
        let results = await fetch(`${this.hostname}/orders/tables/${tableNumber}`)
        let serialized_results: TableOrderReturn = await results.json()

        return serialized_results.orders
    }

    async getItemForTable(tableNumber: number, itemName: string): Promise<TableOrder[]> {
        let results = await fetch(`${this.hostname}/orders/tables/${tableNumber}/items/${itemName}`)
        let serialized_results: TableOrderReturn = await results.json()

        return serialized_results.orders
    }

}

export const OrderHandler = new OrderDatasource()