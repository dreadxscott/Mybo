//QUestionAnswerInput.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {fetchQuestionAnswerInput} from './api';
import "../styles/QuestionAnswer.css";

const QuestionAnswerComponent = () => {
    const [responseMessage, setResponseMessage] = useState('');  // State to display server response
    const [questions, setQuestions] = useState([]);
    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);  // Track current question
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    //Pulls information from API Endpoint*
    useEffect(() => {
        const loadingQuestionsforInput = async () => {
            try {
                const data = await fetchQuestionAnswerInput();  // Await the API call
                setQuestions(data);  // Set the questions in state
                setLoading(false);
            } catch (error) {
                setError('Error loading questions');
                setError(false);
            } finally {
                setLoading(false);  // Stop the loading spinner
            }
        }
            loadingQuestionsforInput();
    }, 
    [])

    if (loading) {
    return <div> Loading...</div>
    }

    if (error) {
        return <div> {error} </div>
    }

    //Handle question data from the API Endpoint
    if (!questions || questions.length === 0) {
        console.log("Questions: ", questions);
        return <div>No questions available</div>;
    }

    // Navigation handlers for Next/Previous
    const nextQuestion = () => {
        if (currentQuestionIndex < questions.length - 1) {
        setCurrentQuestionIndex(currentQuestionIndex + 1);
        setResponseMessage('');  // Clear the response message when moving to previous question
        }
    };

    const previousQuestion = () => {
        if (currentQuestionIndex > 0) {
        setCurrentQuestionIndex(currentQuestionIndex - 1);
        setResponseMessage('');  // Clear the response message when moving to previous question
        }
    };

    //Get current question based on index
    const currentQuestion = questions[currentQuestionIndex];

    //Handles inputs from the textbox, sending them to backend
    const handleSubmit = async (e) => {
        e.preventDefault();
        
        const form = e.target;
        const formData = new FormData(form);
        const formJson = Object.fromEntries(formData)

        const submissionData = {
            question : currentQuestion.question,
            answer : formJson.My_input
        }

        console.log(submissionData)

        try {
            const response = await axios.post('http://localhost:8000/japanese_learner/api/form-submit/', 
                JSON.stringify(submissionData) , {
                 headers: {
                    'Content-Type': 'multipart/form-data',
                },
        });

        //Log the response and update the data
        console.log(response.data.input);
        setResponseMessage(response.data.input);

    } catch (error) {
        console.error("There was an error submitting the form", error);
    }
    };

    return (
        <div className="qa-container">
            <h2 className="qa-title">Story: {currentQuestion.story.title}</h2>
            <p className="qa-question">{currentQuestion.question}</p>
            <p className="qa-points">Points: {currentQuestion.points}</p>
            <form onSubmit={handleSubmit}>
                <label>
                    Answer/答え: <input className="qa-input" name="My_input" />
                    <button className="qa-submit" type="submit">Submit</button>
                </label>
            </form>
            {responseMessage && (
            <div className="response-message">
                <h3>Response:</h3>
                <p>{responseMessage}</p>  {/* Show the response */}
            </div>
            )}
            <div className="navigation-buttons">
                <button onClick={previousQuestion} disabled={currentQuestionIndex === 0}>
                    Previous
                </button>
                <button onClick={nextQuestion} disabled={currentQuestionIndex === questions.length - 1}>
                    Next
                </button>
            </div>
        </div>
    );
}

export default function QuestionAnswer() {
    return (
        <div>
                <QuestionAnswerComponent />
        </div>
    )
}