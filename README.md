<h1>Mybo: A Japanese Language Learning Partner</h1>
<body>
<p>
Mybo is a Japanese Language Learning Partner, named for a portmanteau of 'My' and 'aibo' (the Japanese word for companion)
</p>
<p>
The project is a web-based application that combines multiple-choice flashcards, a sentence navigation system, and questions with answer input, to create an overall immersive learning experience for users. It features a clean, simple aesthetic, dynamic page elements, and smooth transitions between English and Japanese. This writeup covers the technology stack, key challenges, and solutions throughout the project.
</p>
<h1>The Stack:</h1>
<h2>Technology Stack</h2>

<ol>
<li>Backend: Django (Python) </li>
       <ul>
       <li>Django Rest Framework (DRF) for building APIs.</li>
       <li>JWT (JSON Web Token) for authentication.</li>
       </ul>
<li>Frontend: React (JavaScript)</li>
       <ul>
       <li>Axios for API calls.</li>
        <li>React Router for navigation.</li>
       <li>CSS for styling.</li>
       </ul>
<li>Database: SQLite (for local development).</li>
</ol>
<p>
Mybo contains a backend written in Python, using Django and Django Rest Framework to organize the database of words, sentences, and stories
</p>
<p>
Mybo uses a frontend written in Javascript, mainly employing React, to dynamically display the information in a clean and engaging way with animations
</p>


<h4>What was your motivation?</h4>
<p>
I was motivated to create this project by my love of the Japanese language, as well as Japanese culture, and a desire to share this love with the world. I've been studying Japanese since about 11 years old (I'm 28 as of writing this ReadMe), and I've been studying with a teacher for the past three years. During this time, I've gained insights into what did and did not help me learn, and which aspects of language learning I wish I had focused on in my time studying. After reflecting, I took to making Mybo, which yous see now in its infancy. 
</p>
<p>
Why did you build this project?
I built Mybo because I felt like the Japanese functionality on a certain Green Bird app wasn't as extensive as I would like, and didn't give the User an understanding of regular Japanese used by everyday speakers, instead offering speakers lessons in a somewhat disjointed fashion. And while I'm sure this app is a credible educational source, I wasn't satisfied when I used it. 
</p>
<p>
What problem does it solve?
A big part of learning Japanese, as it has no direct linguistic relatives (Korean seems to be a distant linguistic relative), learning to read and write the new script, and incorporate that into other aspects of language learning e.g. vocabulary and grammar, is quite the challenge. It is my hope that Mybo can help tackle this through introducing Users to Japanese literature with various grammatical forms and extensive vocabulary to help them achieve their goals in Japanese language learning. 
</p>
<p>
What did you learn?
While making Mybo I learned quite a bit. I learned of the free resources for learning Japanese that I brought together for the data in my project, including Tadoku and Aozora. Tadoku (多読 meaning 'reading extensively') is a website that offers various picture books for Japanese learners to improve their reading comprehension. Their story "Hanasuke the Chihuahua" acted as the basis for the story available on Mybo at the moment. 
Aozora (青空 meaning 'blue sky') is a Japanese electronic library with a vast quantity of Japanese literature that's entered the public domain. I plan to use Aozora to populate the database further with reading material to continue my efforts of building a web app than can help people improve their reading comprehension. 
</p>
<p>
What makes your project stand out? 
Mybo has a beautiful, sleek interface, and users are able to choose story mode, to read a story, as well as a flashcard and question-and-answer game to test their newly acquired knowledge. The story has a language toggle button, so users can read the story with English subtitles, or can read the story in Japanese.
</p>
<p>
Currently, the answers to the Q&A section are to be found in these English translations. A potential future improvement would be the use of NLP to accept a wider range of answers, as this would help users increase their linguistic flexibility. 
</p>
<p>
In order to use this project, download the whole repository. Create a virtual environment, and add to it the libraries in the requirements.txt. Some issues may arise with recognizing the location of certain models within the project. These can be fixed by adding the interpreter for the project to your PYTHONPATH. Finally, you will be able to log in by creating a user on the app itself. 
</p>
<p>
Please continue reading for a more in-depth discussion on the ins-and-outs of the project, the stack, challenges I faced while building, and how I overcame them. I plan on expanding this as the project grows, and hope you can join me on the journey. 
</p>
Phase 1: Backend (Django)
1.1 Setting up Django and DRF
We began by setting up a Django backend with Django Rest Framework (DRF) for building our API endpoints.
Key Components:
    • Models: The Word and MultipleChoiceQuestion models were created to represent words and questions respectively. We also defined a CustomUser model that extends Django’s AbstractUser to include additional fields like points, level, and mastered words.
