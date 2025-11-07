import pandas as pd
import re
import sys
import subprocess
import codecs

# Set UTF-8 as default encoding for stdout
if sys.stdout.encoding != 'utf-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Try to import NLTK, install if not present
try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from nltk.stem import WordNetLemmatizer
except ImportError:
    print("NLTK not found. Installing NLTK...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "nltk"])
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from nltk.stem import WordNetLemmatizer

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')  # Required for lemmatization
nltk.download('omw-1.4')  # Required for lemmatization

def clean_text(text):
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    # Remove emojis
    text = re.sub(r'[^\w\s,]', '', text, flags=re.UNICODE)
    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    return text

def preprocess_text(text, stop_words, lemmatizer):
    text = clean_text(text)
    # Simple word tokenization by splitting on whitespace
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

def main():
    # Create sample dataset
    data = {
        'post_id': range(1, 11),
        'text': [
            "I love this new phone 😍! The camera quality is amazing! https://techsite.com",
            "Worst customer service ever!! 😡 #frustrated",
            "Just got my order delivered... it's okay, not great, not terrible.",
            "Check out my new blog post 👉 www.myblog.com/travel",
            "I'm so happy with the results! Totally worth it!!",
            "This update ruined the app 😤 now it crashes every time!!",
            "Had a wonderful weekend with friends ❤️",
            "I don't know how to feel about this 🤔",
            "@brand your service is pathetic 😠 will never buy again!",
            "Absolutely love the new design and performance!"
        ],
        'sentiment': ['positive', 'negative', 'neutral', 'neutral', 'positive', 
                     'negative', 'positive', 'neutral', 'negative', 'positive']
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save original dataset with UTF-8 encoding
    df.to_csv('social_media_sentiment.csv', index=False, encoding='utf-8')
    
    # Display original data
    print("Original Data:")
    try:
        print(df.to_string(index=False))
    except UnicodeEncodeError:
        # Fallback to simple display without emojis
        pd.set_option('display.max_colwidth', None)
        print(df.to_string(index=False, max_colwidth=50))
    
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    # Process the text
    df['processed_text'] = df['text'].apply(lambda x: preprocess_text(str(x), stop_words, lemmatizer))

    print("\nProcessed Data:")
    try:
        print(df.to_string(index=False))
    except UnicodeEncodeError:
        # Fallback to simple display without emojis
        pd.set_option('display.max_colwidth', None)
        print(df.to_string(index=False, max_colwidth=50))
    
    # Save processed dataset with UTF-8 encoding
    df.to_csv('social_media_sentiment_processed.csv', index=False, encoding='utf-8')
    print("\nProcessed dataset saved to: social_media_sentiment_processed.csv")

if __name__ == '__main__':
    main()