import re
from collections import Counter

def count_specific_word(text, search_word):
    """
    Count the number of occurrences of a specific word in the text.
    
    Args:
        text (str): The text to search through
        search_word (str): The word to search for
    
    Returns:
        int: The count of occurrences
    """
    if not text or not search_word:
        return 0
    
    # Convert both text and search word to lowercase for case-insensitive search
    text_lower = text.lower()
    search_word_lower = search_word.lower()
    
    # Count occurrences
    count = text_lower.count(search_word_lower)
    return count

def identify_most_common_word(text):
    """
    Identify the most common word in the text.
    
    Args:
        text (str): The text to analyze
    
    Returns:
        str: The most common word, or None if text is empty
    """
    if not text:
        return None
    
    # Clean the text by removing punctuation and converting to lowercase
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Split into words and filter out empty strings
    words = [word for word in cleaned_text.split() if word]
    
    if not words:
        return None
    
    # Count word frequencies
    word_counts = Counter(words)
    
    # Return the most common word
    return word_counts.most_common(1)[0][0]

def calculate_average_word_length(text):
    """
    Calculate the average length of words in the text.
    
    Args:
        text (str): The text to analyze
    
    Returns:
        float: The average word length
    """
    if not text:
        return 0.0
    
    # Clean the text by removing punctuation and special characters
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    
    # Split into words and filter out empty strings
    words = [word for word in cleaned_text.split() if word]
    
    if not words:
        return 0.0
    
    # Calculate total length and average
    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)
    
    return round(average_length, 2)

def count_paragraphs(text):
    """
    Count the number of paragraphs in the text.
    
    Args:
        text (str): The text to analyze
    
    Returns:
        int: The number of paragraphs
    """
    if not text:
        return 1
    
    # Split text by double newlines (paragraphs)
    paragraphs = text.split('\n\n')
    
    # Filter out empty paragraphs and count
    non_empty_paragraphs = [p.strip() for p in paragraphs if p.strip()]
    
    # If no paragraphs found, return 1
    return len(non_empty_paragraphs) if non_empty_paragraphs else 1

def count_sentences(text):
    """
    Count the number of sentences in the text.
    
    Args:
        text (str): The text to analyze
    
    Returns:
        int: The number of sentences
    """
    if not text:
        return 1
    
    # Split text by sentence-ending punctuation marks
    sentences = re.split(r'[.!?]+', text)
    
    # Filter out empty sentences and count
    non_empty_sentences = [s.strip() for s in sentences if s.strip()]
    
    # If no sentences found, return 1
    return len(non_empty_sentences) if non_empty_sentences else 1

def run_interactive_analysis():
    """
    Run the interactive text analysis program.
    This function contains the main program logic with while loops, for loops, and conditionals.
    """
    print("=== News Article Text Analysis ===")
    print()
    
    # Read the news article from README.md
    try:
        with open('README.md', 'r', encoding='utf-8') as file:
            news_article = file.read()
        print("Successfully loaded news article from README.md")
        print()
    except FileNotFoundError:
        print("Error: README.md file not found!")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    # Initialize variables for the while loop
    continue_analysis = True
    analysis_count = 0
    
    # Use while loop as required
    while continue_analysis:
        analysis_count += 1
        print(f"--- Analysis Run #{analysis_count} ---")
        print()
        
        # Display article statistics
        print("Article Statistics:")
        print(f"   • Total characters: {len(news_article)}")
        print(f"   • Total words: {len(news_article.split())}")
        print(f"   • Paragraphs: {count_paragraphs(news_article)}")
        print(f"   • Sentences: {count_sentences(news_article)}")
        print()
        
        # Use for loop as required - iterate through different search words
        search_words = ["apple", "machine", "technology", "baking", "pie"]
        
        print("Word Frequency Analysis:")
        for word in search_words:
            count = count_specific_word(news_article, word)
            print(f"   • '{word}': {count} occurrences")
        print()
        
        # Most common word analysis
        most_common = identify_most_common_word(news_article)
        print(f"Most Common Word: '{most_common}'")
        print()
        
        # Average word length
        avg_length = calculate_average_word_length(news_article)
        print(f"Average Word Length: {avg_length} characters")
        print()
        
        # Use conditional statement as required
        if analysis_count == 1:
            print("First analysis complete! Would you like to run another analysis?")
        else:
            print(f"Analysis #{analysis_count} complete! Would you like to run another analysis?")
        
        # Ask user if they want to continue
        user_input = input("Enter 'y' to continue or any other key to exit: ").lower().strip()
        
        if user_input != 'y':
            continue_analysis = False
            print("\nThank you for using the News Article Text Analyzer!")
        else:
            print("\n" + "="*50 + "\n")
    
    print(f"\nTotal analyses performed: {analysis_count}")

# Only run the interactive program if this file is run directly
if __name__ == "__main__":
    run_interactive_analysis()
