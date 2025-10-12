# Dummy_HMS
Dummy Hospital Management System

Pointers to track your project for MAD1 - Hospital Management System - Version_1

Task to mentees --> 2nd Oct 2025

1. Create a "templates folder" --> inside this only all the HTML pages will be made and saved.
2. Home page of your application --> home.html --> will be your landing page of the application.
3. Patient Registration HTML page is made with the help of HTML forms tag.
4. User (Admin, Doctor and Patient) Login HTML page is made with the help of HTML forms tag.
5. Flask app initialization is done in the file --> app.py.
6. 1st route --> initial route --> for rendering your home page is done.
7. Models for 5 tables especially - Doctor, Patient, Appointment, Treatment, Department --> is completed --> models.py file.
8. Database Initialization is done in the file --> app.py
9. When you run the python file (app.py), your database is getting created with name "your_db_name.db" --> with all the tables created in models.py.
10. Please install SQLite Viewer in your VSCode extensions to see your database clearly.
 

Task to mentees --> 4th Oct 2025

11. Establishing the relationship between the tables created inside models.py file.
12. Once done, and database is getting created, commit your changes.
13. Setting up or predefining the code for admin credentials in app.py file.
14. Once done commit this change as well.
15. Create a base.html page --> containing the rules of flashing the message for success and danger.
16. Template inheritance is done in registration.html and login.html file from base.html file, using jinja2.
17. Create a route for Patient Registration HTML page --> to render the HTML page.
18. Create a route for Login of 3 users --> Admin, Doctor and Patient --> to render the HTML page.
19. Create a basic HTML page for --> Admin Dashboard.
20. Create a basic HTML page for --> Doctor Dashboard.
21. Create a basic HTML page for --> Patient Dashboard.
22. Create a route for Admin Dashboard HTML page --> to render the HTML page.
23. Create a route for Doctor Dashboard HTML page --> to render the HTML page.
24. Create a route for Patient Dashboard HTML page --> to render the HTML page.
25. Once done, commit the changes of registration and login, with dashboard routes and HTML pages.
26. After cross reviewing your task with me, then only you will push your codes on github repository.


Task to mentees --> 7th Oct 2025

27. Create a HTML Page for --> creating department --> done by admin.
28. Create a route for creating department HTML page --> to render the HTML page.
29. Create a button on admin dashboard --> to redirect to create department page.
30. Table creation showing the list of all the present departments --> with edit and delete button --> on admin dashboard.
31. Using jinja2, all the details of departments are shown on admin dashboard inside the table.
32. Create a HTML page --> for editing the department --> done by  admin.
33. Create a route for editing the department HTML page --> to render the HTML page.
34. Create a route for deleting the department --> done by  admin.
35. Once done, commit all the changes done till now.
36. After cross reviewing your task with me, then only you will push your codes on github repository.
37. Create a HTML page --> for creating doctors profile --> done by  admin.
38. Create a route for creating doctors profile HTML page --> to render the HTML page.
39. Create a button on admin dashboard --> to redirect to create doctor profile page.
40. Table creation showing the list of all the present doctors --> with edit, blacklist and delete button --> on admin dashboard.
41. Using jinja2, all the details of doctors are shown on admin dashboard inside the table.
42. Table creation showing the list of all the present patients --> with edit, blacklist and delete button --> on admin dashboard.
43. Using jinja2, all the details of patients are shown on admin dashboard inside the table.
44. Create a HTML page --> for editing the doctor profile --> done by  admin.
45. Create a route for editing the doctor profile HTML page --> to render the HTML page.
46. Create a HTML page --> for editing the patient profile --> done by  admin.
47. Create a route for editing the patient profile HTML page --> to render the HTML page.
48. Create a route for deleting the doctor profile --> done by  admin.
49. Create a route for deleting the patient profile --> done by  admin.
50. Create a route for blacklisting the doctor profile --> done by  admin.
51. Create a route for blacklisting the patient profile --> done by  admin.
52. Once done, commit all the changes done till now.
53. After cross reviewing your task with me, then only you will push your codes on github repository.
54. Create a Search bar on admin dashboard --> to search the doctor and patient by name.
55. Create a route for searching the doctor and patient by name --> to render the HTML page with searched details.
56. Once done, commit all the changes done till now.
57. After cross reviewing your task with me, then only you will push your codes on github repository.

Task to mentees --> 11th Oct 2025

58. Search functionality is done using SQLAlchemy filter function --> search route made, done by admin, to search doctors and patients by name.
59. Search route mentioned inside admin_dashboard.html page as well.
60. Show all the departments created by admin --> inside Patient dashboard using jinja2 --> with button to view doctors inside that department.
61. Each department should have a button --> to view all the doctors present in that department --> inside Patient dashboard.
62. Create a route --> to show all the doctors present in that department --> inside Patient dashboard.
63. Give the route link inside patient_dashboard.html page as well.
64. Search bar on Patient dashboard --> to search the doctor by name.
65. Create a route for searching the doctor by name --> shown on patient dashboard..
66. Doctor table should have a column of "Available" --> to show the availability status of the doctor --> inside models.py file as well.
67. Create a route --> to update the availability status of the doctor --> done by doctor himself.
68. Create a button on doctor dashboard --> to redirect to update availability status page.
69. Create a HTML page --> for updating the availability status of the doctor --> done by doctor himself.
70. Once done, commit all the changes done till now.
71. Patient Dashboard --> when a particular department view details button clicked --> show all doctors inside that department using jinja2.
72. On patient dashboard --> when list of doctor of particular department is shown --> create a button to show availability of that doctor.
73. Create a route --> to show availability of that doctor --> on patient dashboard.
74. Create a HTML page --> to show availability of that doctor --> on patient dashboard.
75. Once done, commit all the changes done till now.
76. when checking each doctors availability --> show all the mentioned available dates of that doctor --> give a select option, which patient can select any one date from the available dates --> and give a button book appointment to confirm and save that booking into appointment table.
77. Create a route --> to book the appointment of that doctor on selected date --> on patient dashboard.
78. once appointment is booked, show that appointment details on patient dashboard as well.
79. Create a HTML page --> to show all the appointments booked by that patient --> on patient dashboard.
80. Create a button on patient dashboard --> to cancel the booked appointement.
81. Create a route --> to cancel the booked appointement --> on patient dashboard.
82. Once done, commit all the changes done till now.
83. show that booked appointment to that particular doctor --> on doctor dashboard in a table format with 2 button, completed and cancel.
84. Create a route --> to mark that appointment as completed --> on doctor dashboard.
85. Create a route --> to cancel that appointment --> on doctor dashboard.
86. Once done, commit all the changes done till now.
87. show all the appointments table data on the admin dashboard as well.
88. give a check route that whatever date of doctor is booked is not shown again in the availability of that doctor to other patients.
89. Once done, commit all the changes done till now.
90. On admin dashboard --> show total number of doctors, patients and appointments using SQLAlchemy count function.
91. After cross reviewing your task with me, then only you will push your codes on github repository.