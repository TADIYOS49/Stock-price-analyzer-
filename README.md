# Stock Price Analyzer

Welcome to the Stock Price Analyzer! This project leverages OpenAI's Large Language Models (LLMs) to provide natural language-based stock price inquiries and analyses. By integrating with the Yahoo Finance API, users can effortlessly retrieve real-time stock prices, analyze historical data, and compare the performance of multiple stocks over specified time frames.

## Features

- **Natural Language Stock Queries**: Ask about stock prices using company names (e.g., "Apple", "Google", "Meta"), and the system will automatically convert these to their respective ticker symbols to fetch real-time prices.
- **Historical Price Analysis**: Retrieve and analyze stock price changes over custom time ranges, such as the past 30 days.
- **Performance Comparison**: Compare the performance of multiple stocks within a specified time frame to determine which has performed best.

## Technologies Used

- **Backend Framework**: FastAPI
- **Language Models**: OpenAI's LLMs
- **Data Retrieval**: Yahoo Finance API
- **Orchestration**: Langchain
- **Programming Languages**: Python

## Folder Structure

The project's folder structure is organized as follows:

- **app/**: Contains the main application code.
- **experiment/**: Includes experimental scripts and notebooks. There are still more improvements and other modifications that can be applied like better memory management, streaming output, and other guardrails you can have. 
- **.gitignore**: Specifies files and directories to be ignored by Git.


## Getting Started

To set up and run the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/TADIYOS49/Stock-price-analyzer-.git
   cd Stock-price-analyzer-
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```
   The application will be accessible at `http://127.0.0.1:8000`.

## Usage

Once the server runs, you can interact with the application using natural language queries to retrieve stock information, analyze historical data, and compare stock performances. ( Utilize Swagger for ease )

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

*Note: This project is for educational and informational purposes only. It should not be considered financial advice.* 
