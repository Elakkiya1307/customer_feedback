# ============================
# ReviewSense – Milestone 2
# Sentiment Analysis Module
# ============================

import pandas as pd
from textblob import TextBlob

# -------- Sentiment Function --------
def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity
    if polarity > 0:
        return "Positive", polarity
    elif polarity < 0:
        return "Negative", polarity
    else:
        return "Neutral", polarity

# -------- Main Execution --------
if __name__ == "__main__":

    # Input from Milestone 1
    df = pd.read_csv("Milestone1_Cleaned_Feedback.csv")

    # Apply sentiment analysis
    df[["sentiment", "confidence_score"]] = df["clean_feedback"].apply(
        lambda x: pd.Series(get_sentiment(x))
    )

    # Save output for next milestones
    df.to_csv("Milestone2_Sentiment_Results.csv", index=False)

    print("Milestone 2 completed successfully ✅")
    print(df[["clean_feedback", "sentiment", "confidence_score"]].head())
