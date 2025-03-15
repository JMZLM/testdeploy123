const questions = {
    "E/I": [
         {
        question: "In a social gathering, do you feel more energized by interacting with a large group of people or by having one-on-one conversations?",
        options: { a: "Large group interactions (E)", b: "One-on-one conversations (I)" },
        type: "E/I"
    },

    {
        question: "How do you typically recharge after a busy day?",
        options: { a: "Spending time with friends or engaging in social activities (E)", b: "Having some alone time to relax and unwind (I)" },
        type: "E/I"
    },

    {
        question: "When facing a challenge, do you prefer brainstorming ideas with others or working through it independently?",
        options: { a: "Brainstorming with others (E)", b: "Working through it independently (I)" },
        type: "E/I"
    },

    {
        question: "In your free time, do you find yourself seeking out social events and gatherings or enjoying quieter activities at home?",
        options: { a: "Social events and gatherings (E)", b: "Quieter activities at home (I)" },
        type: "E/I"
    },

    {
        question: "How do you feel about small talk?",
        options: { a: "Enjoy it and find it easy to engage in (E)", b: "Find it somewhat awkward or draining (I)" },
        type: "E/I"
    },
    {
        question: "When making decisions, do you rely more on your own instincts and feelings or seek input from others?",
        options: { a: "Seek input from others (E)", b: "Rely on own instincts and feelings (I)" },
        type: "E/I"
    },

    {
        question: "How do you handle new and unfamiliar situations?",
        options: { a: "Embrace them with enthusiasm (E)", b: "Approach them with caution (I)" },
        type: "E/I"
    },

    {
        question: "In a work or team setting, do you prefer open office spaces and collaboration or individual workspaces?",
        options: { a: "Open office spaces and collaboration (E)", b: "Individual workspaces (I)" },
        type: "E/I"
    },

    {
        question: "How do you typically respond to being the focal point in a group setting?",
        options: { a: "Embrace it and feel at ease (E)", b: "Prefer to avoid being the center of attention (I)" },
        type: "E/I"
    },

    {
        question: "When planning a weekend, do you lean towards social plans with friends or quiet time for yourself?",
        options: { a: "Social plans with friends (E)", b: "Quiet time for yourself (I)" },
        type: "E/I"
    },


        // Add remaining E/I questions here...
    ],
    "S/N": [

    {
        question: "When faced with a problem, do you prefer to rely on concrete facts and details or explore possibilities and potential meanings?",
        options: { a: "Rely on concrete facts and details (S)", b: "Explore possibilities and potential meanings (N)" },
        type: "S/N"
    },

    {
        question: "How do you approach new information or learning?",
        options: { a: "Prefer practical, hands-on experiences (S)", b: "Enjoy exploring theories and concepts (N)" },
        type: "S/N"
    },

    {
        question: "In a conversation, are you more focused on the present and current details or on future possibilities and patterns?",
        options: { a: "Present and current details (S)", b: "Future possibilities and patterns (N)" },
        type: "S/N"
    },

    {
        question: "When planning a trip, do you prefer to have a detailed itinerary and clear schedule or leave room for spontaneous experiences and changes?",
        options: { a: "Detailed itinerary and clear schedule (S)", b: "Leave room for spontaneous experiences and changes (N)" },
        type: "S/N"
    },

    {
        question: "How do you make decisions?",
        options: { a: "Based on practical considerations and real-world implications (S)", b: "Consider potential outcomes and future possibilities (N)" },
        type: "S/N"
    },

    {
        question: "When working on a project, do you tend to focus on the specific tasks at hand or the overall vision and goals",
        options: { a: "Specific tasks at hand (S)", b: "Overall vision and goals (N)" },
        type: "S/N"
    },

    {
        question: "In a group discussion, do you prefer to stick to the facts and details or contribute ideas and theories?",
        options: { a: "Stick to facts and details (S)", b: "Contribute ideas and theories (N)" },
        type: "S/N"
    },

    {
        question: "How do you handle unexpected changes or disruptions to your plans?",
        options: { a: "Prefer stability and may find changes challenging (S)", b: "Adapt well to changes and enjoy the flexibility (N)" },
        type: "S/N"
    },

    {
        question: "When recalling a past event, do you focus more on the specific details and occurrences or the overall impressions and meanings?",
        options: { a: "Specific details and occurrences (S)", b: "Overall impressions and meanings (N)" },
        type: "S/N"
    },

    {
        question: "When reading a book or watching a movie, do you pay close attention to the plot and events or look for deeper meanings and symbolism?",
        options: { a: "Plot and events (S)", b: "Deeper meanings and symbolism (N)" },
        type: "S/N"
    },


        // Add remaining S/N questions here...
    ],
    "T/F": [
        {
        question: "When making decisions, do you prioritize logical analysis and objective criteria or consider the impact on people and relationships?",
        options: { a: "Logical analysis and objective criteria (T)", b: "Consider the impact on people and relationships (F)" },
        type: "T/F"
    },

    {
        question: "How do you handle criticism or feedback?",
        options: { a: "Focus on the facts and seek constructive solutions (T)", b: "Consider the emotional aspects and how it affects relationships (F)" },
        type: "T/F"
    },

    {
        question: "When faced with a problem, do you rely more on your head and reason or your heart and empathy?",
        options: { a: "Head and reason (T)", b: "Heart and empathy (F)" },
        type: "T/F"
    },

    {
        question: "How do you prioritize tasks and responsibilities?",
        options: { a: "Based on logical importance and efficiency (T)", b: "Considering the values and impact on people (F)" },
        type: "T/F"
    },

    {
        question: "In a group decision-making process, do you tend to advocate for the most logical and rational choice or the one that aligns with personal values and harmony?",
        options: { a: "Logical and rational choice (T)", b: "Aligns with personal values and harmony (F)" },
        type: "T/F"
    },

    {
        question: "When giving feedback, do you focus on providing objective analysis or consider the individual's feelings and emotional response?",
        options: { a: "Objective analysis (T)", b: "Consider the individual's feelings and emotional response (F)" },
        type: "T/F"
    },

    {
        question: "How do you express your opinions in a debate or discussion?",
        options: { a: "Emphasize facts, evidence, and logical reasoning (T)", b: "Consider personal values, emotions, and the impact on people (F)" },
        type: "T/F"
    },

    {
        question: "When solving a problem, do you prioritize efficiency and effectiveness, even if it means being blunt, or do you consider the feelings of those involved?",
        options: { a: "Prioritize efficiency and effectiveness (T)", b: "Consider the feelings of those involved (F)" },
        type: "T/F"
    },

    {
        question: "In a work environment, do you value objective performance metrics and results or prioritize a positive and supportive team culture?",
        options: { a: "Objective performance metrics and results (T)", b: "Positive and supportive team culture (F)" },
        type: "T/F"
    },

    {
        question: "How do you approach conflict resolution?",
        options: { a: "Focus on finding logical solutions and compromises (T)", b: "Consider the emotional needs and harmony of individuals involved (F)" },
        type: "T/F"
    },




        // Add remaining T/F questions here...
    ],
    "J/P": [
       {
        question: "How do you feel about making plans and sticking to a schedule?",
        options: { a: "Enjoy making plans and prefer a structured schedule (J)", b: "Prefer flexibility and spontaneity, dislike strict schedules (P)" },
        type: "J/P"
    },

    {
        question: "When starting a project, do you prefer to have a detailed plan in place or do you like to explore possibilities and figure it out as you go?",
        options: { a: "Prefer to have a detailed plan (J)", b: "Like to explore possibilities and figure it out as you go (P)" },
        type: "J/P"
    },

    {
        question: "How do you approach deadlines?",
        options: { a: "Work diligently to meet deadlines well in advance (J)", b: "Tend to work better under pressure and close to the deadline (P)" },
        type: "J/P"
    },

    {
        question: "In a work setting, do you prefer a clear and organized workspace or are you comfortable with a more flexible and adaptable environment?",
        options: { a: "Prefer a clear and organized workspace (J)", b: "Comfortable with a more flexible and adaptable environment (P)" },
        type: "J/P"
    },

    {
        question: "When packing for a trip, do you plan and make a checklist in advance or pack on the fly, throwing in what feels right at the moment?",
        options: { a: "Plan and make a checklist in advance (J)", b: "Pack on the fly, throwing in what feels right (P)" },
        type: "J/P"
    },

    {
        question: "What do you do when your plans suddenly change?",
        options: { a: "Dislike unexpected changes and prefer to stick to the original plan (J)", b: "Adapt well to unexpected changes and enjoy the flexibility (P)" },
        type: "J/P"
    },

    {
        question: "When faced with a new opportunity, do you prefer to consider the advantages and disadvantages prior to making a decision or go with the flow and see where it takes you ?",
        options: { a: "Consider the advantages and disadvantages prior to deciding (J)", b: "Go with the flow and see where it takes you (P)" },
        type: "J/P"
    },

    {
        question: "How do you approach work tasks?",
        options: { a: "Like to have a set plan and follow it step by step (J)", b: "Enjoy being flexible and adapting as the situation evolves (P)" },
        type: "J/P"
    },

    {
        question: "When organizing your day, do you prefer to have a to-do list with specific tasks and deadlines or keep it open-ended and see where the day takes you?",
        options: { a: "To-do list with specific tasks and deadlines (J)", b: "Keep it open-ended and see where the day takes you (P)" },
        type: "J/P"
    },

    {
        question: "How do you feel about routine and predictability?",
        options: { a: "Prefer routine and find comfort in predictability (J)", b: "Dislike routine and enjoy spontaneity (P)" },
        type: "J/P"
    },

        // Add remaining J/P questions here...
    ]
};

