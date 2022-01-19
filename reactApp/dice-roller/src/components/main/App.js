import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import Menu from '../menu';
import Results from '../results';
import Header from '../common/header';

function App() {
  return (
    <div>
      <div>
        <Header />
      </div>
      <div className="App">
        <div className="Menu aside">
          <Menu />
        </div>
        <div className="Results aside">
          <Results />
        </div>
      </div>
    </div>
  );
}

export default App;
