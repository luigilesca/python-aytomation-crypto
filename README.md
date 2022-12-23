# Python automation-cryptocurrencies

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


This app is built by Python and uses CoinMarketCap's API (The CoinMarketCap API is a suite of high-performance RESTful JSON endpoints that are specifically designed to meet the mission-critical demands of application developers, data scientists, and enterprise business platforms).

This app creates a JSON file evry day, at a certain specific time.

In thi file JSON you can find:

  1. The Crypto with the largest volume (in $) of the last 24 hours.

  2. The best and worst 10 cryptocurrencies (by % increase) of the last 24 hours.

  3. The amount of $ needed to buy one unit of each of the top 20 cryptocurrencies.

  4. The amount of $ required to purchase a unit of all Crypto whose volume in the last 24 hours exceeds 76,000,000$.

  5. Profit/loss % you would have made if you had bought one unit of each of the top 20 cryptocurrencies the day before (assuming that the rankings have     not changed).

Once the project is complete, send the report in JSON.


Use the `BLANK_README.md` to get started.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With
- [PYTHON](https://www.python.org/)



## Getting Started

### Prerequisites

Running the application requires [Python](https://www.python.org/) to be installed on your operating system.

### Installation

1. Clone the repository locally with the git command:

   ```sh
   git clone https://github.com/luigilesca/python.git
   ```

2. Check if you have PIP packages:

   ```sh
   pip --version
   ```
   
   if you don't have pip you can install it following the official guide (https://pip.pypa.io/en/stable/cli/pip_install/)

3. Intall requests library with pip:

   ```sh
   pip install requests
   ```

4. Replace this parameter (os.environ.get("API_KEY")) with your API_KEY --> you must sign in to CoinMArketCap to download your FREE API_KEY (https://pro.coinmarketcap.com/account)

   ```sh
   pip install requests
   ```
5. Now you can start your app.


## License

Distributed under the MIT License. See `LICENSE` for more information.

## Links & Contacts

[@Luigi Lesca](https://www.linkedin.com/in/luigi-lesca/) - luigilesca@hotmail.it

Project Repository: [python-cryptocurrencies-automation
](https://github.com/luigilesca/python.git)


Portfolio: [Luigi Lesca-web-developer-portfolio](https://talent.start2impact.it/profile/luigi-lesca)
