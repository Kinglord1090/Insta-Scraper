
# Insta-Scraper 📸

Insta-Scraper is a tool designed to quickly extract information from public Instagram profiles, such as the user-provided name, number of posts, followers, following count, and profile description. This tool uses Selenium to automate the data extraction process, making it useful for gathering insights about public profiles efficiently.

## Features

- **Automated Data Extraction**: Uses Selenium to log in and fetch information from Instagram profiles automatically.
- **Profile Information Retrieval**: Extracts name, post count, followers, following count, and bio description of the target profile.
- **Headless Mode**: Operates in headless mode for efficiency and to avoid UI interruptions during scraping.
- **Error Handling**: Implements basic error handling for cases where elements might not be found.
- **Privacy Focused**: Does not save or transmit login details locally or over the internet.
- **Extensible Codebase**: Code is structured for easy modifications and additional features.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Kinglord1090/insta-scraper.git
    ```

2. Install the required Python libraries:
    ```bash
    python3 -m pip install -r requirements.txt
    ```

## Setup

1. **Download Chromedriver**:  
   Download the latest or your specific Chrome version of Chromedriver from [here](https://chromedriver.chromium.org/downloads).  

2. **Place Chromedriver**:  
   Ensure that both the Python script (`insta-scraper.py`) and Chromedriver are in the same folder.  

3. **Set Environment Variables**:  
   Make sure Python is included in the PATH environment variables.  

## Usage

1. Open the terminal and navigate to the script’s directory:
    ```bash
    cd insta-scraper
    ```

2. Run the script:
    ```bash
    python insta-scraper.py
    ```

3. Enter your Instagram login credentials and the target username when prompted.  
   > **Note:** None of these details are saved locally or transmitted over the internet.

4. View the extracted profile information directly in the terminal.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [Selenium](https://www.selenium.dev/) for providing the automation framework.  
- Inspired by the need for efficient data gathering tools for public profiles.  
