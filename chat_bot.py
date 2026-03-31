# lis5 including all the comon places
list_of_all_location=["bedroom","kitchen", "hall", "bag","table", "sofa","car", "office"]
# Memory which will be used to learn from past answers
memory_data={}
# ourhelper functiions
def intro():
    print("\n Hey! I will help you find your lost item ")
    print("(Type 'Exit' anytime to sto p)\n")
def clean_input(text):
    return text.strip().lower()
def ask(question):
    return clean_input(input(question+" "))
# Core logic of our chat bot
def calculate_location_scores(last,usual, time, activity,confidence):
    scores = [] # making a empty list to save our score
    for place in list_of_all_location:
        score = 0
        # last used place
        if place == last:
            score += 6
        # usual place
        if place == usual:
            score += 4
        # guesses based on time
        if time == "night" and place == "bedroom":
            score += 3
        if time == "morning" and place == "kitchen":
            score += 3
        if time == "afternoon" and place == "table":
            score += 3
        # guesses based on activity
        if activity == "study" and place == "table":
            score += 3
        if activity == "cooking" and place == "kitchen":
            score += 3
        if activity == "rest" and place == "sofa":
            score += 3
        if activity == "travel" and place == "car":
            score +=3
        if activity == "work" and place == "office":
            score += 3
        # confidence adjustment
        if confidence == "high ":
            score += 2
        elif confidence == " low":
            score -= 1
        # learning from past
        if place in memory_data:
            score += memory_data[place]
        scores.append(score)
    return scores
# Finding best place
def get_best_place(scores):
    best_place = list_of_all_location[0]
    best_score = scores[0]
    for i in range(len(scores)):
        if scores[i] > best_score:
            best_score = scores[i]
            best_place = list_of_all_location[i]
    return best_place, best_score
# Shows result nicely
def show_answer(place, score):
    print("\n I think your item is most likely in:", place.upper())
    if score >= 10:
        print("Confidence : High ")
    elif score >= 6:
        print("Confidence: Medium ")
    else:
        print("Confidence: Low ")
    print("Tip: Check carefully around the", place)
# Learning from feedback
def learn(place, result):
    if result == "yes":
        print("Nice! I'll remember that for next time ")
        if place in memory_data:
            memory_data[place] += 1
        else:
            memory_data [place] = 1
    else:
        print("Okay, I will try better next time ")
        if place in memory_data:
            memory_data[place] -= 1
# Debuging
def show_debug(scores):
    print("\n(Just for understanding)")
    for i in range(len(list_of_all_location )):
        print(list_of_all_location[i], "->", scores[i])
# Main chatbot loop
def run_chatbot():
    intro()
    while True:
        item = clean_input(input("What did you lose? "))
        if item == "exit" :
            print("Bye! Hope you find everything ")
            break
        print("Okay, let's find your", item )
        print("\nSome quick questions.. .")
        last = ask("Where did you last use it?")
        usual = ask("Where do you usually keep it?")
        time = ask("When did you last use it? (morning/afternoon/night)")
        activity = ask("What were you doing? (study/cooking/rest/travel/work)")
        confidence = ask("How sure are you? (low/medium/high)")
        print("\nThinking...")
        scores = calculate_location_scores(last,usual,time,activity,confidence)
        show_debug(scores)
        best_place, best_score = get_best_place(scores)
        show_answer( best_place, best_score )
        feedback = ask("Did you find it there? (yes/no)")
        learn(best_place, feedback)
        print("\n Memory so far : ", memory_data )
        print ("\n-----------------------------")
# Start program
if __name__ == "__main__" :
          run_chatbot()