<h1>Mybo: A Japanese Language Learning Partner</h1>
<body>
<p>
Mybo is a Japanese Language Learning Partner, named for a portmanteau of 'My' and 'aibo' (the Japanese word for companion).
</p>
<p>
The project is a web-based application that combines multiple-choice flashcards, a sentence navigation system, and questions with answer input to create an overall immersive learning experience for users. It features a clean, simple aesthetic, dynamic page elements, and smooth transitions between English and Japanese. This writeup covers the technology stack, key challenges, and solutions throughout the project.
</p>

<h1>The Stack</h1>
<h2>Technology Stack</h2>
<ol>
  <li>Backend: Django (Python)</li>
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
Mybo contains a backend written in Python, using Django and Django Rest Framework to organize the database of words, sentences, and stories.
</p>
<p>
Mybo uses a frontend written in JavaScript, mainly employing React, to dynamically display the information in a clean and engaging way with animations.
</p>

<h2>Motivation</h2>
<p>
I was motivated to create this project by my love of the Japanese language, as well as Japanese culture, and a desire to share this love with the world. I've been studying Japanese since about 11 years old (I'm 28 as of writing this ReadMe), and I've been studying with a teacher for the past three years. During this time, I've gained insights into what did and did not help me learn, and which aspects of language learning I wish I had focused on. After reflecting, I created Mybo, which you now see in its infancy.
</p>

<h2>Why Did I Build This Project?</h2>
<p>
I built Mybo because I felt like the Japanese functionality on a certain Green Bird app wasn't as extensive as I would like, and didn't give the user an understanding of regular Japanese used by everyday speakers. It offered lessons in a somewhat disjointed fashion. While this app is a credible educational source, I wasn't satisfied when I used it.
</p>

<h2>Problem It Solves</h2>
<p>
A big part of learning Japanese, as it has no direct linguistic relatives (Korean seems to be a distant linguistic relative), is learning to read and write the new script, and incorporating that into other aspects of language learning, such as vocabulary and grammar. It is my hope that Mybo can help tackle this by introducing users to Japanese literature with various grammatical forms and extensive vocabulary, helping them achieve their goals in Japanese language learning.
</p>

<h2>What I Learned</h2>
<p>
While making Mybo, I learned quite a bit. I discovered free resources for learning Japanese that I used as data for my project, including Tadoku and Aozora. Tadoku (多読 meaning 'reading extensively') offers various picture books for learners to improve their reading comprehension. Their story "Hanasuke the Chihuahua" serves as the basis for the story currently available on Mybo.
</p>
<p>
Aozora (青空 meaning 'blue sky') is a Japanese electronic library with a vast collection of Japanese literature that has entered the public domain. I plan to use Aozora to further populate the database with reading material as I continue building a web app that helps people improve their reading comprehension.
</p>
<p>
  On top of that, I learned how to integrate a tech stack with multiple components, namely Javascript using React, and Python using Django. I learned about how imporant, and how much effort goes, into cross-origin resource sharing. I learned the basics of security while creating a sign-in form, and how to secure different modules in my program to where they require credentials for access. 
</p>

<h2>What Makes Mybo Stand Out?</h2>
<p>
Mybo has a beautiful, sleek interface where users can choose 'story mode' to read Japanese literature, as well as flashcard and question-and-answer games to test their newly acquired knowledge. The story has a language toggle button, so users can read it with English subtitles or in Japanese.
</p>
<p>
Currently, the answers to the Q&A section are based on these English translations. A future improvement could be the use of Natural Language Processing (NLP) to accept a wider range of answers, helping users enhance their linguistic flexibility.
</p>

<h2>How to Use This Project</h2>
<p>
To use this project, create a virtual environment and install the required libraries listed in requirements.txt. Download this project inside the virtual environment directory. You may need to add this virtual environment's python interpreter to your local PYTHONPATH. Afterwards, you'll then have to navigate to where the manage.py is (should be in Mybo/myboapp/backend/) and in the command line/terminal run "python manage.py runserver". This will initiate the backend. To initiate the frontend, navigate to the location of the package.json (should be Mybo/myboapp/frontend/), start a command line or terminal from this, and run "nmp start". This will initiate the frontend. 
</p>
<p>
Some issues might arise in recognizing certain model locations within the project; these can be fixed by adding the project's interpreter to your PYTHONPATH. Finally, create a user on the app to log in. If you don't want to make a user, the following credentials should get you in:
<p>username: dread</p>
<p>password: snowfairy99</p>
</p>

<h2>In-depth Overview</h2>
<p>
Please continue reading for a more detailed discussion of the project's stack, the challenges I faced while building it, and how I overcame them. I plan on expanding this as the project grows, and I hope you can join me on this journey.
</p>

<h2>Phase 1: Backend (Django)</h2>
<h3>1.1 Setting Up Django and DRF</h3>
<p>
We began by setting up a Django backend with Django Rest Framework (DRF) for building our API endpoints.
</p>
<p>
<b>Key Components:</b>
<ul>
  <li>Models: The Word and MultipleChoiceQuestion models represent words and questions, respectively. We also defined a CustomUser model that extends Django’s AbstractUser to include additional fields like points, level, and mastered words.</li>
