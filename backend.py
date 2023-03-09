from nltk.sentiment import SentimentIntensityAnalyzer as SIA


def analyze_entries(entries):
    analyzer = SIA()
    general_sentiment = []
    for entry in entries:
        score = analyzer.polarity_scores(entry)
        general_sentiment.append(score)
    return general_sentiment


if __name__ == "__main__":
    import glob
    entries = []
    for i in sorted(glob.glob('diary_entries/*.txt')):
        with open(i, 'r') as file:
            entry = file.read()
            entries.append(entry)
    print(analyze_entries(entries))
