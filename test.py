import os

def main():
    directory = os.getcwd()
    with open(f"{directory}/requests.txt", "w") as file:
        file.write("Saving Dream:Troy\nI was flying around the room!")
    with open(f"{directory}/requests.txt", "w") as file:
        file.write("Saving Dream:Test\nThis is a test dream.")
    with open(f"{directory}/requests.txt", 'w') as file:
        file.write("Requesting Dreams:Troy")
    with open(f"{directory}/response.txt", ) as file:
        response = file.read()
        print(response)
    with open(f"{directory}/requests.txt", 'w') as file:
        file.write("Requesting Dreams:ALL DREAMS")
    with open(f"{directory}/response.txt", 'r') as file:
        response = file.read()
        print(response)

if __name__ == "__main__":
    main()