import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [zip, setZip] = useState('');
  const [error, setError] = useState('')
  const [forecasts, setForecasts] = useState([])

  const handleClick = async () => {
    setForecasts([])
    if(!zip) {
      setError('Please Enter Zip')
      return
    }
    if(zip.length !== 5) {
      setError('Please Enter 5 digit zip')
      return
    }

    for (const c of zip) {
      if (!'0123456789'.includes(c)){
        setError('Please Enter only numerical values')
        return
      }
    }

    fetch(`/forecast?zip=${zip}`).then(res => res.json()).then(data => {
      setForecasts(data);
    }).catch(e => setError(e.json()));
  }
  
  const forecasts_display = forecasts.map((forecast) => 
    <li key={forecast.date}>
      <div>DATE: {forecast.date}</div>
      <div>HIGH: {forecast.high}°C</div>
      <div>LOW: {forecast.low}°C</div>
    </li>
  )

  return (
      <div className="App">
        <header className="App-header">
          <div> Please Enter Zip Code:
          <input
            type="text"
            value={zip}
            placeholder="Enter zip"
            onChange={e => {
              setError('')
              return setZip(e.target.value)
            }}
          />
          
          <p>
            <strong>{zip}</strong>
          </p>
          <p>{error}</p>
          <button onClick={handleClick}>Fetch data</button>
          <ul>{forecasts_display}</ul>
        </div>
      </header>
    </div>
  );
}

export default App;