import DiceButton from '../../components/menu/dice-buttons';
import { useState, useEffect } from 'react';

function FetchSteps() {
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [items, setItems] = useState([]);

  useEffect(() => {
    var requestOptions = {
      method: 'GET',
      redirect: 'follow'
    };
    
    fetch("https://earthdawn.azurewebsites.net/api/stepList?&code=mPjEfCJWjS4gQUb/s4gWJtwthAjDBAzcmYjWFWNEvPSruWaK9/QVEg==", requestOptions)
      .then(res => res.json())
      .then(
        (result) => {
          setIsLoaded(true);
          setItems(result);
        },
        (error) => {
          setIsLoaded(true);
          setError(error);
        }
      )
  }, [])

  if (error) {
    return <div>Error: {error.message}</div>;
  } else if (!isLoaded) {
    return <div>Loading...</div>;
  } else {
    return (
      <>
        {items.map((buttonLabel, i) => (
          <DiceButton key={i} name={buttonLabel} />
        ))}
      </>
    );
  }
}

export default FetchSteps;