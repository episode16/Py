num_of_steps = 3

report_template = """Report
We have made {total} observations from tossing a coin: {tails} of them were tails and {heads} of them were heads.
The probabilities are {tail_fraction:.2f}% and {head_fraction:.2f}%, respectively.
Our forecast is that in the next {steps} observations we will have: {predicted_tails} tail(s) and {predicted_heads} head(s).
"""

log_file = "analytics.log"

telegram_bot_token = "7029978496:AAGrrLmAsto_d3i0UEOAXfH1FWjB1sBbCRw"
telegram_chat_id = "329789520"
telegram_api_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
