import React from 'react';
import HotelList from './components/HotelList';
import FoodMenu from './components/FoodMenu';

function App() {
  return (
    <div style={{padding:20, fontFamily: 'Arial, sans-serif'}}>
      <h1>InnEats</h1>
      <div style={{display:'flex', gap:40}}>
        <div style={{flex:1}}>
          <HotelList />
        </div>
        <div style={{flex:1}}>
          <FoodMenu />
        </div>
      </div>
    </div>
  );
}

export default App;
