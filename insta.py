import instaloader

def scrape_instagram():
    L = instaloader.Instaloader()

    # Prompt user for Instagram username
    username = input("Enter an Instagram username: ")

    # Fetch profile metadata
    profile = instaloader.Profile.from_username(L.context, username)

    # Display profile metadata
    print("Username:", profile.username)
    print("Followers:", profile.followers)
    print("Following:", profile.followees)
    print("Posts:", profile.mediacount)
    print("Private:", profile.is_private)
    print("Verified:", profile.is_verified)
    print("Bio:", profile.biography)

    if profile.external_url:
        print("External URL:", profile.external_url)

        # Fetch and display past usernames
        past_usernames = profile.get_username_history()
        if past_usernames:
            print("Past Usernames:", ", ".join(past_usernames))


def main():
    # Prompt user to select an option
    option = input("Select an option:\n1. Scrape Instagram data\n2. Exit\n")

    # Process user's choice
    if option == "1":
        scrape_instagram()
    elif option == "2":
        print("Exiting program...")
    else:
        print("Invalid option. Please try again.")
        main()


if __name__ == "__main__":
    main()
