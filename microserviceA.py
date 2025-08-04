import os

def main():
    directory = os.getcwd()
    run_state = None
    while run_state is None:
        with open(f"{directory}/requests.txt", 'r') as file:
            request = file.readlines()
            if request == []:
                continue
            if request[0][:13] == "Saving Dream:":
                run_state = "Save"
            if request[0][:18] == "Requesting Dreams:":
                run_state = "Request"
    
    if run_state == "Save":
        user = request[0][13:(len(request[0])-1)]
        with open(f"{directory}/dreams.txt", 'a') as file:
            file.write(f"\n{user}: {request[1]}")
            print(f"New dream saved under {user}")
        with open(f"{directory}/requests.txt", 'w') as clear:
            clear.write("")
        main()
    
    elif run_state == "Request":
        user = request[0][18:]
        with open(f"{directory}/dreams.txt", 'r') as file:
            dream_list = file.readlines()
        if user == "ALL DREAMS":
            with open(f"{directory}/response.txt", 'w') as file:
                for dream in dream_list:
                    file.write(dream)
        else:
            with open(f"{directory}/response.txt", 'w') as file:
                for dream in dream_list:
                    name_index = dream.find(":")
                    if user == dream[:name_index]:
                        file.write(dream)
        with open(f"{directory}/requests.txt", 'w') as clear:
            clear.write("")
        main()
        

if __name__ == "__main__":
    main()