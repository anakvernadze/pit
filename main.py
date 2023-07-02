#OOPPLAYLIST
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.albums = []
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"Title: {self.title}\nArtist: {self.artist}\nDuration: {self.duration} minutes"

class Playlist:
    def __init__(self, name, max_songs):
        self.name = name
        self.songs = []
        self.max_songs = max_songs

    def __str__(self):
        return f"Playlist Name: {self.name}\nNumber of Songs: {len(self.songs)}\nMax Songs: {self.max_songs}"

    def add_song(self, song):
        if len(self.songs) < self.max_songs:
            self.songs.append(song)
            song.albums.append(self)
            print(f"{song.title} added to {self.name} playlist.")
        else:
            print(f"Not enough space in {self.name} playlist.")

    def __add__(self, other):
        joined_playlist = Playlist(f"{self.name} + {other.name}", self.max_songs + other.max_songs)
        joined_playlist.songs = self.songs + other.songs
        return joined_playlist

# Example usage
song1 = Song("Song 1", "Artist 1", 3)
song2 = Song("Song 2", "Artist 2", 4)
song3 = Song("Song 3", "Artist 3", 5)
song4 = Song("Song 4", "Artist 4", 3)

playlist1 = Playlist("Playlist 1", 3)
playlist1.add_song(song1)
playlist1.add_song(song2)

playlist2 = Playlist("Playlist 2", 2)
playlist2.add_song(song3)
playlist2.add_song(song4)

print(playlist1)
print(playlist2)

joined_playlist = playlist1 + playlist2
print(joined_playlist)












#PARSERGOOGLE
import requests
from bs4 import BeautifulSoup
import os

# Read the HTML file
with open("sample.html") as file:
    html_content = file.read()

# Extract university names using Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")
university_list = []

# Find all the elements on the left side containing university names
university_elements = soup.select(".left-side .university")
for element in university_elements:
    university_list.append(element.text)

print("University Names:")
for university in university_list:
    print(university)

# Save the Google logo link
google_logo_link = soup.select_one("#google-logo").get("src")
print("Google Logo Link:", google_logo_link)

# Retrieve and save the image
response = requests.get(google_logo_link)
if response.status_code == 200:
    with open("google_logo.png", "wb") as image_file:
        image_file.write(response.content)
        print("Image saved successfully as google_logo.png.")
else:
    print("Failed to retrieve the image.")














#PARSERBTU
import requests
from bs4 import BeautifulSoup

# Read the HTML file
with open("sample.html") as file:
    html_content = file.read()

# Extract training programs using Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")
training_programs = []

# Find all elements containing training program information
program_elements = soup.select(".training-program")
for element in program_elements:
    training_programs.append(element.text)

print("Training Programs:")
for program in training_programs:
    print(program)

# Save the BTU logo link
btu_logo_link = soup.select_one("#btu-logo").get("src")
print("BTU Logo Link:", btu_logo_link)

# Retrieve and save the image
response = requests.get(btu_logo_link)
if response.status_code == 200:
    with open("btu_logo.png", "wb") as image_file:
        image_file.write(response.content)
        print("Image saved successfully as btu_logo.png.")
else:
    print("Failed to retrieve the image.")





