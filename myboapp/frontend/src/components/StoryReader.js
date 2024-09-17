import React, { useState, useEffect } from 'react';
import '../styles/Story.css';
import { fetchStorySentences } from './api';

const StoryReader = ({ storyId=1 }) => {
  const [animationClass, setAnimationClass] = useState('slide-in-right'); // Default to sliding in from the right
  const [sentences, setSentences] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [currentSentenceIndex, setCurrentSentenceIndex] = useState(0); // Track the current sentence index
  const [showEnglish, setShowEnglish] = useState(true);  // State to toggle English visibility

  // Function to toggle between English and Japanese
  const toggleEnglish = () => {
    setShowEnglish(!showEnglish); // Toggle between showing/hiding English translation
  };

  useEffect(() => {
    const loadSentences = async () => {
      try {
        const data = await fetchStorySentences(storyId);  // Await the API call
        setSentences(data);  // Set the sentences in state
      } catch (error) {
        setError('Error loading sentences');
        //console.error(error);
      } finally {
        setLoading(false);  // Stop the loading spinner
      }
    };
    loadSentences();
  }, [storyId]);

  // Handle next sentence with animation
  const nextSentence = () => {
    if (currentSentenceIndex < sentences.length - 1) {
      setAnimationClass('slide-out-right'); // Slide out current text to the right
      setTimeout(() => {
        setCurrentSentenceIndex(currentSentenceIndex + 1); // Move to next sentence
        setAnimationClass('slide-in-left'); // Slide in new text from the left
      }, 500); // Adjust timeout to match animation duration
    }
  };

  // Handle previous sentence with animation
  const prevSentence = () => {
    if (currentSentenceIndex > 0) {
      setAnimationClass('slide-out-left'); // Slide out current text to the left
      setTimeout(() => {
        setCurrentSentenceIndex(currentSentenceIndex - 1); // Move to previous sentence
        setAnimationClass('slide-in-right'); // Slide in new text from the right
      }, 500); // Adjust timeout to match animation duration
    }
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  // Make sure sentences are available before accessing current sentence
  const currentSentence = sentences[currentSentenceIndex];
  const sentence = currentSentence?.sentence || '';
  const meaning = currentSentence?.meaning || '';
  const keyword = currentSentence?.keyword || '';

  // Function to highlight the keyword in the sentence
  const renderHighlightedSentence = (sentence, keyword) => {
    if (!keyword || !sentence.includes(keyword)) {
      return <span>{sentence}</span>; // If no keyword or keyword not found, render sentence normally
    }

    const parts = sentence.split(keyword);  // Split sentence by the keyword
    return (
      <>
        {parts.map((part, index) => (
          <React.Fragment key={index}>
            {part}
            {index < parts.length - 1 && <span className="keyword">{keyword}</span>}
          </React.Fragment>
        ))}
      </>
    );
  };

  return (
    <div className="story-container">
      {/* Display the current sentence with keyword highlighted */}
      <div className={`story-text ${animationClass}`}>
        <p>{renderHighlightedSentence(sentence, keyword)}</p>
        {showEnglish && <p className="english-translation">{meaning}</p>} {/* Show English translation below */}
      </div>
      {/* Navigation Buttons */}
      <div className="story-buttons">
        <button onClick={prevSentence} disabled={currentSentenceIndex === 0}>
          {!showEnglish ? '前へ' : 'Previous'}
        </button>
        <button onClick={nextSentence} disabled={currentSentenceIndex === sentences.length - 1}>
          {!showEnglish ? '次へ' : 'Next'}
        </button>
        {/* Button to toggle the language */}
        <div className='toggle-language-btn'>
        <button className="toggle-language-btn" onClick={toggleEnglish}>
          {showEnglish ? '日本語' : 'English'}
        </button>
        </div>
      </div>
    </div>
  );
};

export default StoryReader;
