# Birthday Wisher
A birthday wisher that uses SMTP, datetime, and pandas to automatically send customized birthday emails to friends and family.

## Feature Tasks
1. Update the `birthdays.csv` with your friends & family's details.
1. Check if today matches a birthday in the birthdays.csv
1. If there is a match, pick a random letter (`letter_1.txt`/`letter_2.txt`/`letter_3.txt`) from `letter_templates` and replace the [NAME] with the person's actual name from `birthdays.csv`.
1. Send the letter generated in step 3 to that person's email address.
