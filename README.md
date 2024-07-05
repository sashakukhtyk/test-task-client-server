# Test Task Client-Server Application

This project is a client-server application designed to demonstrate basic networking, data encryption/decryption, and database operations. The server listens for incoming connections, decrypts received data, and stores it in a database.

## Features

- **Server**: Listens on a specified port for incoming connections.
- **Client**: Sends encrypted data to the server.
- **Encryption/Decryption**: Utilizes a simple encryption algorithm for data transmission.
- **Database Integration**: Inserts decrypted data into a specified database table.
- **Django Web Application**: Provides a web interface to view the data stored in the database.


## Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL or any SQL database
- Django

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/test-task-client-server.git
```

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
```

### Configuration

1. Update the `settings.py` file with your database connection details and encryption key.

### Running the Application

1. Start the server:
   ```bash
   python server.py
   ```
2. In a separate terminal, start the django app:
   ```bash
   python manage.py runserver
   ```

## Usage

Once both the server and client are running, the client will send encrypted data to the server, which will then decrypt and insert the data into the database.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.



