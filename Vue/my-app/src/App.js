import './App.css';

import React from 'react';

//Add reset button to reset all squares to 0.

function Square() {
  const [count, setCount] = React.useState(0);

  return (
    <div className="square" onClick={() => setCount(count + 1)}>
      {count}
    </div>
  )
}

function App() {

  const [counters, setCounters] = React.useState([<Square/>, <Square/>, <Square/>, <Square/>, <Square/>, <Square/>, <Square/>, <Square/>, <Square/>]);

  const resetAllCounters = () => {
    const newCounters = []
    counters.forEach(() => {
      newCounters.push(<Square key={Math.random()}/>)
      setCounters(newCounters)
    })
  }


  return (
    <div className="App">
      <div className="grid">
        <div className="col">
          {counters[0]}
          {counters[1]}
          {counters[2]}
        </div>

        <div className="col">
          {counters[3]}
          {counters[4]}
          {counters[5]}
        </div>

        <div className="col">
          {counters[6]}
          {counters[7]}
          {counters[8]}
        </div>
    </div>

      <div className="button">
        <button onClick={() => {
          const squares = document.querySelectorAll('.square');
          squares.forEach((square, index) => {
            setTimeout(() => {
              square.click();
            }, 1000 * index);
          }
          );
        }}>Increment</button>

        <button onClick={resetAllCounters}>Reset</button>

      </div>
    </div>
  );
}

export default App;
