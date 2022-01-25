import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import Menu from '../menu';
import Results from '../results';
import Header from '../common/header';
import { ResultsContext } from '../../utils/contexts/ResultsContext';
import { useState } from 'react';

function App() {
  const [value, setValue] = useState("Please choose a step to roll.");

  return (
    <div>
      <div>
        <Header />
      </div>
      <div className="App">
        <ResultsContext.Provider value={{ value, setValue }}>
          <div className="Menu aside">
            <Menu />
          </div>
          <div className="Results aside">
            <Results />
          </div>
        </ResultsContext.Provider>
      </div>
    </div>
  );
}

export default App;