Challenges:
    • We had issues with model migrations, particularly when creating a CustomUser. The error involved inconsistent migration history. We fixed it by ensuring the migration files were clean and up to date.
1.2 JWT Authentication
We set up JWT (JSON Web Tokens) for user authentication using Django's Simple JWT package. This allowed us to generate tokens when users log in, ensuring secure API access.
Key Steps:
    • Created token-based authentication using /api/token/ and /api/token/refresh/ endpoints.
    • We configured IsAuthenticated in DRF views to secure routes.
Challenges:
    • Initially, we had issues with JWT tokens not being passed correctly from the frontend. By adjusting how tokens were stored and retrieved in localStorage and configuring Axios interceptors, we resolved this.
1.3 Models and APIs
We defined several key models:
    • Word: Represents words in both English and Japanese.
    • MultipleChoiceQuestion: Questions associated with words.
    • CustomUser: An extension of Django's AbstractUser with fields for tracking progress.
APIs:
    • We created endpoints to fetch questions, answers, and story sentences, utilizing serializers to transform models into JSON responses.

Phase 2: Frontend (React)
2.1 Creating Components
We built various React components:
    1. SentenceNavigator: This component allows users to navigate between different story sentences, switching between Japanese and English.
    2. MultipleChoiceFlashcards: Displays questions as flashcards, allowing users to answer multiple-choice questions.
    3. LoginForm: Handles user authentication, collecting and sending login credentials to the backend.
    4. StoryReader: A feature that presents users with a story in Japanese, toggling the translation between Japanese and English.
Challenges:
    • Handling undefined values: We encountered errors when certain sentences or words weren’t fetched immediately. We solved this by using conditional rendering to ensure the components loaded only when data was available.
    • Axios interceptor setup: To handle JWT authentication, we implemented Axios interceptors to add tokens to outgoing requests and refresh them if they expire.
2.2 Routing with React Router
Using React Router, we set up different routes to switch between pages (e.g., login, flashcards, story navigation).
Challenges:
    • Initially, we had issues where some routes like /login weren't functioning as expected because of improper token handling. Once we resolved authentication, the routing worked correctly.
2.3 Styling with CSS
We designed the UI with a clean and functional aesthetic, integrating animations and transitions to give users a smooth experience.
    • Animated transitions: For sentence navigation, we used CSS animations (e.g., slide-in, slide-out) to improve the user experience.
    • Dynamic CSS: We styled the sentence translations and toggle button using a sleek color scheme matching the app's branding.
Challenges:
    • CSS alignment issues: The placement of buttons and text elements was sometimes inconsistent, particularly for translations. We fixed this by adding proper flexbox-based layouts.

Phase 3: Authentication and User Flow
3.1 Login & Token Management
The LoginForm.js was responsible for user authentication. We handled login through Axios POST requests to the /api/token/ endpoint and stored tokens in localStorage. Additionally, we refreshed tokens using /api/token/refresh/.
Challenges:
    • We encountered an issue where users were receiving "Invalid credentials" errors despite logging in successfully. This was due to mishandling the response object. Fixing the way Axios handled and stored response tokens solved this issue.
3.2 Protected Routes
We configured protected routes in React so that users could only access certain pages (like the flashcards and story reader) if they were authenticated.
Challenges:
    • Logout: We had to ensure that the JWT token was removed from localStorage and users were redirected to the login page on logout.
3.3 Hide Navigation Links on Login
To hide navigation links when users were on the login page, we used the useLocation hook to check if the current path was /login. If so, we hid the navigation.

Challenges and Solutions
    1. JWT Token Handling: We initially had difficulty properly attaching tokens to outgoing requests and refreshing them. By setting up Axios interceptors, we ensured seamless token management.
    2. Database Migration Issues: Inconsistent migration history caused problems during development. Deleting old migrations and regenerating them solved this.
    3. Undefined Errors: We dealt with several undefined value errors when data was fetched from the API. By adding checks and conditional rendering, we resolved these.
    4. UI Layout: CSS alignment and positioning issues, particularly for dynamic content like translations, required flexbox solutions and careful margin/padding adjustments.

Final Thoughts
The Mybo Japanese Learning App has turned out to be a robust, interactive learning platform. I successfully integrated Django for the backend, React for the frontend, JWT for authentication, and built a clean, functional interface. The journey was filled with various challenges, but I worked through them methodically.
</body>
