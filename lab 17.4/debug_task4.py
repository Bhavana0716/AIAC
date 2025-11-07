import sys
import traceback

try:
    print("Starting script execution...")
    
    # Import all required modules
    print("\nImporting modules...")
    import pandas as pd
    print("pandas imported")
    import re
    print("re imported")
    import codecs
    print("codecs imported")
    import nltk
    print("nltk imported")
    from nltk.corpus import stopwords
    print("stopwords imported")
    from nltk.tokenize import word_tokenize
    print("word_tokenize imported")
    from nltk.stem import WordNetLemmatizer
    print("WordNetLemmatizer imported")
    
    # Download NLTK data with progress indication
    print("\nDownloading NLTK data...")
    for package in ['punkt', 'stopwords', 'wordnet', 'averaged_perceptron_tagger', 'omw-1.4']:
        print(f"Downloading {package}...")
        nltk.download(package, quiet=True)
        print(f"{package} downloaded successfully")
    
    # Run the main script
    print("\nExecuting main script...")
    import task4
    task4.main()
    
except Exception as e:
    print("\nAn error occurred:", str(e), file=sys.stderr)
    print("\nFull traceback:", file=sys.stderr)
    traceback.print_exc()