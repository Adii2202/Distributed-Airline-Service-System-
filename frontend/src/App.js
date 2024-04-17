import React, { useState, useEffect } from 'react';
import './App.css'; // Import your stylesheet (assuming it's named App.css)

function Home() {
  const [fromCity, setFromCity] = useState('');
  const [toCity, setToCity] = useState('');
  const [departureDate, setDepartureDate] = useState('');
  const [travelers, setTravelers] = useState(1);
  const [flights, setFlights] = useState([]); // State to store fetched flights
  const [isLoading, setIsLoading] = useState(false); // State to indicate search progress
  const [error, setError] = useState(null); // State to store any errors

  // Function to handle form submission (assuming integration with a flight search API)
  const handleSubmit = async (event) => {
    event.preventDefault();

    setIsLoading(true);
    setError(null); // Clear any previous errors

    try {
      const response = await fetch(/* Your flight search API URL */ 
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          from: fromCity,
          to: toCity,
          departureDate,
          travelers,
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to fetch flights'); // Handle errors gracefully
      }

      const flightData = await response.json();
      setFlights(flightData);
    } catch (error) {
      console.error('Error fetching flights:', error);
      setError(error.message); // Display an error message to the user
    } finally {
      setIsLoading(false);
    }
  };

  // // Function to fetch initial list of popular routes (optional)
  // useEffect(() => {
  //   const fetchPopularRoutes = async () => {
  //     // const response = await fetch(/* Your popular routes API URL */);
  //     const popularRoutes = await response.json();
  //     // Use popularRoutes to pre-populate dropdown menus (if desired)
  //   };
  //   fetchPopularRoutes();
  // }, []); // Run only once on component mount

  return (
    <div className="home">
      
      <div className="header">
        <h1><img src="/JetSetGo.png" height="50" alt="JetSetGo logo"></img>JetSetGo</h1>
        <nav>
            <a href="#">Login</a>
            <a href="#">SignUp</a>
        </nav>
      </div>

      <main>
        <section className="hero">
          <h2>Millions of cheap prices. One simple search.</h2>
          <div className="search-container">
          <form className="search-form" onSubmit={handleSubmit}>
            <div className="dropdown">
              <label htmlFor="from">From:</label>
              <input
                type="text"
                name="from"
                id="from"
                placeholder="From"
                value={fromCity}
                onChange={(e) => setFromCity(e.target.value)}
              />
            </div>
            <div className="dropdown">
              <label htmlFor="to">To:</label>
              <input
                type="text"
                name="to"
                id="to"
                placeholder="To"
                value={toCity}
                onChange={(e) => setToCity(e.target.value)}
              />
            </div>
            <input
              type="date"
              name="departure-date"
              id="departure-date"
              placeholder="Departure Date"
              value={departureDate}
              onChange={(e) => setDepartureDate(e.target.value)}
            />
            <input
              type="number"
              name="travelers"
              id="travelers"
              placeholder="Travelers"
              value={travelers}
              onChange={(e) => setTravelers(parseInt(e.target.value))} // Ensure valid integer
            />
            <button type="submit" className="btn">
              Search {isLoading && <span className="loading">Loading...</span>}
            </button>
          </form>
          </div>
          {error && <p className="error">{error}</p>}
          </section>

        {flights.length > 0 && (
          <section className="flight-results">
            <h2>Search Results</h2>
            <ul>
              {flights.map((flight) => (
                <li key={flight.id} className="flight-card">
                  <p>
                    {flight.airline} - {flight.fromCode} ({flight.fromCity}) to{' '}
                    {flight.toCode} ({flight.toCity})
                  </p>
                  <p>Departure: {flight.departureTime}</p>
                  <p>Arrival: {flight.arrivalTime}</p>
                  <p>Price: {flight.price.currency} {flight.price.amount}</p>
                  {/* Add a button or link for details/booking (optional) */}
                </li>
              ))}
            </ul>
          </section>
        )}
      </main>
    </div>
  );
}

export default Home;