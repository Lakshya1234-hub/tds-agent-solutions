// Let's get quizSign and email from local storage or app state if available
return {
  quizSign: localStorage.getItem('quizSign') || window.quizSign,
  email: localStorage.getItem('email') || window.email
};
