# Movie/shows data stored in a dictionary 
movies = {
    "action": [
        {"title": "John Wick", "year": 2014, "cast": "Keanu Reeves, Michael Nyqvist", "summary": "A retired hitman seeks vengeance after gangsters kill his dog."},
        {"title": "Mad Max: Fury Road", "year": 2015, "cast": "Tom Hardy, Charlize Theron", "summary": "A woman rebels against a tyrant in a post-apocalyptic desert."},
        {"title": "Mission Impossible: Fallout", "year": 2018, "cast": "Tom Cruise, Henry Cavill", "summary": "Ethan Hunt and his team race against time to stop a global catastrophe."},
        {"title": "Pacific Rim", "year": 2013, "cast": "Charlie Hunnam, Idris Elba", "summary": "Humans pilot giant robots to fight monstrous sea creatures."},
        {"title": "Kingsman: The Secret Service", "year": 2014, "cast": "Taron Egerton, Colin Firth", "summary": "A street kid is recruited by a secret spy organization."}
    ],
    "adventure": [
        {"title": "Jurassic Park", "year": 1993, "cast": "Sam Neill, Laura Dern", "summary": "Scientists visit a theme park with cloned dinosaurs that escape."},
        {"title": "Indiana Jones and the Raiders of the Lost Ark", "year": 1981, "cast": "Harrison Ford, Karen Allen", "summary": "An archaeologist races against Nazis to find the Ark of the Covenant."},
        {"title": "The Lord of the Rings: The Fellowship of the Ring", "year": 2001, "cast": "Elijah Wood, Ian McKellen", "summary": "A young hobbit must destroy a powerful ring in Mount Doom."},
        {"title": "Jumanji: Welcome to the Jungle", "year": 2017, "cast": "Dwayne Johnson, Kevin Hart", "summary": "Teens are transported into a video game jungle world."},
        {"title": "Pirates of the Caribbean: The Curse of the Black Pearl", "year": 2003, "cast": "Johnny Depp, Orlando Bloom", "summary": "A pirate helps rescue a governor's daughter from cursed pirates."}
    ], 
    "comedy": [
        {"title": "The Mask", "year": 1994, "cast": "Jim Carrey, Peter Riegert", "summary": "A man finds a magical mask that transforms him into a trickster."},
        {"title": "Superbad", "year": 2007, "cast": "Jonah Hill, Michael Cera", "summary": "Two high school friends try to have one last wild night before graduation."},
        {"title": "Home Alone", "year": 1990, "cast": "Macaulay Culkin, Joe Pesci", "summary": "An 8-year-old boy must defend his home from burglars when he's accidentally left behind during Christmas vacation."},
        {"title": "Dumb and Dumber", "year": 1994, "cast": "Jim Carrey, Jeff Daniels", "summary": "Two dumb friends travel to return a briefcase to its owner."},
        {"title": "Mrs. Doubtfire", "year": 1993, "cast": "Robin Williams, Sally Field", "summary": "A divorced man disguises himself as a nanny to see his kids."}
    ],
    "drama": [
        {"title": "F1: The Movie", "year": 2025, "cast": "Brad Pitt, Damson Idris", "summary": "A dramatic story about the high-stakes world of Formula 1 racing."},
        {"title": "Se7en", "year": 1995, "cast": "Brad Pitt, Morgan Freeman", "summary": "Two detectives hunt a serial killer who uses the seven deadly sins as his crimes."},
        {"title": "Oppenheimer", "year": 2023, "cast": "Cillian Murphy, Emily Blunt", "summary": "The story of J. Robert Oppenheimer and the creation of the atomic bomb."},
        {"title": "Parasite", "year": 2019, "cast": "Song Kang-ho, Lee Sun-kyun", "summary": "A poor family infiltrates a wealthy household with unexpected consequences."},
        {"title": "The Godfather", "year": 1972, "cast": "Marlon Brando, Al Pacino", "summary": "The aging patriarch of an organized crime dynasty transfers control to his reluctant son."}
    ],    
    "horror": [
        {"title": "The Conjuring", "year": 2013, "cast": "Vera Farmiga, Patrick Wilson", "summary": "Paranormal investigators help a family terrorized by a dark presence."},
        {"title": "It", "year": 2017, "cast": "Bill Skarsgård, Jaeden Lieberher", "summary": "A group of kids face their worst fears when they confront a killer clown."},
        {"title": "The Ring", "year": 2002, "cast": "Naomi Watts, Shannon Cochran", "summary": "A journalist investigates a cursed videotape that kills viewers in 7 days."},
        {"title": "Train to Busan", "year": 2016, "cast": "Gong Yoo, Jung Yu-mi", "summary": "Passengers on a train must survive a zombie apocalypse."},
        {"title": "Midsommar", "year": 2019, "cast": "Florence Pugh, Jack Reynor", "summary": "A couple visits a Swedish festival that turns into a pagan nightmare."}
    ],
        "romance": [
        {"title": "Titanic", "year": 1997, "cast": "Leonardo DiCaprio, Kate Winslet", "summary": "A poor artist and a rich girl fall in love on the doomed Titanic."},
        {"title": "Crazy Rich Asians", "year": 2018, "cast": "Constance Wu, Henry Golding", "summary": "A woman discovers her boyfriend's family is extremely wealthy in Singapore."},
        {"title": "La La Land", "year": 2016, "cast": "Ryan Gosling, Emma Stone", "summary": "A jazz musician and an actress fall in love while pursuing their dreams."},
        {"title": "Pride & Prejudice", "year": 2005, "cast": "Keira Knightley, Matthew Macfadyen", "summary": "Elizabeth Bennet and Mr. Darcy overcome pride and prejudice for love."},
        {"title": "Beauty and the Beast", "year": 2017, "cast": "Emma Watson, Dan Stevens", "summary": "A young woman falls in love with a prince cursed to live as a beast."}
    ],
    "science fiction": [
        {"title": "Dune", "year": 2021, "cast": "Timothée Chalamet, Zendaya", "summary": "A noble family fights for control of the desert planet Arrakis."},
        {"title": "Tenet", "year": 2020, "cast": "John David Washington, Robert Pattinson", "summary": "A protagonist manipulates time to prevent World War III."},
        {"title": "The Matrix", "year": 1999, "cast": "Keanu Reeves, Laurence Fishburne", "summary": "A hacker discovers reality is a simulation and joins a rebellion."},
        {"title": "Edge of Tomorrow", "year": 2014, "cast": "Tom Cruise, Emily Blunt", "summary": "A soldier relives the same day to defeat an alien invasion."},
        {"title": "Star Wars: Episode IV - A New Hope", "year": 1977, "cast": "Mark Hamill, Harrison Ford", "summary": "A farm boy joins a rebellion to rescue a princess and destroy a weapon."}
    ]
}