რა განსხვავებაა GET და POST request-ებს შორის. მოიყვანეთ შესაბამისი მაგალითები.
ყველაზე ხშირად გამოყენებადი HTTP მეთოდებია: GET და POST
✲ GET გამოიყენება მაშინ, როდესაც request-ის გაგზავნა ხდება URL-ის მეშვეობით. შესაბამისად, URL-ში ეთითება
საჭირო პარამეტრები (პარამეტრის სახელი და მნიშნველობა). გამოიყენება ‘&’ სიმბოლო პარამეტრების
ერთმანეთისგან გამოსაყოფად და ‘?’ ძირითადი მისამართისა და პარამეტრების ერთმანეთისგან გამოსაყოფად
GET-ით შესაძლებელია ლიმიტირებული მონაცემების გაგზავნა სერვერზე, იგი რჩება ბრაუზერის history-ში,
გადაცემული ინფორმაცია ხილვადია ყველასთვის (არ გამოიყენება დაფარული ინფორმაციის გადასაცემად)
✲ POST გამოიყენება მონაცემების გასაგზავნად სერვერზე, რომლის შენახვა (ან განახლება) უნდა მოხდეს ბაზაში (ან სხვა
რესურში). POST მეთოდი გამოიყენება ფორმებში შეყვანილი ინფორმაციის სერვერზე გასაგზავნად.
✲ POST მეთოდის ელემენტები არ არის ხილვადი, არ ხდება მისი ქეშირება, არ რჩება ბრაუზერის history-ში, მისი
ელემენტების სიგრძე არ არის ლიმიტირებული.
POST მეთოდისას, ვინაიდან მონაცემების გადაცემა ხდება html ფორმის (<form> ტეგი) მეშვეობით, უმეტესად ფორმას აქვს submit
(დადასტურების) ღილაკი. ფორმის ელემენტებს კი აქვთ სახელები, რომლის მეშვეობითაც მოგვიანებით შესაძლებელია მათზე
წვდომა. დადასტურების ღილაკზე დაწკაპებისას ხდება POST request-ის გაგზავნა და შესაბამისად ფორმაში შეყვანილი
ელემენტებზე წვდომა პითონში შესაძლებელია ფორმის ელემენტების სახელების მეშვეობით, რომლებიც შენახულია form
ლექსიკონის სახით.



რას წარმოადგენს BeatifulSoup მოდულის find() ფუნქცია და რა ტიპის მონაცემს აბრუნებს? მოიყვანეთ მაგალითი.
პარსინგის დროს საჭიროა soup ტექსტში (რომელშიც მოთავსებულია html კოდი) მოვძებნოთ
ჩვენთვის საჭირო ნაწილი (ტეგი) და მასში არსებული ინფორმაცია. ამისათვის გამოიყენება
ძებნის ფუნქციები: find(), find_all() და სხვა.
✲ find() ფუნქცია აბრუნებს მხოლოდ ერთ მნიშვნელობას, პირველივე შემხვედრს

რას წარმოადგენს BeatifulSoup მოდულის find_all() ფუნქცია და რა ტიპის მონაცემს აბრუნებს? მოიყვანეთ მაგალითი.
პარსინგის დროს საჭიროა soup ტექსტში (რომელშიც მოთავსებულია html კოდი) მოვძებნოთ
ჩვენთვის საჭირო ნაწილი (ტეგი) და მასში არსებული ინფორმაცია. ამისათვის გამოიყენება
ძებნის ფუნქციები: find(), find_all() და სხვა.
find_all() ფუნქცია აბრუნებს პარამეტრად მითითებული ტეგების შიგთავს; თუ ეს ტეგი
რამდენიმეჯერ არის ნახსენები, აბრუნებს ყველას სიის სახით


Flask-ის მოდულის გამოყენებით ვებ აპლიკაციაში როგორ არის შესაძლებელი მოხდეს გვერდის სხვა გვერდზე გადამისამართება. მოიყვანეთ მაგალითი.
url_for() ფუნქცია უზრუნველყოფს ლინკის დაგენერირებას. პარამეტრად გადაეცემა სტრიქონი,
რომელიც წარმოადგენს იმ ფუნქციის დასახელებას, რომლის შესაბამისი ლინკის აგებაც გვსურს.
ფუნქციას შესაძლოა გადაეცეს სხვა პარამეტრებიც, იმ შემთხვევაში თუ პირველ პარამეტრად
მითითენულ ფუნქცია არის პარამეტრიანი ფუნქცია, ყველა მისი პარამეტრი შეგვიძლია გადავცეთ
url_for()-ში მომდევნო პარამეტრებად (მაგალითი განხილულია მომდევნო სლაიდებზე).
✲ redirect() ფუნქცია უზრუნველყოფს პარამეტრად გადაცემულ ლინკზე გადასვლას
(გადამისამართებას).



