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

4. Start the server:

   ```bash
   uvicorn main:app --reload --app-dir src
   ```

5. Make a post request to the `/api/tick` endpoint with the following payload:

   ```bash
   {
      "channel_id": "1234567890",   
      "return_url": "http://localhost:8000/tick", // URL to send the data to
      "settings": [
         {
            "label": "db_uri",
            "type": "text",
            "required": true,
            "default": "mongodb://localhost:27017/test" // URI of the database to monitor
         }
      ]
   }
   ```

## Local Monitoring

To monitor your MongoDB instance locally without setting up the web server, use the CLI tool:

Configure the MongoDB connection settings in the `.env` file. Check `env.example` for the required variables. Ensure the connection string has the `cluster monitoring` role enabled.



```bash
cd src
python cli.py
```

This will display MongoDB metrics in your console and refresh every 10 seconds. Press Ctrl+C to stop monitoring.

## Intergating with Telex

To integrate with Telex, you need to deploy the app to a server and copy the `integration.json` endpoint url to your telex 
integration.

```bash
{base_url}/api/integration.json
```

![image](https://dbpulse.s3.us-east-1.amazonaws.com/Screenshot+2025-02-23+014717.png)

Once that is done, you can should see the application in your telex dashboard.

![image](https://dbpulse.s3.us-east-1.amazonaws.com/Screenshot+2025-02-23+013723.png)

Click on Manage App -> Settings and then set your `DB_URI` and `TIME_INTERVAL` (cron equivalent for the interval you wish to receive data).
**Ensure that the DB_URI has cluster monitoring role enabled.**
**It is recommended that the Cluster is on a dedicated server(example is MongoDB Atlas M10, M20, M30) for accurate memory usage monitoring.**

![image](https://dbpulse.s3.us-east-1.amazonaws.com/Screenshot+2025-02-23+014812.png)

Save your settings and you should start receiving data as scheduled in the telex channel for which the integration was added 

## Testing the integration on telex

To test the integration on telex, you can use this curl command: - I have provided a mongodb uri and telex channel id for testing. Channel name - dbpulse

```bash

curl -X POST "https://dbpulse.onrender.com/api/tick" -H "Content-Type: application/json" -d "{\"channel_id\": \"12345d\", \"return_url\": \"https://ping.telex.im/v1/webhooks/0195370a-c6a0-7904-9e75-dbd2b5f7c035\", \"settings\": [{\"label\": \"db_uri\", \"type\": \"text\", \"required\": true, \"default\": \"mongodb+srv://adedotunomomeji:3nuDpwx3!Tkbwj2@clusternew.tep94.mongodb.net/?retryWrites=true^&w=majority^&appName=ClusterNew/test\"}]}"

```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or feedback, please contact [adedotunomomeji@gmail.com](mailto:adedotunomomeji@gmail.com).
