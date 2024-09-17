//auth.js
import axios from 'axios';
import Cookies from 'js-cookie'

// Log in user and store the access and refresh tokens
// Make a GET request to Django to trigger setting the CSRF cookie
export const getCSRFToken = async () => {
  try {
      await axios.get('http://localhost:8000/api/csrf/');  // Dummy GET request
      console.log('CSRF token set in cookies');
  } catch (error) {
      console.error('Error fetching CSRF token', error);
  }
};

export const login = async (username, password) => {
    try {
      const response = await axios.post("http://localhost:8000/api/token/", {
        username,
        password,
      });

      localStorage.setItem('access_token', response.data.access);
      localStorage.setItem('refresh_token', response.data.refresh);

      axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
      
      return response.data;
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    }
  };



export const signup = async (username, email, password1, password2) => {
  try {
    // Step 1: Get CSRF token (this will set the cookie)
    await getCSRFToken();  // Ensure the CSRF token is set before proceeding
    
    // Step 2: Get CSRF token from cookies
    const csrftoken = Cookies.get('csrftoken');  // Get the CSRF token from the cookie

    const response = await axios.post("http://localhost:8000/accounts/signup/", {
      "username": username, 
      "email":email,
      "password1":password1, 
      "password2":password2,
    },
    {
      headers: {
        'X-CSRFToken': csrftoken,  // Include CSRF token in the headers
        'Content-Type': 'application/x-www-form-urlencoded' // Ensure Content-Type is set
      },
      withCredentials: true  // Important: Send cookies with the request);
    });
    return response.data;
  } catch (error) {
    console.error('Signup error:', error);
    throw error;
  }
};


// Refresh access token using the refresh token
export const refreshAccessToken = async () => {
    try {
      const refreshToken = localStorage.getItem('refresh_token');
      const response = await axios.post('http://localhost:8000/api/token/refresh/', {
        refresh: refreshToken,
      });
      localStorage.setItem('access_token', response.data.access);
      axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
      return response.data.access;
    } catch (error) {
      console.error('Error refreshing access token:', error);
      throw error;
    }
  };

  export const Logout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    delete axios.defaults.headers.common['Authorization']

    // Redirect to the login page
    window.location.href = '/login';  // You can use a React Router method instead of window.location.href if needed

  };

  export const isLoggedIn = () => {
    return !!localStorage.getItem('access_token');
  }