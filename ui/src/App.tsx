import React, { useState, useEffect } from "react";
import Dropdown from 'react-bootstrap/Dropdown';
import 'bootstrap/dist/css/bootstrap.min.css';

import './App.scss';

type Response = {
    similarity?: number,
    unknown_word?: string
}

type GiveUpResponse = {
    word: string,
    similarity: number
}

type Tip = {
    tip: string,
    similarity: number
}

const App: React.FC = () => {
  const [guess, setGuess] = useState("");
  const [positions, setPositions] = useState<Array<{ word: string; position: number }>>([]);
  const [inputError, setInputError] = useState(false)

  const handleGuess = async () => {
      // Make a request to the backend API to get the word similarity
      try {
        const response = await fetch('http://127.0.0.1:8000/similarity?guess=' + guess);
        const data: Response = await response.json();

        if (data.unknown_word) {
            setInputError(true);
            return;
        }

        setInputError(false);

        const position = data.similarity!;
        setPositions((prevPositions) => [...prevPositions, { word: guess, position }]);
        setGuess("");
      } catch (error) {
        console.error("Error fetching word similarity:", error);
      }
    };

  const handleTip = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/tip');
        const tip: Tip = await response.json();
        setPositions((prevPositions) => [...prevPositions, { word: tip.tip, position: tip.similarity }]);
      } catch (error) {
        console.error("Error fetching tip:", error);
      }
    };

  const handleGiveUp = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/giveup');
        const giveUpResponse: GiveUpResponse = await response.json();
        setPositions((prevPositions) => [...prevPositions, { word: giveUpResponse.word, position: giveUpResponse.similarity }]);
      } catch (error) {
        console.error("Error fetching give up:", error);
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
        className = {inputError ? "input_error" : ""}
      />
      </div>
      <div className='buttons_block'>
        <button className="submit_button" onClick={handleGuess}>Submit</button>
        <Dropdown>
            <Dropdown.Toggle variant="dropdown-custom" id="dropdown-custom">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 16 16"><path d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"></path></svg>
            </Dropdown.Toggle>
            <Dropdown.Menu>
                <Dropdown.Item onClick={handleTip}>Tip</Dropdown.Item>
                <Dropdown.Item onClick={handleGiveUp}>Give Up</Dropdown.Item>
            </Dropdown.Menu>
        </Dropdown>
      </div>
      <div>
        <ul>
          {sortedPositions.map((pos, index) => (
            <div key={index} className={getPositionStyle(pos.position) + " list_value"}>
              <span>{pos.word} </span>
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

