import os
import logging
from random import randint
import requests
import config

logging.basicConfig(
    filename=config.log_file,
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class Research:
    def __init__(self, file_name):
        self.file_name = file_name
        logging.info("Initialized Research with file: %s", file_name)

    def file_reader(self, has_header=True):
        logging.info("Reading file: %s", self.file_name)
        try:
            with open(self.file_name, "r") as f:
                lines = f.read().strip().split("\n")
                if has_header:
                    lines = lines[1:]
                data = [list(map(int, line.split(","))) for line in lines]
                logging.info("File successfully read: %s", self.file_name)
                return data
        except Exception as e:
            logging.error("Error reading file: %s", e)
            raise Exception(f"File reading error: {e}")

    def send_telegram_message(self, message):
        logging.info("Sending Telegram message: %s", message)
        payload = {
            "chat_id": config.telegram_chat_id,
            "text": message,
        }
        try:
            response = requests.post(config.telegram_api_url, json=payload)
            if response.status_code == 200:
                logging.info("Telegram message sent successfully")
            else:
                logging.error(
                    "Failed to send Telegram message, status code: %s, response: %s",
                    response.status_code,
                    response.text,
                )
        except Exception as e:
            logging.error("Error sending Telegram message: %s", e)

    class Calculations:
        def __init__(self, data):
            self.data = data
            logging.info("Initialized Calculations with data: %s", data)

        def counts(self):
            logging.info("Calculating the counts of heads and tails")
            heads = sum(row[0] for row in self.data)
            tails = len(self.data) - heads
            logging.info("Counts calculated: heads=%d, tails=%d", heads, tails)
            return heads, tails

        def fractions(self):
            logging.info("Calculating the fractions of heads and tails")
            heads, tails = self.counts()
            total = heads + tails
            head_fraction = (heads / total) * 100
            tail_fraction = (tails / total) * 100
            logging.info(
                "Fractions calculated: head_fraction=%.2f, tail_fraction=%.2f",
                head_fraction,
                tail_fraction,
            )
            return head_fraction, tail_fraction

    class Analytics(Calculations):
        def predict_random(self, num_of_predictions):
            logging.info("Predicting %d random outcomes", num_of_predictions)
            predictions = []
            for _ in range(num_of_predictions):
                head = randint(0, 1)
                predictions.append([head, 1 - head])
            logging.info("Random predictions generated: %s", predictions)
            return predictions

        def predict_last(self):
            logging.info("Predicting the last outcome")
            prediction = self.data[-1]
            logging.info("Last prediction: %s", prediction)
            return prediction

        @staticmethod
        def save_file(data, filename, extension="txt"):
            logging.info("Saving data to file: %s.%s", filename, extension)
            if not isinstance(data, str):
                data = str(data)
            try:
                with open(f"{filename}.{extension}", "w") as f:
                    f.write(data)
                logging.info("File saved successfully: %s.%s", filename, extension)
            except Exception as e:
                logging.error("Error saving file: %s", e)
