
# Smart Mirror

## Overview
The **Smart Mirror** project is a highly interactive and feature-rich system built with real-time data integration. Designed to provide users with useful daily information, it combines various technologies such as IoT, software development, and user experience design to create an immersive and functional mirror. 

The mirror displays live updates like weather information, calendar events, and time, while integrating voice control for enhanced interaction. This project was developed using **Kali Linux** and demonstrates the capabilities of **Google Assistant** for voice commands, **RSS feeds** for news updates, and **Snow Boy** for wake word detection.

## Features
- **Interactive Voice Control**: Users can interact with the mirror using voice commands via **Google Assistant**.
- **Weather Updates**: Real-time weather data displayed, sourced from a weather API.
- **Calendar Integration**: Displays events from a Google Calendar to keep track of your schedule.
- **Real-time Data**: Integration of live data feeds such as news and RSS for the latest information.
- **Wake Word Detection**: The mirror responds to the voice command "Hey, Google" using **Snow Boy** for wake word detection.
- **Kali Linux**: Developed and run on **Kali Linux**, utilizing its powerful capabilities for system control and integration.

## Technologies Used
- **JavaScript**: Core programming language used for building the application logic.
- **Kali Linux**: Operating system for hosting the Smart Mirror and executing tasks.
- **Google Assistant**: Provides voice control functionality.
- **RSS Feeds**: For integrating live news and updates into the mirror.
- **Snow Boy**: Wake word detection for listening and triggering voice commands.
  
## Setup Instructions

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/smart-mirror.git
   ```

2. Navigate to the project directory:
   ```bash
   cd smart-mirror
   ```

3. Install the required dependencies:
   ```bash
   npm install
   ```

4. Set up the Google Assistant API by creating a project in the Google Cloud Console and obtaining the necessary credentials. You will need to replace the placeholder in the `credentials.json` file.

5. Run the application:
   ```bash
   npm start
   ```

6. Your Smart Mirror should now be running and responding to voice commands.

## Future Enhancements
- Add more interactive features such as news, traffic updates, and more smart home controls.
- Implement additional IoT devices and sensors for further integration.
- Improve voice recognition for better user interaction.

## Contributing
Feel free to fork the repository, create a pull request, and contribute to improving the Smart Mirror project. All contributions are welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
