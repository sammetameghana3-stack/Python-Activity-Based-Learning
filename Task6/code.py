
# Hackathon Team Formation and Ranking System

MIN_TEAM_SIZE = 2
MAX_TEAM_SIZE = 4
NUMBER_OF_ROUNDS = 3
MAX_SCORE = 100


def validate_team_size(size):
    """Validate the number of team members."""
    return MIN_TEAM_SIZE <= size <= MAX_TEAM_SIZE


def calculate_scores(round_scores):
    """Calculate total and average scores."""
    total = sum(round_scores)
    average = total / NUMBER_OF_ROUNDS

    return total, average


def rank_teams(teams):
    """
    Rank teams using predefined tie-breaking rules.

    1. Higher total score
    2. Higher Round 3 score
    3. Higher Round 2 score
    4. Alphabetical team name
    """

    teams.sort(
        key=lambda team: (
            -team["total"],
            -team["scores"][2],
            -team["scores"][1],
            team["name"].casefold()
        )
    )

    for rank, team in enumerate(teams, start=1):
        team["rank"] = rank

    return teams


def main():

    print("===== HACKATHON TEAM FORMATION AND RANKING =====")

    try:
        number_of_teams = int(input("Enter number of teams: "))

        if number_of_teams <= 0:
            print("Number of teams must be positive.")
            return

        teams = []
        registered_students = set()
        registered_teams = set()

        # Collect team information
        for i in range(number_of_teams):

            print(f"\nEnter details for Team {i + 1}")

            team_name = input("Enter team name: ").strip()

            if not team_name:
                print("Team name cannot be empty.")
                return

            if team_name.casefold() in registered_teams:
                print("Duplicate team name is not allowed.")
                return

            registered_teams.add(team_name.casefold())

            size = int(input("Enter number of team members: "))

            if not validate_team_size(size):
                print("Invalid team size!")
                print("Team must contain 2 to 4 members.")
                return

            members = []

            # Collect member names
            for j in range(size):

                member = input(
                    f"Enter member {j + 1} name: "
                ).strip()

                if not member:
                    print("Member name cannot be empty.")
                    return

                member_key = member.casefold()

                if member_key in registered_students:
                    print("Student already belongs to another team!")
                    return

                registered_students.add(member_key)
                members.append(member)

            # Collect round-wise scores
            round_scores = []

            print("\nEnter round-wise scores (0-100):")

            for r in range(NUMBER_OF_ROUNDS):

                score = float(
                    input(f"Round {r + 1} score: ")
                )

                if not 0 <= score <= MAX_SCORE:
                    print("Invalid score! Score must be 0-100.")
                    return

                round_scores.append(score)

            # Calculate total and average
            total, average = calculate_scores(round_scores)

            team = {
                "name": team_name,
                "members": members,
                "scores": round_scores,
                "total": total,
                "average": average
            }

            teams.append(team)

        # Rank all teams
        ranked_teams = rank_teams(teams)

        # Display team details
        print("\n===== TEAM PERFORMANCE DETAILS =====")

        for team in ranked_teams:

            print(f"\nTeam Name : {team['name']}")
            print("Members   : " + ", ".join(team["members"]))
            print(f"Round 1   : {team['scores'][0]:.2f}")
            print(f"Round 2   : {team['scores'][1]:.2f}")
            print(f"Round 3   : {team['scores'][2]:.2f}")
            print(f"Total     : {team['total']:.2f}")
            print(f"Average   : {team['average']:.2f}")

        # Display final rankings
        print("\n===== FINAL HACKATHON RANKINGS =====")

        print("Rank\tTeam Name\tTotal\tAverage")

        for team in ranked_teams:

            print(
                f"{team['rank']}\t"
                f"{team['name']}\t\t"
                f"{team['total']:.2f}\t"
                f"{team['average']:.2f}"
            )

        print("\nWinner:", ranked_teams[0]["name"])

        print("\n===== RANKING COMPLETED SUCCESSFULLY =====")

    except ValueError:
        print("Invalid input! Enter valid numeric values.")


if __name__ == "__main__":
    main()

