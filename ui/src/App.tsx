import React, { useState, useEffect } from "react";
import logo from './logo.svg';
import './App.css';


const App: React.FC = () => {
  const [guess, setGuess] = useState("");
  const [positions, setPositions] = useState<Array<{ word: string; position: number }>>([]);

  const handleGuess = async () => {
      // Make a request to the backend API to get the word similarity
      try {
        const response = await fetch('http://127.0.0.1:8000/similarity?guess=' + guess);
        const data = await response.json();
        const position = data.similarity;
        setPositions((prevPositions) => [...prevPositions, { word: guess, position }]);
        setGuess("");
      } catch (error) {
        console.error("Error fetching word similarity:", error);
      }
    };


  const sortedPositions = [...positions].sort((a, b) => b.position - a.position);

  return (
    <div className="App">
      <h1>Contexto Game</h1>
      <p>Find the secret word. You have unlimited guesses.</p>
      <div>
      <input
        type="text"
        value={guess}
        onChange={(e) => setGuess(e.target.value)}
        placeholder="Enter your guess"
      />
      </div>
      <button onClick={handleGuess}>Submit</button>
      <div>
        <ul>
          {sortedPositions.map((pos, index) => (
            <div key={index} className={getPositionStyle(pos.position) + " list_value"}>
              <span>{pos.word}: </span>
              <span>{pos.position} </span>
            </div>
          ))}
        </ul>
      </div>
    </div>
  );
};

function getPositionStyle(position: number) {
    switch(true){
        case position <= 20: return 'low';
        case position <= 40: return 'ok';
        case position <= 60: return 'medium';
        case position <= 80: return 'high';
        case position <= 99: return 'close';
        case position == 1: return 'exact';
        default: return "exact";
    }
}

export default App;

