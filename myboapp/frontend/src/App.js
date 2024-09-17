// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link, useLocation } from 'react-router-dom';
import MultipleChoiceFlashcard from './components/MultipleChoiceFlashcards';
import QuestionAnswer from './components/QuestionAnswerInput';
import LoginForm from './components/LoginForm';
import SignUpForm from "./components/SignUpForm";
import StoryReader from './components/StoryReader';
import { isLoggedIn, Logout } from './components/auth'; // Import the isLoggedIn and Logout functions
import './styles/Logout.css';

const App = () => {
  return (
    <Router>
      <AppContent />
    </Router>
  );
};

// Separate component to use `useLocation()`
const AppContent = () => {
  const location = useLocation();

  return (
    <div>
      {/* Conditionally render the navigation links and logout button based on the current path */}
      {location.pathname !== '/login' && (
        <>
          {/* Navigation Links */}
          <nav>
            <ul>
              <li>
                <Link to="/login">Home</Link>
              </li>
              <li>
                <Link to="/story">Story</Link>
              </li>
              <li>
                <Link to="/flashcards">Flashcards</Link>
              </li>
              <li>
                <Link to="/question-answer">Q&A</Link>
              </li>
            </ul>
          </nav>
          
          {/* Show the Logout button when logged in */}
          {isLoggedIn() && (
            <button className="logout-btn" onClick={Logout}>
              Logout
            </button>
          )}
        </>
      )}
      
      <Routes>
        <Route path="/flashcards" element={<MultipleChoiceFlashcard />} />
        <Route path="/question-answer" element={<QuestionAnswer />} />
        <Route path="/" element={<LoginForm />} />
        <Route path="/story" element={<StoryReader />} />
        <Route path="/login" element={<LoginForm />} />
        <Route path="/signup" element={<SignUpForm />} />
      </Routes>
    </div>
  );
};

export default App;
