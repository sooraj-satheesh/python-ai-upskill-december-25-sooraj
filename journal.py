from datetime import datetime

def get_journal_message():
    print("Write your journal message: How do you feel today? (happy/sad/neutral)")
    while True:
        msg=input()
        if msg=="" or not (msg=="happy" or msg=="sad" or msg=="neutral"):
            print("invalid answer, try again")
            continue
        else:
            return msg
def msg_to_mood(msg):
    match msg:
        case "happy":
            return "`:)"
        case "sad":
            return ":("
        case "neutral":
            return "`:"

if __name__=='__main__':
    print("Welcome to the Secret Journal\nEnter your name")
    name=input()
    entries=[]
    while True:

        print(
        """What would you like  to  do?
        1. Write a new journal entry 
        2. View saved entries 
        3. Exit 
        Enter your choice:""")
        choice=int(input())

        match choice:
            case 1:
                msg=get_journal_message()
                mood=msg_to_mood(msg)
                entry={
                        "id": len(entries)+1,
                        "message": msg,
                        "mood": mood,
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
                    }
                print(entry)
                entries.append(entry)
            case 3:
                exit()



