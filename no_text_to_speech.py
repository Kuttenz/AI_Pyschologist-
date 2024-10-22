import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

class MentalHealthChatbot:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')

    def respond(self, user_input):
        main_issue = self.extract_main_issue(user_input)
        if main_issue:
            return self.generate_solution(main_issue)
        else:
            main_feeling = self.extract_main_feeling(user_input)
            if main_feeling:
                return self.generate_solution(main_feeling)
            else:
                return "I'm sorry, I couldn't understand the issue. Could you please rephrase?"

    def extract_main_issue(self, user_input):
        tokens = word_tokenize(user_input)
        tagged_tokens = pos_tag(tokens)
        main_verbs = [word for word, pos in tagged_tokens if pos.startswith('VB')]
        for word, pos in tagged_tokens:
            if pos.startswith('NN') and word in main_verbs:
                return word.lower()
        return None

    def extract_main_feeling(self, user_input):
        tokens = word_tokenize(user_input)
        tagged_tokens = pos_tag(tokens)
        feelings = {"happy", "sad", "anxious", "stressed", "excited", "lonely", "angry","demotivated", "glad", "motivation"}
        for word, pos in tagged_tokens:
            if word.lower() in feelings:
                return word.lower()
        return None

    def generate_solution(self, issue_or_feeling):
        solutions = {
            "anxiety": "Practice deep breathing exercises and consider mindfulness meditation to manage anxiety. You can also try talking to a therapist to develop coping strategies.",
            "depression": "Engage in activities you enjoy, exercise regularly, and maintain a healthy lifestyle. Consider seeking professional help from a therapist or psychiatrist.",
            "stress": "Identify stressors in your life and develop coping mechanisms such as time management and relaxation techniques. Don't hesitate to seek support from friends, family, or a counselor.",
            "loneliness": "Connect with friends and family, join social groups or clubs, and engage in activities that interest you. Volunteering and helping others can also combat feelings of loneliness.",
            "relationship": "Communication is key in resolving relationship issues. Express your feelings openly and listen to your partner's perspective. Consider couples therapy for professional guidance.",
            "happy": "It's great to hear that you're feeling happy! Remember to savor the moment and engage in activities that bring you joy.",
            "sad": "I'm sorry to hear that you're feeling sad. It's important to acknowledge your feelings and reach out for support if needed. You're not alone.",
            "anxious": "Feeling anxious can be challenging, but remember that it's okay to feel this way. Practice relaxation techniques and consider talking to a therapist for support.",
            "stressed": "Stress is a common experience, but it's important to manage it effectively. Make time for self-care activities and seek support from friends or a counselor.",
            "excited": "It's wonderful to hear that you're feeling excited! Make sure to channel that energy into positive activities and enjoy the moment.",
            "lonely": "Feeling lonely can be tough, but remember that you're not alone. Reach out to friends or family members, or consider joining social groups to connect with others.",
            "angry": "Feeling angry is natural, but it's important to manage it constructively. Take deep breaths and try to understand the source of your anger. Seeking support from a therapist can also be helpful.",
            "demotivated": "I understand feeling demotivated can be tough. Try breaking tasks into smaller, manageable steps and celebrate small achievements along the way.",
            "glad": "I'm glad to hear that you're feeling glad! Remember to appreciate the positive moments and take care of yourself.",
            "motivation": "Remember the childhood dreams you had? dont you think we need to accomplish that?"
        }
        return solutions.get(issue_or_feeling, "It's important to prioritize your mental health. Consider seeking professional help for personalized support.")

def main():
    chatbot = MentalHealthChatbot()
    print("Welcome to the Mental Health AI Chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