let selectedQuestions = [];
let currentQuestionIndex = 0;
let scores = { E: 0, I: 0, S: 0, N: 0, T: 0, F: 0, J: 0, P: 0 };

// Shuffle and select 30 questions per category
function shuffleAndSelect(questionsArray, limit) {
    const shuffled = questionsArray.sort(() => Math.random() - 0.5);
    return shuffled.slice(0, limit);
}

// Initialize the quiz with 30 questions from each category
function initializeQuiz() {
    selectedQuestions = [
        ...shuffleAndSelect(questions["E/I"], 6).map(q => ({ ...q, type: "E/I" })),
        ...shuffleAndSelect(questions["S/N"], 6).map(q => ({ ...q, type: "S/N" })),
        ...shuffleAndSelect(questions["T/F"], 7).map(q => ({ ...q, type: "T/F" })),
        ...shuffleAndSelect(questions["J/P"], 6).map(q => ({ ...q, type: "J/P" }))
    ];
    loadQuestion();
}

function loadQuestion() {
    const questionContainer = document.getElementById("question-container");
    const question = selectedQuestions[currentQuestionIndex];

    questionContainer.innerHTML = `
        <p>${currentQuestionIndex + 1} / ${selectedQuestions.length}. ${question.question}</p>
        <div class="option" onclick="selectOption('a')">${question.options.a}</div>
        <div class="option" onclick="selectOption('b')">${question.options.b}</div>
    `;
}

function selectOption(answer) {
    const question = selectedQuestions[currentQuestionIndex];

    if (answer === "a") {
        if (question.type === "E/I") scores.E++;
        else if (question.type === "S/N") scores.S++;
        else if (question.type === "T/F") scores.T++;
        else if (question.type === "J/P") scores.J++;
    } else {
        if (question.type === "E/I") scores.I++;
        else if (question.type === "S/N") scores.N++;
        else if (question.type === "T/F") scores.F++;
        else if (question.type === "J/P") scores.P++;
    }

    currentQuestionIndex++;
    if (currentQuestionIndex < selectedQuestions.length) {
        loadQuestion();
    } else {
        displayResult();
    }
}

function displayResult() {
    const personalityType = determinePersonality();
    window.location.href = `/result?personality_type=${personalityType}`;
}

function determinePersonality() {
    const type = (scores.E > scores.I ? 'E' : 'I') +
                 (scores.S > scores.N ? 'S' : 'N') +
                 (scores.T > scores.F ? 'T' : 'F') +
                 (scores.J > scores.P ? 'J' : 'P');
    return type;
}

document.addEventListener("DOMContentLoaded", initializeQuiz);
