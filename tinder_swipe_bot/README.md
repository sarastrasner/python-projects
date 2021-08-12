# Tinder Swipe Bot
A Selenium WebDriver bot that logs in to Tinder with Facebook and swipes right on the first 100 potential matches.

## Feature Tasks
1. Set up your Tinder Account, making sure to use the Facebook/Google login in order to avoid dual verification with a phone every time you log in.
1. Using Selenium and Python Navigate to the Tinder website `https://tinder.com/` and click on LOG IN then LOGIN WITH FACEBOOK.
1. The Facebook login page opens in a new window. In order for our selenium code to work on the new window, we have to switch to the window in front.
1. Then revert to the base_window and verify by printing the title of the Selenium controlled window title.
1. Using Selenium and Python:
    - Click ALLOW for location.
    - Click NOT INTERESTED for notifications.
    - Click I ACCEPT for cookies.
1. Automate clicking the "Like" button. You'll want to add at least a 1 second delay between "Likes" so that Tinder doesn't block you because you seem like a bot.