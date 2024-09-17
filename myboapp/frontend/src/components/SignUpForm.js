import React, {useState} from 'react';
import {signup} from './auth';

const SignUpForm = (e) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [emailAddress, setEmailAddress] = useState("");
    const [reconfirmPassword, setReconfirmPassword] = useState("");
    const [error, setError] = useState([]);

    // Logic to handle sign-up
    const handleSubmit = async (e) => {
        e.preventDefault(); // Prevent form from refreshing the page

        if (password !== reconfirmPassword) {
            setError("Passwords do not match.");
            return;
        }
        
        try {
            const response = await signup(username, emailAddress, password, reconfirmPassword);
            console.log(response.data);
            // Redirect to /Story after successful signup
            window.location.href = '/Story';

        } catch (error) {
            console.error("Signup error: ", error)
            setError("Signup failed. Please try again.");
        }
    };

    return (
        <div className="login-container">
        <div className="welcome-message">Welcome to Mybo, Your Japanese Language Partner</div>
        <div className="japanese-message">日本語勉強の相棒マイボウにようこそ！</div>
        <div className="sign-up-message">Please Sign Up to Continue</div>
        <div className="login-form">
            <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
            />
            <input
                type="text"
                placeholder="Email Address"
                value={emailAddress}
                onChange={(e) => setEmailAddress(e.target.value)}
                />
            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)
                }
            />
                <input
                type="password"
                placeholder="Re-enter Password"
                value={reconfirmPassword}
                onChange={(e) => setReconfirmPassword(e.target.value)}
            />
            <button type="submit">Sign Up</button>
            </form>
            {error && <p>{error}</p>}
        </div>
        </div>
    );
};
export default SignUpForm;

