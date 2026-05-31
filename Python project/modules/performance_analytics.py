# Q8: Student Performance Analysis using NumPy, Pandas, Matplotlib
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt


def create_sample_csv(filepath):
    """Create a sample student performance CSV file"""
    data = {
        'Name': ['Priya', 'Rahul', 'Anita', 'Vikram', 'Sneha'],
        'Math': [85, 72, 95, 88, 78],
        'Science': [90, 88, 89, 92, 85],
        'English': [78, 91, 92, 85, 88]
    }
    
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)
    return df


def analyze_student_performance(csv_filepath):
    """
    Analyzes student performance data from CSV file
    """
    print("\n" + "="*50)
    print("    STUDENT PERFORMANCE ANALYSIS")
    print("="*50)
    
    try:
        # Check if file exists, if not create sample data
        if not os.path.exists(csv_filepath):
            print("\nCreating sample CSV file...")
            create_sample_csv(csv_filepath)
            print(f"✓ Sample CSV created: {os.path.basename(csv_filepath)}")
        
        # Load data using Pandas
        df = pd.read_csv(csv_filepath)
        
        print("\n" + "-"*50)
        print("            RAW DATA")
        print("-"*50)
        print(df.to_string(index=False))
        
        # Statistical summaries using Pandas
        print("\n" + "-"*50)
        print("            STATISTICAL SUMMARY")
        print("-"*50)
        print(df[['Math', 'Science', 'English']].describe().to_string())
        
        # Convert to NumPy array for numerical operations
        scores = df[["Math", "Science", "English"]].to_numpy()
        
        # Compute mean, median, and standard deviation using NumPy
        mean_scores = np.mean(scores, axis=0)
        median_scores = np.median(scores, axis=0)
        std_dev_scores = np.std(scores, axis=0)
        
        print("\n" + "-"*50)
        print("            NUMPY ANALYSIS")
        print("-"*50)
        print(f"Mean Scores (Math, Science, English):")
        print(f"  {mean_scores}")
        print(f"\nMedian Scores (Math, Science, English):")
        print(f"  {median_scores}")
        print(f"\nStandard Deviation (Math, Science, English):")
        print(f"  {std_dev_scores}")
        
        # Basic Data Analysis - Top Performers
        print("\n" + "-"*50)
        print("            TOP PERFORMERS")
        print("-"*50)
        
        try:
            top_math = df.loc[df["Math"].idxmax(), "Name"]
            print(f"Math:    {top_math}")
        except:
            top_math = "N/A"
        
        try:
            top_science = df.loc[df["Science"].idxmax(), "Name"]
            print(f"Science: {top_science}")
        except:
            top_science = "N/A"
        
        try:
            top_english = df.loc[df["English"].idxmax(), "Name"]
            print(f"English: {top_english}")
        except:
            top_english = "N/A"
        
        # Generate visualizations
        print("\n" + "-"*50)
        print("            GENERATING VISUALIZATIONS")
        print("-"*50)
        
        generate_visualizations(df, mean_scores)
        
    except FileNotFoundError:
        print(f"Error: CSV file not found at {csv_filepath}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


def generate_visualizations(df, mean_scores):
    """Generate and display charts"""
    try:
        # Create a figure with subplots
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Chart 1: Average scores per subject
        subjects = ["Math", "Science", "English"]
        colors = ["blue", "green", "orange"]
        
        axes[0].bar(subjects, mean_scores, color=colors, alpha=0.7, edgecolor='black')
        axes[0].set_title("Average Scores per Subject", fontsize=12, fontweight='bold')
        axes[0].set_xlabel("Subjects")
        axes[0].set_ylabel("Average Score")
        axes[0].set_ylim(0, 100)
        axes[0].grid(axis='y', alpha=0.3)
        
        # Add value labels on bars
        for i, v in enumerate(mean_scores):
            axes[0].text(i, v + 1, f'{v:.1f}', ha='center', fontweight='bold')
        
        # Chart 2: Student-wise performance
        df_plot = df.set_index('Name')
        df_plot.plot(kind='bar', ax=axes[1], color=colors, alpha=0.7, edgecolor='black')
        axes[1].set_title("Student Performance Comparison", fontsize=12, fontweight='bold')
        axes[1].set_ylabel("Scores")
        axes[1].set_xlabel("Students")
        axes[1].set_ylim(0, 100)
        axes[1].legend(loc='upper left')
        axes[1].grid(axis='y', alpha=0.3)
        plt.setp(axes[1].xaxis.get_majorticklabels(), rotation=45, ha='right')
        
        plt.tight_layout()
        print("✓ Visualizations generated successfully!")
        plt.show()
        
    except Exception as e:
        print(f"Error generating visualizations: {e}")
        print("Note: Matplotlib requires display support.")
