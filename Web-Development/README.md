# Web Development Track

[Back to Main Page](../README.md)

## Overview

This page documents the tasks, progress, and learning outcomes related to the Web Development track of the robotics summer training program.

The Web Development track focuses on creating websites, organizing web files, connecting frontend and backend systems, working with databases and APIs, debugging server problems, and publishing websites online using hosting platforms.

## Tasks

| Task No. | Task Name | Date | Status | Documentation | Live Website |
|---|---|---|---|---|---|
| 1 | Personal Portfolio Website | 2026-07-15 | Completed | [View Task](./Task-1-Personal-Website) | [Open Website](https://mllix-portfolio.nfy.fyi/) |
| 2 | PHP MySQL Form and Status Toggle | 2026-07-25 | Completed | [View Task](./Task-2-PHP-MySQL-Form) | [Open Website](https://mllix-portfolio.nfy.fyi/task-2/) |
| 3 | Voice Assistant PHP Integration and Fix | 2026-08-03 | Completed | [View Task](./Task-3-Voice-Assistant) | [Open Website](https://mllix-portfolio.nfy.fyi/Task-3-Voice-Assistant/) |

## Task Summary

### Task 1: Personal Portfolio Website

This task focused on creating and designing a personal portfolio website using HTML, CSS, and JavaScript.

The website includes a home section, about section, university background section, learning section, projects section, and contact section. It was developed locally using Visual Studio Code and hosted online using InfinityFree.

The project introduced the basic structure of a complete website and the process of organizing frontend files before publishing them online.

[Open Task 1 Documentation](./Task-1-Personal-Website)

### Task 2: PHP MySQL Form and Status Toggle

This task focused on creating a dynamic webpage using HTML, CSS, JavaScript, PHP, and MySQL.

The webpage allows users to submit a name and age, store the data in a MySQL database, display the records in a table, and toggle each record status between `0` and `1`.

The project was developed locally using XAMPP and phpMyAdmin before being uploaded and tested on InfinityFree.

This task introduced the connection between frontend forms, PHP server processing, and MySQL database operations.

[Open Task 2 Documentation](./Task-2-PHP-MySQL-Form)

### Task 3: Voice Assistant PHP Integration and Fix

This task focused on deploying and repairing a web-based Arabic voice assistant.

The original interface loaded correctly, but every submitted voice message displayed a server-connection error. The project was tested locally through XAMPP, debugged using Chrome Developer Tools, connected securely to the Gemini API through PHP, and deployed to InfinityFree.

The completed workflow is:

```text
Arabic Voice Input
        ↓
Browser Speech Recognition
        ↓
Recognized Text
        ↓
JavaScript Fetch Request
        ↓
PHP Backend
        ↓
Gemini API
        ↓
Generated Arabic Response
        ↓
Browser Speech Synthesis
        ↓
Spoken AI Response
```

Several problems were identified and corrected:

- The JavaScript requested an incorrect backend path
- The PHP file loaded `config.php` from the wrong location
- The API-key constant was incorrectly defined
- InfinityFree blocked the original `chat.php` filename
- The browser continued loading an outdated cached JavaScript file
- Gemini Markdown symbols appeared visibly in plain-text responses

The final project now recognizes Arabic speech, sends the transcript securely to Gemini through PHP, displays the generated answer, removes unnecessary Markdown formatting, and reads the response aloud.

[Open Task 3 Documentation](./Task-3-Voice-Assistant)

## Tools and Topics

- HTML
- CSS
- JavaScript
- PHP
- MySQL
- JSON
- Fetch API
- REST APIs
- Gemini API
- PHP cURL
- Web Speech API
- Browser Speech Recognition
- Browser Speech Synthesis
- Arabic language support
- UTF-8 encoding
- Right-to-left web design
- XAMPP
- Apache
- phpMyAdmin
- Chrome Developer Tools
- Browser Network inspection
- HTTP status codes
- JavaScript and PHP integration
- Frontend development
- Backend development
- API integration
- API-key security
- Environment and configuration files
- `.htaccess`
- Directory protection
- Error handling
- Browser cache management
- Responsive design
- Form handling
- Database connection
- CRUD basics
- Status toggle functionality
- File organization
- Local testing
- Web deployment
- InfinityFree
- Visual Studio Code
- GitHub documentation

## Notes

- Each Web Development task has its own folder and README page.
- The main Web Development page is used as an index and summary page.
- Detailed documentation, screenshots, links, source code, and outputs are stored inside each task folder.
- Task 1 was a static personal portfolio website.
- Task 2 was a dynamic PHP and MySQL webpage.
- Task 3 was a voice-enabled web application using JavaScript, PHP, and the Gemini API.
- The real database connection file for Task 2 was not uploaded to GitHub to protect private database information.
- Safe example source code was included for Task 2 using `db.example.php`.
- The real Gemini API key and private `config.php` file for Task 3 were not uploaded to GitHub.
- Task 3 includes `config.example.php` as a safe public configuration template.
- Direct browser access to the private Task 3 configuration file is blocked using `.htaccess`.
- All projects were built and tested before their GitHub documentation was completed.
- InfinityFree was used as the hosting platform, while GitHub was used for project organization and documentation.

## Reflection

The Web Development track helped me understand how websites are structured, styled, tested, debugged, connected to backend services, and hosted online.

Through Task 1, I practiced building a complete static portfolio website using HTML, CSS, and JavaScript. I learned how to organize website sections, create a responsive layout, manage assets, and publish a frontend project through InfinityFree.

Through Task 2, I learned how frontend and backend development work together. I used PHP to receive form data, connected the application to a MySQL database, displayed stored records, and updated their status dynamically. This task also introduced me to XAMPP, phpMyAdmin, local server testing, and private database configuration.

Through Task 3, I gained more experience in debugging and server integration. I learned how to inspect failed network requests, understand HTTP status codes such as `404`, `403`, and `200`, and identify differences between local XAMPP behavior and online InfinityFree hosting.

Task 3 also taught me how to connect JavaScript to PHP using the Fetch API, send and receive JSON, call an external AI service through PHP cURL, and protect an API key from public access. I also learned how browser caching and hosting restrictions can affect a deployed project even when it works correctly on a local server.

The most important lesson from this track was that creating a working website involves more than writing frontend code. A complete project may require server configuration, database or API integration, security measures, local testing, browser debugging, online deployment, and clear technical documentation.

These tasks improved my understanding of both frontend and backend development and gave me practical experience building, troubleshooting, securing, and deploying complete web applications.
