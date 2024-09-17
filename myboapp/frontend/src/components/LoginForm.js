import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { login } from './auth';
import '../styles/Mybo.css';  // Import the Login CSS
import '../styles/Logout.css'; //import the Logout CSS

const LoginForm = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await login(username, password);  // Call login function

      // Store the access token and refresh token in localStorage
      localStorage.setItem('accessToken', response.access);
      localStorage.setItem('refreshToken', response.refresh);

      setError(null);
      window.location.href = '/Story';  // Redirect to the homepage or dashboard
    } catch (error) {
      setError('Invalid credentials, please try again.');
    }
  };

  return (
    <div className="login-container">
      <div className="welcome-message">Welcome to Mybo, Your Japanese Language Partner</div>
      <div className="japanese-message">日本語勉強の相棒マイボウにようこそ！</div>
      <div className="login-form">
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button type="submit">Login</button>
          <div>
           <Link to="/signup" className='sign-up-link'>Not a member? Sign Up Today!</Link>
          </div>
        </form>
        {error && <p>{error}</p>}
      </div>
    </div>
  );
};

export default LoginForm;
