import React, { useState, useEffect } from 'react';
import {fetchStorySentences} from './api';

const SentenceList = () => {
  const [sentences, setSentences] = useState([]);

  useEffect(() => {
    const loadSentences = async () => {
        try {
          const data = await fetchStorySentences();  // Await the API call
          setSentences(data.questions);  // Set the questions in state
      } catch (error) {
          setError('Error loading questions or words');
      } finally {
          setLoading(false);  // Stop the loading spinner
      }
    }
        loadSentences();
  }, []);  // The empty array ensures this runs only once when the component is mounted

  return (
    <div>
      <h1>Sentences</h1>
      <ul>
        {sentences.map(sentence => (
          <li key={sentence.id}>{sentence.text}</li>
        ))}
      </ul>
    </div>
  );
};

export default SentenceList;
