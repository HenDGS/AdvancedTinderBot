# Tinder Bot
<a id="readme-top"></a>

<!-- TABLE OF CONTENTS -->
## Table of Contents

<details>
  <summary>Index</summary>
    <ol>
        <li>
        <a href="#about-the-project">About The Project</a>
        </li>      
        <li>
        <a href="#how-to-use">How To Use</a>
        </li>
        <li>
        <a href="#how-to-run">How To Run</a>
        </li>
        <li>
        <a href="#to-do">To Do</a>
        </li>
    </ol>
</details>

<!-- ABOUT THE PROJECT -->
<a id="about-the-project"></a>
## About The Project

A bot to auto-like on Tinder with human-like interactions. The best feature of this bot is that it has options for filters that are not available on the Tinder app, like filtering by name or race, with more to come.

Uses Selenium to create a local Chrome User on the same path as the .exe and like profiles with human time speed and random timed interactions (like scrolling through photos) to not be perceived as a bot.

<p style="text-align: right;">(<a href="#readme-top">back to top</a>)</p>

<!-- HOW TO USE -->
<a id="how-to-use"></a>
## How To Use

Run the **Tinder Bot.exe** and click the * *First Login* * button.

![First Login](https://i.imgur.com/gKXMZMC.png)

Proceed to login with your account, select if you want to use location and disable notifications. Then click * *OK* * on the window that appeared.

![Login](https://imgur.com/OxI2IVC.png)

Click * *OK* * again to confirm saving this account. 

![Confirm](https://imgur.com/Q636T03.png)

A folder named * *ChromeData* * should have appeared on the same path as the .exe. This folder contains the user data for the bot to use.

Now go to the * *Options* * tab and select the filters you want to use. 
The bot will only like profiles that match the filters.

(Headless mode will hide the browser window, making it run in the background.)

![Options](https://i.imgur.com/79V8ZDz.png)

Now start the bot with the selected number of likes and like ratio of the bot.

![Start](https://i.imgur.com/3hKNSG3.png)

The * *Console* * tab will print some events that happened.

![Console](https://i.imgur.com/foWXQbp.png)

<p style="text-align: right;">(<a href="#readme-top">back to top</a>)</p>

<!-- HOW TO RUN FROM SOURCE -->
<a id="how-to-run"></a>
## How To Run

Clone or download the repository and run the following commands on the terminal in the directory of the project.

```bash 
pip install -r requirements.txt
```

```bash
python src/gui.py
```

Alternatively, you can run the * *main.py* * file directly. But as its still not officially supported, you can't pass the arguments in terminal, so you will have to change the default values in the code.

```bash
python src/main.py
```

<p style="text-align: right;">(<a href="#readme-top">back to top</a>)</p>

<!-- To Do -->
<a id="to-do"></a>
## To Do

- [ ] Add filter for tags
- [ ] Add filter for job
- [ ] Add filter for height
- [ ] Add filter for zodiac signs
- [ ] Add filter for keywords in bio (blacklist and whitelist)
- [ ] Add log with results
- [ ] Add video tutorial
- [ ] Add option to use a proxy
- [ ] Disable buttons in GUI while bot is running
- [ ] Add option for the user to control the bot speed
- [ ] Add option to use ChatGPT API to answer messages
- [ ] Better terminal support

<p style="text-align: right;">(<a href="#readme-top">back to top</a>)</p>

<!-- FAQ -->
<a id="faq"></a>
## FAQ

- Why use ChromeData instead of auto-login?

    Because 2FA, and the fact that there are 3 ways to login. Also, its safer to use the user data and just login once instead of constantly send suspicious login requests to Tinder.


<p style="text-align: right;">(<a href="#readme-top">back to top</a>)</p>
