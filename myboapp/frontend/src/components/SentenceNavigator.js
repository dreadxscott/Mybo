import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../styles/Story.css';
import {fetchStorySentences} from './api'

const SentenceNavigator = () => {
  const [animationClass, setAnimationClass] = useState('slide-in-right'); // Default to sliding in from the right
  const [sentences, setSentences] = useState([]); // Store the sentences
  const [currentSentenceIndex, setCurrentSentenceIndex] = useState(0); // Track the current sentence index
  const [loading, setLoading] = useState(true); // Loading state for the API call
  const [storyId, setStoryId] = useState([]);
  const [error, setError] = useState(null);


  // Fetch the sentences from the API
  useEffect(() => {
    const loadSentences = async () => {
      const token = localStorage.getItem('access_token');
      
      if (!token) {
        setError('User not authenticated');
        return; // Do not make the request if there is no token
      }

      setStoryId(1);

      try {
        const data = await fetchStorySentences(storyId);  // Await the API call
        setSentences(data);  // Set the sentences in state
      } catch (error) {
        setError('Error loading sentences');
        console.error('Error fetching sentences:', error);
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

    // Ensure sentences are available before rendering
    if (!sentences.length) {
      return <div>No sentences available.</div>;
    }

  // Extract the current sentence, keyword, and meaning from the current sentence object
  const currentSentence = sentences[currentSentenceIndex];
  const { sentence, keyword, meaning } = currentSentence;

  return (
    <div className="story-container">
      <div className="content">
        {/* Story Text with Keyword Highlight */}
        <div className={`story-text ${animationClass}`}>
          {sentence.split(keyword).map((part, index) => (
            <React.Fragment key={index}>
              {part}
              {index < sentence.split(keyword).length - 1 && (
                <span className="keyword">{keyword}</span>
              )}
            </React.Fragment>
          ))}
        </div>

        {/* Navigation Buttons */}
        <div className="story-buttons">
          <button onClick={prevSentence} disabled={currentSentenceIndex === 0}>
            Previous
          </button>
          <button onClick={nextSentence} disabled={currentSentenceIndex === sentences.length - 1}>
            Next
          </button>
        </div>
      </div>
    </div>
  );
};

export default SentenceNavigator;