</ul>
<b>Challenges:</b>
<ul>
  <li>We faced issues with model migrations, particularly when creating a CustomUser. The error involved inconsistent migration history, which we fixed by ensuring the migration files were clean and up to date.</li>
</ul>
</p>

<h3>1.2 JWT Authentication</h3>
<p>
We set up JWT (JSON Web Tokens) for user authentication using Django's Simple JWT package. This allowed us to generate tokens when users log in, ensuring secure API access.
</p>
<b>Key Steps:</b>
<ul>
  <li>Created token-based authentication using /api/token/ and /api/token/refresh/ endpoints.</li>
  <li>Configured IsAuthenticated in DRF views to secure routes.</li>
</ul>
<b>Challenges:</b>
<ul>
  <li>Initially, we had issues with JWT tokens not being passed correctly from the frontend. We resolved this by adjusting how tokens were stored and retrieved in localStorage and configuring Axios interceptors.</li>
</ul>

<h3>1.3 Models and APIs</h3>
<p>
We defined several key models:
<ul>
  <li><b>Word:</b> Represents words in both English and Japanese.</li>
  <li><b>MultipleChoiceQuestion:</b> Questions associated with words.</li>
  <li><b>CustomUser:</b> An extension of Django's AbstractUser with fields for tracking progress.</li>
</ul>
<b>APIs:</b>
<ul>
  <li>We created endpoints to fetch questions, answers, and story sentences, utilizing serializers to transform models into JSON responses.</li>
</ul>
</p>

<h2>Phase 2: Frontend (React)</h2>
<h3>2.1 Creating Components</h3>
<p>
We built various React components:
<ul>
  <li><b>SentenceNavigator:</b> Allows users to navigate between different story sentences, switching between Japanese and English.</li>
  <li><b>MultipleChoiceFlashcards:</b> Displays questions as flashcards, allowing users to answer multiple-choice questions.</li>
  <li><b>LoginForm:</b> Handles user authentication, collecting and sending login credentials to the backend.</li>
  <li><b>StoryReader:</b> Presents users with a story in Japanese, toggling the translation between Japanese and English.</li>
</ul>
<b>Challenges:</b>
<ul>
  <li>Handling undefined values: We encountered errors when certain sentences or words weren’t fetched immediately. We solved this by using conditional rendering to ensure the components loaded only when data was available.</li>
  <li>Axios interceptor setup: To handle JWT authentication, we implemented Axios interceptors to add tokens to outgoing requests and refresh them if they expire.</li>
</ul>
</p>

<h3>2.2 Routing with React Router</h3>
<p>
Using React Router, we set up different routes to switch between pages (e.g., login, flashcards, story navigation).
</p>
<b>Challenges:</b>
<ul>
  <li>Some routes like /login weren't functioning as expected due to improper token handling. Resolving authentication issues fixed this.</li>
</ul>

<h3>2.3 Styling with CSS</h3>
<p>
We designed the UI with a clean and functional aesthetic, integrating animations and transitions to enhance user experience.
<ul>
  <li><b>Animated transitions:</b> We used CSS animations for sentence navigation to give a smooth experience.</li>
  <li><b>Dynamic CSS:</b> Styled the sentence translations and toggle button with a sleek color scheme matching the app's branding.</li>
</ul>
<b>Challenges:</b>
<ul>
  <li>CSS alignment issues were resolved by adding proper flexbox-based layouts.</li>
</ul>
</p>

<h2>Phase 3: Authentication and User Flow</h2>
<h3>3.1 Login & Token Management</h3>
<p>
The LoginForm.js component handled user authentication using Axios POST requests to the /api/token/ endpoint, storing tokens in localStorage.
</p>
<b>Challenges:</b>
<ul>
  <li>Users were receiving "Invalid credentials" errors due to mishandling of the response object. Adjusting how Axios handled and stored response tokens solved this.</li>
</ul>

<h3>3.2 Protected Routes</h3>
<p>
We configured protected routes in React so that users could access certain pages (like flashcards and story reader) only if authenticated.
</p>
<b>Challenges:</b>
<ul>
  <li>Ensuring proper logout by removing the JWT token from localStorage and redirecting users to the login page.</li>
</ul>

<h3>3.3 Hide Navigation Links on Login</h3>
<p>
To hide navigation links when users were on the login page, we used the useLocation hook to check the current path and conditionally render links.
</p>

<h2>Challenges and Solutions</h2>
<ul>
  <li><b>JWT Token Handling:</b> We implemented Axios interceptors to ensure seamless token management.</li>
  <li><b>Database Migration Issues:</b> Fixed by deleting old migrations and regenerating them.</li>
  <li><b>Undefined Errors:</b> Used conditional rendering to handle undefined values from the API.</li>
  <li><b>UI Layout:</b> Employed flexbox for consistent alignment and positioning of dynamic content.</li>
</ul>

<h2>Final Thoughts</h2>
<p>
The Mybo Japanese Learning App has turned out to be a robust, interactive learning platform. I successfully integrated Django for the backend, React for the frontend, JWT for authentication, and built a clean, functional interface. The journey was filled with various challenges, but I worked through them methodically.
</p>
</body>
