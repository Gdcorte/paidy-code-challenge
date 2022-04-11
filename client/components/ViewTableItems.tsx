import { OrderHandler } from "datasources/order";
import { FunctionComponent, useState } from "react";
import styled from 'styled-components';

const VIewItemsInTableStyled = styled.div`
  display: flex;
  flex-direction: column;
  width: fit-content;
  margin: 8px;
  h4 {
    margin-bottom: 4px;
  }
  
  p {
    margin-bottom: 2px;
    margin-top: 2px;
  }

  button {
    margin: 8px;
  }
`

const ViewMenuStyled = styled.div`
    display:flex;

`

const ViewTableStyled = styled.table`
  margin-top: 12px;

  table {
    border-collapse: collapse;
    width: 100%;
  }
  
  td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
  }
  
  th {
    text-align: center;
  }

  tr:nth-child(even) {
    background-color: #dddddd;
  }

  button.danger {
      background-color: #ff4861;
      color: #fefefe;
      border: medium double transparent;
      border-radius: 5px;
      padding: 8px;

      &:hover {
        background-color: #fefefe;
        color: #ff4861;
        border: medium double #ff4861;
      }

      &:active {
        color: #363636;
        border: medium double #363636;
      }
  }
`

const VIewTableItems: FunctionComponent = ({ }) => {
    const [itemName, setitemName] = useState('')
    const [tableNumber, settableNumber] = useState(0)

    const [tableData, settableData] = useState([<tr key='empty-view-table'></tr>])

    function removeItemFromTable(orderId: string) {
        OrderHandler.deleteItemInTable(orderId)

        viewTableItems()
        alert("ITEM REMOVED!!")
    }

    function applyItemRowTemplate(
        orderId: string,
        itemName: string,
        timeToCook: number
    ) {
        return (
            <tr key={`view-items-${orderId}`}>
                <td>{orderId}</td>
                <td>{itemName}</td>
                <td>{timeToCook}</td>
                <td>
                    <button
                        className={`danger`}
                        onClick={() => removeItemFromTable(orderId)}
                    >
                        Delete
                    </button>
                </td>
            </tr>
        )
    }

    async function viewTableItems() {
        let results = await OrderHandler.getTableItems(tableNumber)

        console.info(results)
        let formattedResults = results.map((value) => {
            return applyItemRowTemplate(value.id, value.item_name, value.time_to_cook)
        })
        settableData(formattedResults)
    }

    async function viewSpecificItemInTable() {
        let results = await OrderHandler.getItemForTable(tableNumber, itemName)

        console.info(results)
        let formattedResults = results.map((value) => {
            return applyItemRowTemplate(value.id, value.item_name, value.time_to_cook)
        })
        settableData(formattedResults)
    }

    return (
        <VIewItemsInTableStyled>
            <h4>View Items in Table</h4>
            <ViewMenuStyled>
                <label>
                    <p>Table Number</p>
                    <input
                        type="number" name="addItem-TableNumber" id="addItem-TableNumber"
                        value={tableNumber}
                        onChange={event => settableNumber(parseInt(event.target.value))}
                    />
                </label>

                <button onClick={viewTableItems}>View Items for Table</button>

                <label>
                    <p>Item Name</p>
                    <input
                        type="text" name="addItem-TableNumber" id="addItem-TableNumber"
                        value={itemName}
                        onChange={event => setitemName(event.target.value)}
                    />
                </label>

                <button onClick={viewSpecificItemInTable}>View Specific Item for table</button>
            </ViewMenuStyled>

            <ViewTableStyled>
                <thead>
                    <tr>
                        <th>Order Id</th>
                        <th>Item Name</th>
                        <th>Time to Cook</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {tableData}
                </tbody>
            </ViewTableStyled>
        </VIewItemsInTableStyled>
    )
}

export default VIewTableItems