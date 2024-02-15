# Alertmanager-Prometheus to Signals Test

This project sets up a monitoring solution using Prometheus and Alertmanager, with a custom Python server acting as the exporter for test metrics. Follow these steps to clone the repository, set up the environment, and test alerting functionality with your webhook.

## Prerequisites

- Docker
- Docker Compose
- Git

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone git@github.com:christopherweber/alertmanger-prometheus-signals-alert-testing.git
cd alertmanger-prometheus-signals-alert-testing
```

### 2. Configure Alertmanager
Before building the Docker containers, you need to configure Alertmanager to use your webhook.

- Open alertmanager.yml with a text editor of your choice.
- Locate the webhook_configs section.
- Replace the placeholder with the webhook URL provided by Signals.

```receivers:
- name: 'web.hook'
  webhook_configs:
  - url: '<your_signals_webhook_url_here>'
```

### 3. Build with Docker Compose
With the webhook configured, build the Docker environment:

```docker-compose build```

### 4. Running the Services
To start the services:

```docker-compose up -d```

### 5. Accessing the Interfaces
You can access the Prometheus and Alertmanager UIs at the following local paths:

- Prometheus: http://localhost:9090
- Alertmanager: http://localhost:9093

### 6. The Python Exporter Server
The python_exporter service runs a simple Python server that exposes custom test metrics for Prometheus to scrape.

### 7. Testing Alerting
To test the alerting functionality, you can simulate an outage by stopping the python_exporter:

```docker-compose stop python_exporter```

After approximately 5 minutes, Prometheus will detect that the python_exporter is down and will fire an alert. This alert should then be visible in the Prometheus UI under the 'Alerts' tab.

Note: In Prometheus go to Status => Targets to see that python_exporter's state. This is different from the Alerts page which will go "Pending" to "Firing" to AlertManager.

To restart the python_exporter"

```docker-compose start python_exporter```

### 8. Receiving Events in Signals
Once Prometheus fires the alert, Alertmanager will process this alert and send an event to the configured webhook in Signals.

### 9. Customization
This setup is customizable. You can adjust the alerting rules and Alertmanager configuration via the alert.rules.yml file.

### Notes
Remember to keep your webhook URL secure and not expose it in public repositories or logs.