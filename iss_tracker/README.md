# International Space Station Tracker
An ISS tracker that emails me if it's dark out, and the ISS is overhead. Utilizes 
Sunrise-Sunset and ISS Open-Notify APIs and `smtplib` for email.

## Feature Tasks
1. If the ISS is close to my current position, and it's currently dark:
    1. Create fn that returns true if your position is within +5 or -5 degrees of the ISS position.
    1. Create fn that returns true if it's currently dark out.
1. Then email me to tell me to look up.
   1. Utilize `smtplib` for email.
1. Run the code every 60 seconds.
    1. Use `time` module to sleep code for 60 seconds.