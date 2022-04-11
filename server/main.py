from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controller.orders import orders_controller
from models.orders import Order, TableOrderReturn

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.delete("/orders/{order_id}", status_code=204)
def get_all_offers(order_id: str):
    orders_controller.delete_table_item(order_id=order_id)

    return {"status": "resource deleted"}


@app.get("/orders/tables/{table_number}")
def get_items_for_table(table_number: int) -> TableOrderReturn:
    return orders_controller.get_items_for_table(table_number=table_number)


@app.post("/orders/tables/{table_number}/items", status_code=201)
def add_item_to_table(
    table_number: int,
    item_name: str = Body(..., embed=True),
    cook_time: int = Body(..., embed=True),
) -> Order:
    return orders_controller.add_item_to_table(
        table_number=table_number,
        item_name=item_name,
        cook_time=cook_time,
    )


@app.get("/orders/tables/{table_number}/items/{item_name}")
def get_specific_item_at_table(table_number: int, item_name: str) -> TableOrderReturn:
    return orders_controller.get_specific_item_at_table(
        table_number=table_number,
        item_name=item_name,
    )
