# Movie Finder

Movie Finder is a simple command-line application that helps you discover new movies by genre. The script presents a curated list of films for each genre and provides details like release year, main cast, and a short summary when you make a selection.

## Requirements
- Python 3.8 or later (no additional packages are required)

## Getting Started
1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the script with Python:
   - **On macOS or Linux**
     ```bash
     python3 exit.py
     ```
   - **On Windows (PowerShell or Command Prompt)**
     ```powershell
     python exit.py
     ```

## Usage
1. After launching the script you will see a welcome message and a list of available genres.
2. Type the name of a genre (e.g., `action`, `comedy`) and press **Enter**.
3. The script will display a numbered list of movies in the chosen genre. Type the number of the movie you want more information about and press **Enter**.
4. The program will print the selected movie's year, cast, and a brief summary.
5. When prompted, choose whether you would like to look up another genre:
   - Enter `Y` to continue browsing.
   - Enter `N`, `exit`, or `q` to quit the program.

If you ever want to exit immediately, you can type `exit` or `q` at the genre prompt.

## Example Session
```
🎬 Welcome to Movie Finder!

Available genres: Action, Adventure, Comedy, Drama, Horror, Romance, Science fiction
Enter a genre or type 'exit' or 'q' to quit: comedy

Available Comedy Movies:
1. The Mask
2. Superbad
3. Home Alone
4. Dumb and Dumber
5. Mrs. Doubtfire

Enter the number of the movie you want to know more about: 3

🎥 You selected: Home Alone
Year: 1990
Cast: Macaulay Culkin, Joe Pesci
Summary: An 8-year-old boy must defend his home from burglars when he's accidentally left behind during Christmas vacation.

Do you want to look for another genre? (Y/N): n
Thank you for using Movie Finder!
```

Enjoy exploring new movies!
