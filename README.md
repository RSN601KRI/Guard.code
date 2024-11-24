# Cybersecurity Threat Intelligence Report Generator

## Overview

The **Cybersecurity Threat Intelligence Report Generator** is an AI-powered tool built using **Google's Gemini Pro API** and **Streamlit**. This application allows users to input cybersecurity event details and receive a formal, structured threat intelligence report. The report includes sections like an abstract, incident overview, analysis, recommendations, and conclusions, making it ideal for documenting and analyzing cybersecurity incidents.

This tool uses **Generative AI** to generate detailed and formal reports, aiding cybersecurity teams in understanding incidents, recommending defense measures, and improving future security protocols.

## Key Features

- **Automated Report Generation**: Automatically generates detailed and formal cybersecurity reports based on user input.
- **Incident Analysis**: Provides insights into attack types, vulnerabilities, and defense strategies used.
- **Structured Report**: Generates reports with clear sections such as Abstract, Incident Overview, Recommendations, and Conclusion.
- **Real-time Interaction**: Users can input event details and receive a report instantly.
- **Easy-to-use Interface**: The app is powered by Streamlit for simple, intuitive interaction.

## Prerequisites

Before running the app, ensure you have the following:

- Python 3.7+
- **Google Gemini API key** (for integrating Google's Gemini AI model)
- Install necessary dependencies using `pip`

## Installation

### 1. Clone the Repository

Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/threat-intelligence-report-generator.git
cd threat-intelligence-report-generator
```

### 2. Set Up Environment

Create a `.env` file in the root directory and add your **Google API Key**:
```
GOOGLE_API_KEY=your_google_api_key_here
```

### 3. Install Dependencies

Install the required Python libraries:
```bash
pip install -r requirements.txt
```

Alternatively, install them manually:
```bash
pip install streamlit python-dotenv google-generativeai
```

### 4. Run the App

Start the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`.

## Usage

1. **Enter Event Details**: In the provided text box, input the details of the cybersecurity event (e.g., phishing attack, malware infection, data breach).
2. **Generate Report**: Click on the **"Generate Report"** button, and the system will automatically create a structured threat intelligence report based on the event details.
3. **View the Report**: The generated report will be displayed below the input field with sections like **Abstract**, **Incident Overview**, **Analysis**, **Recommendations**, and **Conclusion**.

Video Link: https://vimeo.com/1032841431/95950d1a51?share=copy

## Project Structure

```
threat-intelligence-report-generator/
│
├── app.py               # Main Streamlit application script
├── .env                 # Environment variables for API key
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation (this file)
└── assets/              # Any static files (e.g., images, icons)
```

## Technologies Used

- **Streamlit**: For creating the user interface and handling real-time interactions.
- **Google Gemini Pro API**: For generating AI-powered responses and reports.
- **Python**: Main programming language used to build the application.
- **dotenv**: For managing sensitive API keys securely.

## Contributing

Contributions are welcome! If you'd like to contribute, feel free to fork the repository, make your changes, and submit a pull request. Please ensure that your changes follow the existing code style and include any relevant tests or documentation updates.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Example Input and Output

#### Input:
```
A phishing attack targeted our employees through a well-crafted email pretending to be from the IT department. The email included a link to a fake login page designed to capture employee credentials. Approximately 50 employees entered their credentials, which were later used to gain unauthorized access to sensitive company data. The breach was detected after a monitoring alert was triggered, and the affected accounts were locked immediately. The phishing domain was also blacklisted, and additional multi-factor authentication (MFA) measures were implemented to prevent further attacks.
```

#### Generated Report:
```
### Abstract:
This report analyzes a phishing attack that targeted employees within the organization. It summarizes the incident details, impact, and the steps taken to mitigate the attack.

### Incident Overview:
A phishing email impersonated the IT department and led to 50 employees submitting their credentials on a fake login page. The breach allowed unauthorized access to sensitive data.

### Analysis:
The phishing attack exploited a lack of user awareness, leveraging social engineering tactics. The attack was detected via monitoring alerts, and immediate actions were taken to lock affected accounts.

### Recommendations:
- Train employees on recognizing phishing attempts.
- Implement multi-factor authentication (MFA) for all accounts.
- Continuously monitor and update security measures to detect emerging threats.

### Conclusion:
The breach was contained successfully, but further precautions are recommended to prevent similar attacks in the future.
```

## Contact

For any inquiries or support, please contact:
- **Email**: roshni06k2004@gmail.com
- **GitHub**: [@yourusername](https://github.com/RSN601KRI)
