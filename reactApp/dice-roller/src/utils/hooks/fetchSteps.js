import DiceButton from '../../components/menu/dice-buttons';
import { useState, useEffect, useContext } from 'react';
import { ResultsContext } from '../contexts/ResultsContext';

function FetchSteps() {
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);

  const { stepsValue, setStepsValue } = useContext(ResultsContext);

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
          setStepsValue(result);
        },
        (error) => {
          setIsLoaded(true);
          setError(error);
        }
      )
  }, [setStepsValue])

  if (error) {
    return <div>Error: {error.message}</div>;
  } else if (!isLoaded) {
    return <div>Loading...</div>;
  } else {
    return (
      <>
        {Object.keys(stepsValue).map((buttonLabel, i) => (
          <DiceButton key={i} name={buttonLabel} />
        ))}
      </>
    );
  }
}

export default FetchSteps;