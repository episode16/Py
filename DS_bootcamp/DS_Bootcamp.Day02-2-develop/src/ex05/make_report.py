import sys
from analytics import Research
import config


def main():
    try:

        research = Research(sys.argv[1])
        data = research.file_reader()

        analytics = Research.Analytics(data)
        heads, tails = analytics.counts()
        head_fraction, tail_fraction = analytics.fractions()
        random_predictions = analytics.predict_random(config.num_of_steps)

        predicted_heads = sum(pred[0] for pred in random_predictions)
        predicted_tails = config.num_of_steps - predicted_heads

        report = config.report_template.format(
            total=heads + tails,
            heads=heads,
            tails=tails,
            head_fraction=head_fraction,
            tail_fraction=tail_fraction,
            steps=config.num_of_steps,
            predicted_heads=predicted_heads,
            predicted_tails=predicted_tails,
        )

        analytics.save_file(report, "report")

        print(report)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
