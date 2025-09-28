import React, { useState } from 'react';
import axios from 'axios';

function Booking({ hotel }) {
    const [nights, setNights] = useState(1);
    const [message, setMessage] = useState("");

    const bookRoom = () => {
        axios.post('http://localhost:5001/book', {
            hotel_id: hotel.id,
            room_type: 'standard',
            nights: Number(nights),
            user_id: "user123"
        })
        .then(res => setMessage(res.data.message))
        .catch(err => setMessage("Error booking room"));
    }

    return (
        <div>
            <label>Nights: </label>
            <input type="number" value={nights} onChange={e => setNights(e.target.value)} min="1" />
            <button onClick={bookRoom} style={{marginLeft:10}}>Book Now</button>
            {message && <p>{message}</p>}
        </div>
    );
}

export default Booking;
