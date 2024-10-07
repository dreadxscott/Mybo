import React, { useState, useEffect } from 'react';
import { fetchMultipleChoiceQuestions } from './api';
import '../styles/Flashcard.css';  // Ensure you create a CSS file for styling

const MultipleChoiceFlashcard = () => {
  const [questions, setQuestions] = useState([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);  // Track current question
  const [loadingQuestions, setLoadingQuestions] = useState(true);
  const [loadingWords, setLoadingWords] = useState(false);
  const [error, setError] = useState(null);
  const [allWords, setAllWords] = useState([]);
  const [message, setMessage] = useState([]);
  const [isCorrect, setCorrect] = useState([]);
  const [choices, setChoices] = useState([]);


  useEffect(() => {
    const loadingQuestionsAndWords = async () => {
      try {
          // Fetch the data from the API
          const data = await fetchMultipleChoiceQuestions();
          
          // Update the state with the fetched data
          setQuestions(data.questions);  // Set the questions in state
          setAllWords(data.words);  // Set the words in state
      } catch (error) {
          // Handle any error that occurs during the fetch
          setError('Error loading questions or words');
      } finally {
          // Whether successful or not, stop the loading state
          setLoadingQuestions(false);
          setLoadingWords(false)
      }
    }
      loadingQuestionsAndWords();
  }, []);

  useEffect(() => {
    if (!questions || questions.length === 0) return;  // If no questions, do nothing

    // Generate choices for the current question when currentQuestionIndex changes
    const currentQuestion = questions[currentQuestionIndex];
    const newChoices = generateRandomChoices(currentQuestion);
    setChoices(newChoices);
  }, [currentQuestionIndex, questions]);

  if (loadingQuestions) {
    return <div>Loading Questions...</div>;
  }

  if (loadingQuestions) {
    return <div>Loading Questions...</div>;
  }

  if (loadingWords) {
    return <div>Loading Words...</div>
  }

  if (error) {
    return <div>{error}</div>;
  }

  if (!questions || questions.length === 0) {
    return <div>No questions available</div>;
  }

  // Get the current question based on currentQuestionIndex
  const currentQuestion = questions[currentQuestionIndex];

  // Function to generate random choices
  const generateRandomChoices = (currentQuestion) => {
    const correctAnswer = currentQuestion.correct_answer;
    if (!allWords || allWords.length < 3) {
      return [correctAnswer];  // Return just the correct answer if not enough words
    }
    const incorrectWords = allWords.filter(word => word !== correctAnswer);
    incorrectWords.filter(word => word.meaning !== correctAnswer.meaning);


    const randomIncorrectWords = incorrectWords.sort(() => Math.random()-.5);

    const shuffledChoices = [...randomIncorrectWords.sort(() => Math.random() - 5).slice(0, 3) //shuffle choices and get random answers
      , currentQuestion.correct_answer]; // 3 random incorrect answers + correct answer

    return shuffledChoices.sort(() => Math.random() - 0.5);  // Shuffle the choices
  };

  // Navigation handlers for Next/Previous
  const nextQuestion = () => {
    //change to the next question
    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    }

    //load choices
    const newChoices = generateRandomChoices(currentQuestion);
    setChoices(newChoices);

    //clear message
    setMessage(''); //Clear the message when the button is clicked
  };

  const previousQuestion = () => {
    //go to the previous question
    if (currentQuestionIndex > 0) {
      setCurrentQuestionIndex(currentQuestionIndex - 1);
    }

    //load choices
    const newChoices = generateRandomChoices(currentQuestion);
    setChoices(newChoices)

    //clear the message
    setMessage(''); //Clear the message when the button is clicked
  };

    

    // Handle flashcard click
    const handleFlashcardClick = (choice) => {
      if (choice.meaning === currentQuestion.correct_answer.meaning) {
        setMessage('Correct! よくできました!');  // Set the message to "Correct!"
        setCorrect(true);
      } else {
        setMessage('Incorrect. また答え見てよ');  // Set the message to "Incorrect!"
        setCorrect(false);
      }
    };

  return (
    <div className="flashcard-container">
      {/* Flashcard Content */}
      <div className="question-card">

        <h2>Story: {currentQuestion.story.title}</h2>

        <p>{currentQuestion.question_text}</p>

        <div className="flashcards">
          {choices.map((choice, i) => (
            <div key={i} 
            className="flashcard"
              onClick={() => handleFlashcardClick(choice)}>
              {choice.meaning ? choice.meaning : 'No available meaning'}
            </div>
          ))}

        </div>
        {/* Message Display */}
        {message && (
        <p className={`message ${isCorrect ? 'message-correct' : 'message-incorrect'}`}>
          {message}
        </p>
        )}


        <p>Points: {currentQuestion.points}</p>

      </div>
      <div className="navigation-buttons">
        <button onClick={previousQuestion} disabled={currentQuestionIndex === 0}>Previous</button>
        <button onClick={nextQuestion} disabled={currentQuestionIndex === questions.length - 1}>Next</button>
      </div>
    </div>
  );
};

export default MultipleChoiceFlashcard;