print("🎬 Welcome to Movie Finder!")

while True:
    print("\nAvailable genres:", ", ".join([g.capitalize() for g in movies.keys()]))
    genre = input("Enter a genre or type 'exit' or 'q' to quit: ").lower()

    if genre in {"exit", "q"}:
        print("Thank you for using Movie Finder!")
        break

    if genre in movies:
        print(f"\nAvailable {genre.capitalize()} Movies:")
        for i, movie in enumerate(movies[genre], start=1):
            print(f"{i}. {movie['title']}")

        try:
            choice = int(input("\nEnter the number of the movie you want to know more about: "))
            if 1 <= choice <= len(movies[genre]):
                selected_movie = movies[genre][choice - 1]
                print(f"\n🎥 You selected: {selected_movie['title']}")
                print(f"Year: {selected_movie['year']}")
                print(f"Cast: {selected_movie['cast']}")
                print(f"Summary: {selected_movie['summary']}\n")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Sorry, that genre is not available.\n")

    exit_program = False
    while True:
        again = input("Do you want to look for another genre? (Y/N): ").strip().lower()
        if again == "y":
            break
        if again in {"n", "exit", "q"}:
            print("Thank you for using Movie Finder!")
            exit_program = True
            break
        print("Invalid choice. Please enter 'Y' or 'N'.")

    if exit_program:
        break
