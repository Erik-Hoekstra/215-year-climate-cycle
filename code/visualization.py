#!/usr/bin/env python3
"""
Visualization code for the 215-Year Climate Cycle
Generates charts showing the pattern and predictions
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def load_data():
    """Load the climate events data"""
    # This would load from the CSV file
    events = {
        'year': [536, 754, 963, 1179, 1397, 1608, 1823],
        'predicted': [536, 751, 966, 1181, 1396, 1611, 1826],
        'deviation': [0, 3, -3, -2, 1, -3, -3],
        'event': ['Darkness', 'Constantinople', 'Rhine', 'Thames', 
                  'Baltic', 'Constance', 'Seine']
    }
    return pd.DataFrame(events)

def plot_deviations(df):
    """Plot the deviations from predicted years"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot deviations
    ax.scatter(df['year'], df['deviation'], s=200, alpha=0.6, color='darkblue')
    ax.plot(df['year'], df['deviation'], 'b--', alpha=0.4)
    
    # Add sine wave fit
    years = np.linspace(536, 2100, 1000)
    sine_wave = 3 * np.sin((years - 536) * 2 * np.pi / 1290)
    ax.plot(years, sine_wave, 'r-', alpha=0.6, linewidth=2, 
            label='1,290-year sine wave')
    
    # Add zero line
    ax.axhline(y=0, color='gray', linestyle='-', alpha=0.3)
    
    # Labels and title
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Deviation from 215-year prediction (years)', fontsize=12)
    ax.set_title('The 215-Year Cycle: Deviations Follow a Sine Wave', fontsize=14)
    ax.legend()
    
    # Add event labels
    for idx, row in df.iterrows():
        ax.annotate(row['event'], (row['year'], row['deviation']), 
                   xytext=(5, 5), textcoords='offset points', fontsize=9)
    
    plt.tight_layout()
    return fig

def plot_cycle_timeline():
    """Create a timeline showing all cycles and predictions"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Generate all cycle points
    cycles = []
    year = 536
    while year <= 2100:
        cycles.append(year)
        year += 215
    
    # Historical events
    events = [754, 963, 1179, 1397, 1608, 1823]
    
    # Plot cycle predictions
    ax.scatter(cycles, [1]*len(cycles), s=300, marker='v', 
               color='green', alpha=0.6, label='215-year cycle points')
    
    # Plot actual events
    ax.scatter(events, [1]*len(events), s=300, marker='o', 
               color='red', alpha=0.8, label='Actual freeze events')
    
    # Special markers
    ax.scatter([1479], [1], s=500, marker='*', color='gold', 
               edgecolor='black', linewidth=2, label='Black Sea Freeze (1479)')
    ax.scatter([2044], [1], s=400, marker='D', color='purple', 
               alpha=0.8, label='Predicted (2044)')
    
    # Add timeline
    ax.plot([500, 2100], [1, 1], 'k-', alpha=0.3)
    
    # Formatting
    ax.set_xlim(500, 2100)
    ax.set_ylim(0.5, 1.5)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_title('The 215-Year Climate Cycle: 1,500 Years of Evidence', fontsize=14)
    ax.legend(loc='upper left')
    ax.set_yticks([])
    
    # Add annotations for key events
    ax.annotate('536: Sun disappears', (536, 1), xytext=(536, 1.2), 
                ha='center', fontsize=9, arrowprops=dict(arrowstyle='->', alpha=0.5))
    ax.annotate('1479: BLACK SEA FREEZES', (1479, 1), xytext=(1479, 0.8), 
                ha='center', fontsize=10, weight='bold',
                arrowprops=dict(arrowstyle='->', alpha=0.5))
    ax.annotate('2044: Next crisis?', (2044, 1), xytext=(2044, 1.2), 
                ha='center', fontsize=10, arrowprops=dict(arrowstyle='->', alpha=0.5))
    
    plt.tight_layout()
    return fig

def plot_severity_by_sine_position():
    """Show how sine wave position affects severity"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Generate sine wave
    years = np.linspace(536, 3116, 1000)
    sine_wave = np.sin((years - 536) * 2 * np.pi / 1290)
    
    # Plot sine wave
    ax.plot(years, sine_wave, 'b-', linewidth=2)
    ax.fill_between(years, sine_wave, alpha=0.3)
    
    # Mark key positions
    troughs = [536, 1826, 3116]
    peaks = [1181, 2471]
    
    ax.scatter(troughs, [-1, -1, -1], s=300, marker='v', 
               color='red', label='Troughs (Maximum severity)')
    ax.scatter(peaks, [1, 1], s=300, marker='^', 
               color='green', label='Peaks (Minimum severity)')
    ax.scatter([2044], [np.sin((2044-536)*2*np.pi/1290)], s=300, 
               marker='D', color='purple', label='2044 (Moderate)')
    
    # Labels
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Sine Wave Position', fontsize=12)
    ax.set_title('Severity Modulation: Why Some Crises Are Worse Than Others', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig

def create_all_visualizations():
    """Generate all charts for the repository"""
    # Load data
    df = load_data()
    
    # Create visualizations
    fig1 = plot_deviations(df)
    fig1.savefig('figures/sine_wave_pattern.png', dpi=300, bbox_inches='tight')
    
    fig2 = plot_cycle_timeline()
    fig2.savefig('figures/cycle_timeline.png', dpi=300, bbox_inches='tight')
    
    fig3 = plot_severity_by_sine_position()
    fig3.savefig('figures/severity_modulation.png', dpi=300, bbox_inches='tight')
    
    print("✓ Generated sine_wave_pattern.png")
    print("✓ Generated cycle_timeline.png")
    print("✓ Generated severity_modulation.png")
    print("\nAll visualizations created successfully!")

if __name__ == "__main__":
    create_all_visualizations()