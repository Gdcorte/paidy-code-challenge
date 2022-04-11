import { OrderHandler } from "datasources/order";
import { FunctionComponent, useState } from "react";
import styled from 'styled-components';

const AddItemStyled = styled.div`
  display: flex;
  flex-direction: column;
  width: fit-content;
  margin: 8px;
  h4 {
    margin-bottom: 4px;
  }
  
  p {
    margin-bottom: 2px;
  }

  button {
    margin: 8px;
  }
`
const AddItemToTable: FunctionComponent = ({ }) => {
    const [itemName, setitemName] = useState('')
    const [tableNumber, settableNumber] = useState(0)
    const [cookTime, setcookTime] = useState(35)

    async function AddItem() {
        OrderHandler.addItemToTable(tableNumber, itemName, cookTime)

        alert("Item Added to table")
    }

    return (
        <AddItemStyled>
            <h4>Add Item To Table</h4>
            <div>
                <label>
                    <p>Table Number</p>
                    <input
                        type="number" name="addItem-TableNumber" id="addItem-TableNumber"
                        value={tableNumber}
                        onChange={event => settableNumber(parseInt(event.target.value))}
                    />
                </label>

                <label>
                    <p>Time to Cook (min)</p>
                    <input
                        type="number" name="addItem-TableNumber" id="addItem-TableNumber"
                        value={cookTime}
                        onChange={event => setcookTime(parseInt(event.target.value))}
                    />
                </label>

                <label>
                    <p>Item Name</p>
                    <input
                        type="text" name="addItem-TableNumber" id="addItem-TableNumber"
                        value={itemName}
                        onChange={event => setitemName(event.target.value)}
                    />
                </label>
            </div>
            <button onClick={AddItem}>Add Item</button>
        </AddItemStyled>
    )
}

export default AddItemToTable