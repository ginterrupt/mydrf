Snippet Sharing API
ეს არის ვებ-პროექტი, რომელიც შექმნილია კოდის ფრაგმენტების (სნიპეტების) შესანახად და გასაზიარებლად. პროექტი საშუალებას აძლევს მომხმარებლებს მართონ საკუთარი კოდის ბიბლიოთეკა, დაალაგონ ის ენების მიხედვით და გააზიარონ სხვებთან.

როგორ მუშაობს
მომხმარებლის სივრცე: რეგისტრირებულ მომხმარებლებს შეუძლიათ დაამატონ, შეცვალონ ან წაშალონ მხოლოდ საკუთარი სნიპეტები.

API სტრუქტურა: პროექტი აგებულია Django REST Framework-ზე, რაც მონაცემების სწრაფ და მოწესრიგებულ გაცვლას უზრუნველყოფს.

მონაცემთა ბაზა: პროექტი იყენებს PostgreSQL-ს (Neon), რაც უზრუნველყოფს მონაცემთა უსაფრთხოებასა და საიმედოობას.

განთავსება: აპლიკაცია მუშაობს ღრუბლოვან სერვერზე (Render), რაც მას ხელმისაწვდომს ხდის ნებისმიერი ადგილიდან.

ძირითადი შესაძლებლობები
CRUD ოპერაციები: სნიპეტების შექმნა, წაკითხვა, განახლება და წაშლა.

წვდომის კონტროლი: უსაფრთხოების სისტემა, რომელიც იცავს მონაცემებს არასანქცირებული წაშლისგან ან რედაქტირებისგან.

მრავალენოვნება: მხარდაჭერა სხვადასხვა პროგრამირების ენების (Python, JavaScript, HTML, CSS და ა.შ.).

ტექნოლოგიური Stack
Framework: Django + DRF (Django REST Framework)

Database: PostgreSQL (Neon)

Server: Gunicorn (WSGI)

Platform: Render


########################

Snippet Sharing API
A web-based project designed to store, manage, and share code snippets efficiently. It provides a structured environment for developers to maintain a personal library of code fragments, organize them by programming language, and ensure secure access.

How It Works
User Workspace: Registered users can create, update, and delete their own code snippets.

API Architecture: Built on Django REST Framework, ensuring fast and standardized data exchange.

Database Management: Uses PostgreSQL (via Neon) to ensure data reliability and scalability.

Deployment: Hosted on Render, making the service accessible globally from the cloud.

Key Features
Full CRUD Operations: Seamless creation, reading, updating, and deletion of snippets.

Access Control: Integrated permission system ensuring that only the author can modify or delete their snippets.

Language Support: Designed to handle various programming languages (Python, JavaScript, HTML, CSS, etc.).

Technology Stack
Framework: Django + Django REST Framework (DRF)

Database: PostgreSQL (Neon Serverless)

Server: Gunicorn (WSGI)

Platform: Render (Cloud Hosting)
