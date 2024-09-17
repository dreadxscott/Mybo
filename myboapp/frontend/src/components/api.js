//api.js
import axios from "axios";
import { refreshAccessToken } from './auth.js';

//get access token
const getAccessToken = () => localStorage.getItem('access_token');

//setup axios instance
const apiClient = axios.create({
    baseURL: 'http://localhost:8000',
    headers: {
        'Content-Type': 'application/json',
    },
});


// Axios interceptor to attach JWT tokens to request headers
apiClient.interceptors.request.use(
    (config) => {
        const token = getAccessToken();
        if (token) {
            config.headers['Authorization'] = `Bearer ${token}`;  // Attach token to headers
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

// Axios interceptor to handle token refresh when receiving a 401 error
apiClient.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;
        if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            const newToken = await refreshAccessToken();  // Call token refresh logic
            if (newToken) {
                localStorage.setItem('accessToken', newToken);  // Save the new token
                originalRequest.headers['Authorization'] = `Bearer ${newToken}`;  // Attach new token to original request
                return apiClient(originalRequest);  // Retry the request with the new token
            }
        }
        return Promise.reject(error);
    }
);

// API to fetch multiple choice questions and words
export const fetchMultipleChoiceQuestions = async () => {
    try {
        // Fetch Multiple Choice Questions
        const mcqResponse = await apiClient.get('/japanese_learner/api/mcq/');
        console.log('MCQ API Response:', mcqResponse.data);  // Log to verify data

        // Fetch Words
        const wordsResponse = await apiClient.get('/japanese_learner/api/words/');
        console.log('Words API Response:', wordsResponse.data);  // Log to verify data

        // Return both MCQs and words
        return {
            questions: mcqResponse.data,
            words: wordsResponse.data,
        };
    } catch (error) {
        console.error('Error fetching MCQ or Word data:', error);
        throw error;  // Throw the error to be handled by the calling component
    }
};

// API to fetch Question and Answer
export const fetchQuestionAnswerInput = async () => {
    try {
        const response = await apiClient.get('/japanese_learner/api/qa/');
        console.log('QA API Response:', response.data);
        return response.data;
    } catch (error) {
        console.error("Error fetching Q&A data:", error);
        throw error;
    }
};

// API to fetch Story sentences
export const fetchStorySentences = async (storyId) => {
    try {
        const response = await apiClient.get(`/japanese_learner/api/story/${storyId}/sentences/`);
        console.log('Story Sentences API Response:', response.data);
        return response.data;
    } catch (error) {
        console.error('Error fetching story sentences:', error);
        throw error;
    }
};