def search_by_team(matches, team_name):
    result = [match for match in matches if team_name in (match[2], match[3])]
    return result

def search_by_location(matches, location):
    result = [match for match in matches if location == match[1]]
    return result

def search_by_timing(matches, timing):
    result = [match for match in matches if timing == match[4]]
    return result

def main():
    matches = [
        ("Mumbai", "India", "Sri Lanka", "DAY"),
        ("Delhi", "England", "Australia", "DAY-NIGHT"),
        ("Chennai", "India", "South Africa", "DAY"),
        ("Indore", "England", "Sri Lanka", "DAY-NIGHT"),
        ("Mohali", "Australia", "South Africa", "DAY-NIGHT"),
        ("Delhi", "India", "Australia", "DAY")
    ]

    while True:
        print("Search Options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            team_name = input("Enter the team name: ")
            result = search_by_team(matches, team_name)
            print("Matches involving", team_name)
            for match in result:
                print(match)
        elif choice == '2':
            location = input("Enter the location: ")
            result = search_by_location(matches, location)
            print("Matches in", location)
            for match in result:
                print(match)
        elif choice == '3':
            timing = input("Enter the timing: ")
            result = search_by_timing(matches, timing)
            print("Matches at", timing, "timing")
            for match in result:
                print(match)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
