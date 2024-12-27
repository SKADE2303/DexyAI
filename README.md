# DexyAI

This is a web automation tool that automates interactions with platforms like Wellfound. It includes a frontend built with Next.js for user interaction and a backend powered by Python and Selenium for automated browser control.
Demo Link: https://drive.google.com/file/d/1_LE8chAna4x5DMo02f3IgeQgdDK6LsjQ/view?usp=sharing

Modified assignment suggestion : Making the same functionality for a website which doesn't use detectors for automated bots
---

## Features

- Automated login and navigation on websites using Selenium.
- Send predefined messages to specified threads on Wellfound.
- Browser automation with configurable delays to mimic human behavior.
- Frontend built with Next.js for easy user interaction and configuration.

---

## Tech Stack

### Frontend
- **Framework**: Next.js
- **Languages**: JavaScript/TypeScript
- **Styling**: Tailwind CSS (or another styling framework, if applicable)

### Backend
- **Language**: Python
- **Libraries**: Selenium, WebDriver, WebDriverWait

---

## Installation

### Backend

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DexyAI.git
   cd DexyAI/backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the appropriate ChromeDriver version for your Chrome browser and place it in a directory, e.g., `/usr/local/bin/`.

4. Update the `service` path in the `send_message.py` file to point to your ChromeDriver binary.

### Frontend

1. Navigate to the `frontend` directory:
   ```bash
   cd ../frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

---

## Configuration

### Backend

- Set your credentials in the `send_message.py` file:
  ```python
  WELLFOUND_EMAIL = "your_email@example.com"
  WELLFOUND_PASSWORD = "your_password"
  THREAD_URL = "https://wellfound.com/jobs/messages/thread_id"
  MESSAGE = "Hello, this is an automated message!"
  ```

- Adjust delays (`time.sleep`) to mimic human browsing behavior.

### Frontend

- Update the API endpoints in the Next.js application to connect to the backend.

---

## Usage

1. Start the backend:
   ```bash
   python send_message.py
   ```

2. Start the frontend:
   ```bash
   npm run dev
   ```

3. Open the frontend in your browser (typically at `http://localhost:3000`), configure your message, and start the automation process.

---

## Notes

- Ensure your Chrome version matches the ChromeDriver version to avoid compatibility issues.
- Use different user agents in Selenium to avoid detection.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

