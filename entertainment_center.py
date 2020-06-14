"""Stores details of movies and displays them on a website."""
import notice
import media

def main():
    
    n1 = media.Movie("TCS Ion Online Workshop",
                          "TCS ION's Industry Honour Certification(IHC) - Your bridge to industry readiness.",
                          "https://pbs.twimg.com/profile_images/912616865574219776/s0G4kIoM_400x400.jpg",
                          '''https://g01.tcsion.com/FeedbackSolution/openPublishURL.do?publishKey=Zov9nXtMsRmK3coanS6nxA%3D%3D&integrationLinkRespondentDetail=%7B%22username%22:%22Anonymous%22,%22useremailId%22:%22Anonymous@tcs.com%22%7D&respondentAttribute=%7B%7D''',
                          "June 10, 2020")

    n2 = media.Movie("Quiz on Java Programming",
                          '''Department of Information Technology is organizing an online Technical Quiz on 'Basics of Java Programming' to test the skills of students and faculty.''',
                          "https://i.pinimg.com/originals/51/1d/36/511d363cea877348b65ecde493e6063a.png",
                          "https://forms.gle/rBrYBk6atUENcgfdA",
                          "June 12, 2020")

    n3 = media.Movie("TCS Ion Online Workshop",
                          "TCS ION's Industry Honour Certification(IHC) - Your bridge to industry readiness.",
                          "https://pbs.twimg.com/profile_images/912616865574219776/s0G4kIoM_400x400.jpg",
                          '''https://g01.tcsion.com/FeedbackSolution/openPublishURL.do?publishKey=Zov9nXtMsRmK3coanS6nxA%3D%3D&integrationLinkRespondentDetail=%7B%22username%22:%22Anonymous%22,%22useremailId%22:%22Anonymous@tcs.com%22%7D&respondentAttribute=%7B%7D''',
                          "June 10, 2020")

    n4 = media.Movie("Quiz on Java Programming",
                          '''Department of Information Technology is organizing an online Technical Quiz on 'Basics of Java Programming' to test the skills of students and faculty.''',
                          "https://i.pinimg.com/originals/51/1d/36/511d363cea877348b65ecde493e6063a.png",
                          "https://forms.gle/rBrYBk6atUENcgfdA",
                          "June 12, 2020")

    n5 = media.Movie("TCS Ion Online Workshop",
                          "TCS ION's Industry Honour Certification(IHC) - Your bridge to industry readiness.",
                          "https://pbs.twimg.com/profile_images/912616865574219776/s0G4kIoM_400x400.jpg",
                          '''https://g01.tcsion.com/FeedbackSolution/openPublishURL.do?publishKey=Zov9nXtMsRmK3coanS6nxA%3D%3D&integrationLinkRespondentDetail=%7B%22username%22:%22Anonymous%22,%22useremailId%22:%22Anonymous@tcs.com%22%7D&respondentAttribute=%7B%7D''',
                          "June 10, 2020")

    n6 = media.Movie("Quiz on Java Programming",
                          '''Department of Information Technology is organizing an online Technical Quiz on 'Basics of Java Programming' to test the skills of students and faculty.''',
                          "https://i.pinimg.com/originals/51/1d/36/511d363cea877348b65ecde493e6063a.png",
                          "https://forms.gle/rBrYBk6atUENcgfdA",
                          "June 12, 2020")

    n7 = media.Movie("TCS Ion Online Workshop",
                          "TCS ION's Industry Honour Certification(IHC) - Your bridge to industry readiness.",
                          "https://pbs.twimg.com/profile_images/912616865574219776/s0G4kIoM_400x400.jpg",
                          '''https://g01.tcsion.com/FeedbackSolution/openPublishURL.do?publishKey=Zov9nXtMsRmK3coanS6nxA%3D%3D&integrationLinkRespondentDetail=%7B%22username%22:%22Anonymous%22,%22useremailId%22:%22Anonymous@tcs.com%22%7D&respondentAttribute=%7B%7D''',
                          "June 10, 2020")

    n8 = media.Movie("Quiz on Java Programming",
                          '''Department of Information Technology is organizing an online Technical Quiz on 'Basics of Java Programming' to test the skills of students and faculty.''',
                          "https://i.pinimg.com/originals/51/1d/36/511d363cea877348b65ecde493e6063a.png",
                          "https://forms.gle/rBrYBk6atUENcgfdA",
                          "June 12, 2020")
    # Store the Movie objects in a list.
    movies = [n1, n2, n3, n4, n5, n6, n7, n8]

    # Open the movie website in the user's browser, featuring the movies above.
    notice.open_movies_page(movies)

if __name__ == '__main__':
    main()
