# DBPulse

DBPulse is a monitoring tool designed to provide insights into the performance of your MongoDB database. It offers real-time data on key performance metrics such as active connections, disk space usage, and CPU usage.

## Features

- **Uptime Monitoring**: Monitor the uptime of your MongoDB instance.
- **Active Connections**: Monitor the number of active connections to your MongoDB instance.
- **Disk Space Usage**: Track the amount of disk space being used by your MongoDB data.

## Installation

To get started with DBPulse, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/telexintegrations/DBPulse
   ```

2. Navigate to the project directory:

   ```bash
   cd DBPulse
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage 

You can configure the MongoDB connection settings in the `.env` file. Check `env.example` for the required variables. Ensure the connection string has the `cluster monitoring` role enabled.

## Local Monitoring

To monitor your MongoDB instance locally without setting up the web server, use the CLI tool:

```bash
cd src
python cli.py
```

This will display MongoDB metrics in your console and refresh every 10 seconds. Press Ctrl+C to stop monitoring.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or feedback, please contact [adedotunomomeji@gmail.com](mailto:adedotunomomeji@gmail.com).
