#!/bin/bash

APP_URL="https://accuknox.com/"
LOG_FILE="app_health_log.txt"
SNS_TOPIC_ARN="arn:aws:sns:ap-northeast-1:050752643577:AppHealthAlerts"

timestamp() {
  date +"%Y-%m-%d %H:%M:%S"
}

echo "$(timestamp) - Health check started." | tee -a $LOG_FILE

# Sends HTTP request
status_code=$(curl -o /dev/null -s -w "%{http_code}" $APP_URL)

if [ $status_code -eq 200 ]; then
    message="$(timestamp) - Application is UP. Status Code: $status_code"
    echo "$message" | tee -a $LOG_FILE
else
    message="$(timestamp) - Application is DOWN. Status Code: $status_code"
    echo "$message" | tee -a $LOG_FILE
    # Sends SNS alert
    aws sns publish --topic-arn $SNS_TOPIC_ARN --message "$message" --subject "ALERT: Application DOWN"
fi

echo "$(timestamp) - Health check finished." | tee -a $LOG_FILE
