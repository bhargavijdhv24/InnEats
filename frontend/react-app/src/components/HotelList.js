import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Booking from './Booking';

function HotelList() {
    const [hotels, setHotels] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5001/hotels')
            .then(res => setHotels(res.data))
            .catch(err => console.log(err));
    }, []);

    return (
        <div>
            <h2>Hotels</h2>
            {hotels.length === 0 && <p>No hotels found. Seed some data in MongoDB 'hotels' collection.</p>}
            {hotels.map(hotel => (
                <div key={hotel.id} style={{border:'1px solid #ddd', padding:10, marginBottom:10}}>
                    <h3>{hotel.name}</h3>
                    <p>{hotel.description}</p>
                    <Booking hotel={hotel} />
                </div>
            ))}
        </div>
    );
}

export default HotelList;