Flask-ის მოდულის გამოყენებით ვებ აპლიკაციაში როგორ არის შესაძლებელი მოხდეს კონკრეტულ route-ზე html ფაილის მიბმა. აღწერეთ დეტალურად.
საიტის რომელიმე გვერდზე html ფაილის მიბმა ხორციელდება
render_template() ფუნქციის გამოყენებით. პირველ პარამეტრად
ეთითება ფაილის სახელი, რომელიც მოთავსებული უნდა იყოს
templates საქაღალდეში.
✲ თუ html ფაილში გვსურს გამოვიყენოთ პიტონის ფაილიდან
რომელიმე ცვლადი, მათი გადაცემა ხორციელდება
render_template() ფუნქციაში მომდევნო პარამეტრებად. მაგ. user()
ფუნქციაში ხდება user.html ფაილის მიბმა და პარამეტრად
გადაეცემა name ცვლადის მნიშვნელობა, რომლის გამოყენება html
ფაილში ხდება my_name-ით (პარამეტრის სახელით)



რას წარმოადგენს csv მოდული? მოიყვანეთ რომელიმე ფუნქცია შესაბამისი მაგალითით.
Python-ში csv მოდულის გამოყენებით შესაძლებელია csv ფაილიდან მონაცემთა იმპორტი/წაკითხვა (Read) და/ან მონაცემების ექსპორტი/ჩაწერა (Write) csv ფაილში. csv (Comma Separated Values) ფაილი გამოიყენება დიდი რაოდენობის მონაცემების შესანახად ტექსტურ ფორმატში. CSV ფაილის გავს excel-ის ფაილს, სადაც მონაცემები წარმოდგენილია ცხრილის სახით (სტრიქონების და სვეტების მეშვეობით). csv ფაილში ცხრილის მონაცემები წარმოდგენილია ტექსტურად, რომლის თითოეული ხაზზე არის ცხრილის თითო სტრიქონის მონაცემი, ხოლო მძიმე გამოიყენება უჯრების (სვეტების) ერთმანეთისგან გამოსაყოფად.
csv.writer() - აბრუნებს writer-ის ობიექტს, რომელზეც writerow() მეთოდის გამოყენებით შესაძლებელია csv ფაილში ცალკეული სტრიქონების (row)-ის ჩაწერა


რას ნიშნავს საიტის Deployment? მოიყვანეთ შესაბამისი მაგალითი და აღწერეთ პროცესი.
ვებ აპლიკაციის შექმნის საბოლოო ეტაპი არის მისი ატვირთვა სერვერზე და ოფიციალური გაშვება.
ამისათვის საჭიროა გქონდეთ ჰოსტინგი და დომენი. ჰოსტინგის პროვაიდერები თავად აძლევენ
ინსტრუქციას თუ როგორ უნდა მოხდეს საიტის ფაილების ატვირთვა სერვერზე.
✲ არსებობს cloud პლატფორმები, რომლებიც სთავაზობენ სერვერულ მხარდაჭერას. მაგ.
https://www.pythonanywhere.com/



რა არის პარსინგის უარყოფითი მხარე?
Variety (განსხვავებულობა) - ყველა ვებ გვერდს ჭირდება ინდივიდუალური
პარსინგის კოდის დაწერა, ვინადან ყველა ვებ გვერდს აქვს განსხვავებული html
კოდი.
✲ Durability (მდგრადობა) - საიტის html კოდის ცვლილების შემთხვევაში, არსებულ პარსინგის
კოდშიც საწირო გახდება ცვლილებების განხორციელება



აღწერეთ როგორ არის შესაძლებელი html ფაილში პითონის ცვლადების და ფუნქციონალის ინტეგრირება?
BeatifulSoup კლასის გამოყენებით უნდა შეიქმნას ობიექტი, რომლის საშუალებითაც
დავამუშავებთ html კოდს




რა მსგავსება და განსხვავებაა პარსინგსა და API-ის შორის
Web Scraping/Parsing გამოიყენება ვებ გვერდებიდან დიდი ინფორმაციის წამოსაღებად და
წასაკითხად ავტომატურ რეჟიმში. Scraping ნიშნავს ინფორმაციის წამოღებას, ხოლოდ parsing
ნიშნავს წამოღებული ინფორმაციის დაყოფას ნაწილებად და საჭირო კონტენტზე წვდომას
ვებ გვერდზე განთავსებული ინფორმაცია არ არის სტრუქტურირებული. იმ შემთხვევაში, თუ
გვინდა ინფორმაცია წამოვიღოთ სტრუქტურირებული სახით, მაშინ ვიყენებთ ვებ სერვისებს,
API-ს.




რას წარმოადგენს 200 Status Code?
http სტატუს კოდია და ნიშნავს წარმატებით შესრულებას