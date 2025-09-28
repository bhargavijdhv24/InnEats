import React, { useState, useEffect } from 'react';
import axios from 'axios';

function FoodMenu() {
    const [menu, setMenu] = useState([]);
    const [cart, setCart] = useState([]);
    const [message, setMessage] = useState("");

    useEffect(() => {
        axios.get('http://localhost:5002/menu/restaurant123')
            .then(res => setMenu(res.data))
            .catch(err => console.log(err));
    }, []);

    const addToCart = (item) => setCart(prev => [...prev, item]);

    const placeOrder = () => {
        axios.post('http://localhost:5002/order', {
            user_id: "user123",
            restaurant_id: "restaurant123",
            items: cart.map(i => i.name || i)
        })
        .then(res => setMessage(res.data.message))
        .catch(err => setMessage("Error placing order"));
    }

    return (
        <div>
            <h2>Food Menu</h2>
            {menu.length === 0 && <p>No menu found. Seed 'restaurants' collection in MongoDB.</p>}
            {menu.map(item => (
                <div key={item.name} style={{display:'flex', justifyContent:'space-between', padding:6, borderBottom:'1px solid #eee'}}>
                    <span>{item.name} - ${item.price}</span>
                    <button onClick={() => addToCart(item)}>Add</button>
                </div>
            ))}
            <div style={{marginTop:10}}>
                <strong>Cart:</strong>
                <ul>
                    {cart.map((c, i) => <li key={i}>{c.name || c}</li>)}
                </ul>
                <button onClick={placeOrder}>Place Order</button>
                {message && <p>{message}</p>}
            </div>
        </div>
    );
}

export default FoodMenu;
