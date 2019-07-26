# --- Define your functions below! ---


# --- Put your main program below! ---
def main():
  while True:
    answer = input("Hey whats your name? ")
    print("Hello " + answer + " nice meeting you my name is Johana Verdin. I am a senior at El Cerrito High School!")
    schoolandgrade()
    
def schoolandgrade():
    schoolanswer= input("But what school do you attend? ")
    if schoolanswer == "none":
        whynoschool=input("Why dont you go to school? ")
        print("Dang")
        bye()
        exit()
    else:
        niceschool= input("Is "+schoolanswer+" a nice school?(Yes,No) ")
        if niceschool == "yes":
            print("Never been there maybe I should stop by sometime")
            poetry()
        else:
            print("If you dont like it I prob dont either but thats fine. Wish you could come to my school, you prob would like it. We have a particular poetry class.")
            poetry()

def poetry():
    like=input("Do you like poetry?(Yes,No) ")
    if like=="yes":
        recite= input("uhh tell me a short poem.  ")
        print("Nice poem I like it")
        bye()
        exit()
    else:
        if favsubject():
            print("Thats one of my favorite subject too")
            bye()
            exit()
        else:
            print("Nice well one of mines is math.")
            bye()
            exit()
def favsubject():
    fav= input("Whats your favorite subject?  ").lower()
    favorite=["math", "science"]
    if fav in favorite:
        return True
    else:
        return False

            
            
def bye():
    print("Well I have to go, BYE. Nice meeting you.")
    
# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
