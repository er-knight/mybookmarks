def bookman(url: str):
    """ bookman means bookmarks manager. """

    with open("bookmarks.txt", "a") as bookmarks:
        bookmarks.write(f"{url}\n")
    
    print("bookmarks updated!")

if __name__ == "__main__":
    
    url = input("link : ")
    bookman(url)

# NOTE : git commit -a -m "." && git push origin main

