import React, { useState, useEffect } from "react";
import logo from './logo.svg';
import './App.css';

// Replace this with your AI algorithm or word similarity logic
function getWordPosition(word: string, secretWord: string): number {
  // For this example, let's assume we're using a simple function to check similarity
  return word === secretWord ? 1 : 0;
}

const App: React.FC = () => {
  const [secretWord] = useState("example"); // Replace "example" with your secret word
  const [guess, setGuess] = useState("");
  const [positions, setPositions] = useState<Array<{ word: string; position: number }>>([]);

  const handleGuess = async () => {
      // Make a request to the backend API to get the word similarity
      try {
        const response = await fetch('http://127.0.0.1:8000/similarity?word1=' + guess + '&word2=' + secretWord);
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
      <input
        type="text"
        value={guess}
        onChange={(e) => setGuess(e.target.value)}
        placeholder="Enter your guess"
      />
      <button onClick={handleGuess}>Submit</button>
      <div>
        <h2>Word Positions:</h2>
        <ul>
          {sortedPositions.map((pos, index) => (
            <div key={index}>
              {pos.word}: {pos.position}
            </div>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default App;

