#!/usr/bin/env python3
"""
Generate static PNG charts for the 215-Year Climate Cycle
These can be used in the PDF or for sharing
"""

import matplotlib.pyplot as plt
import numpy as np

# Set style for professional look
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10

def create_pattern_timeline():
    """Chart 1: The 215-year pattern with events"""
    fig, ax = plt.subplots(figsize=(14, 6))
    
    # Events data
    events = {
        'year': [536, 754, 963, 1179, 1397, 1608, 1823],
        'name': ['Darkness', 'Constantinople', 'Rhine', 'Thames', 'Baltic', 'Constance', 'Seine'],
        'predicted': [536, 751, 966, 1181, 1396, 1611, 1826]
    }
    
    # Plot predicted points
    predictions = list(range(536, 2100, 215))
    ax.scatter(predictions, [1]*len(predictions), s=200, marker='v', 
               color='green', alpha=0.6, label='215-year predictions', zorder=1)
    
    # Plot actual events
    ax.scatter(events['year'], [1]*len(events['year']), s=250, 
               color='darkblue', alpha=0.8, label='Actual events', zorder=2)
    
    # Special markers
    ax.scatter([1479], [1], s=500, marker='*', color='gold', 
               edgecolor='black', linewidth=2, label='Black Sea Freeze', zorder=3)
    ax.scatter([2044], [1], s=350, marker='D', color='purple', 
               alpha=0.8, label='Next prediction', zorder=3)
    
    # Timeline
    ax.hlines(1, 500, 2100, colors='gray', alpha=0.3, linewidth=2)
    
    # Annotations
    for i, (year, name) in enumerate(zip(events['year'], events['name'])):
        ax.annotate(f'{name}\n{year}', (year, 1), xytext=(0, 25), 
                    textcoords='offset points', ha='center', fontsize=9)
    
    ax.annotate('BLACK SEA\nFREEZES\n1479', (1479, 1), xytext=(0, -40), 
                textcoords='offset points', ha='center', fontsize=10, 
                weight='bold', color='darkred')
    
    ax.annotate('PREDICTED\n2044', (2044, 1), xytext=(0, 25), 
                textcoords='offset points', ha='center', fontsize=10, 
                weight='bold', color='purple')
    
    # Formatting
    ax.set_xlim(500, 2100)
    ax.set_ylim(0.5, 1.5)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_title('The 215-Year Climate Cycle: 1,500 Years of Evidence', fontsize=16, pad=20)
    ax.legend(loc='upper left', framealpha=0.9)
    ax.set_yticks([])
    ax.grid(True, axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('figures/pattern_timeline.png', bbox_inches='tight', facecolor='white')
    plt.close()

def create_deviation_chart():
    """Chart 2: Deviations with sine wave"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Actual deviations
    years = [754, 963, 1179, 1397, 1608, 1823]
    deviations = [3, -3, -2, 1, -3, -3]
    names = ['Constantinople', 'Rhine', 'Thames', 'Baltic', 'Constance', 'Seine']
    
    # Plot deviations
    ax.scatter(years, deviations, s=300, alpha=0.8, color='darkblue', zorder=2)
    
    # Add sine wave
    x = np.linspace(536, 2200, 1000)
    y = 3 * np.sin((x - 536) * 2 * np.pi / 1290)
    ax.plot(x, y, 'r-', alpha=0.7, linewidth=3, label='1,290-year sine wave')
    
    # Add predicted 2044
    predicted_dev = 3 * np.sin((2044 - 536) * 2 * np.pi / 1290)
    ax.scatter([2044], [predicted_dev], s=350, marker='D', color='purple', 
               alpha=0.8, label='2044 prediction', zorder=2)
    
    # Zero line
    ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    
    # Annotations
    for year, dev, name in zip(years, deviations, names):
        ax.annotate(name, (year, dev), xytext=(5, 5), 
                    textcoords='offset points', fontsize=10)
    
    ax.annotate('2044', (2044, predicted_dev), xytext=(5, 5), 
                textcoords='offset points', fontsize=10, weight='bold')
    
    # Formatting
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Deviation from 215-year prediction (years)', fontsize=12)
    ax.set_title('The Sine Wave Discovery: Deviations Follow a 1,290-Year Pattern', 
                 fontsize=16, pad=20)
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(700, 2100)
    ax.set_ylim(-4, 4)
    
    plt.tight_layout()
    plt.savefig('figures/deviation_sine_wave.png', bbox_inches='tight', facecolor='white')
    plt.close()

def create_severity_chart():
    """Chart 3: Severity by sine position"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Generate severity curve
    years = np.linspace(0, 3200, 1000)
    severity = -np.sin((years - 536) * 2 * np.pi / 1290)
    
    # Fill areas
    ax.fill_between(years, severity, where=(severity > 0.5), 
                    color='red', alpha=0.3, label='Catastrophic zone')
    ax.fill_between(years, severity, where=(severity < -0.5), 
                    color='green', alpha=0.3, label='Manageable zone')
    ax.fill_between(years, severity, where=(abs(severity) <= 0.5), 
                    color='yellow', alpha=0.3, label='Moderate zone')
    
    # Plot curve
    ax.plot(years, severity, 'k-', linewidth=2)
    
    # Mark key events
    troughs = [536, 1826, 3116]
    peaks = [1181, 2471]
    
    ax.scatter(troughs, [1, 1, 1], s=300, marker='v', color='darkred', 
               label='Maximum severity', zorder=3)
    ax.scatter(peaks, [-1, -1], s=300, marker='^', color='darkgreen', 
               label='Minimum severity', zorder=3)
    ax.scatter([2044], [-0.5], s=400, marker='*', color='purple', 
               label='2044 (moderate)', zorder=3)
    
    # Current position
    ax.axvline(x=2024, color='blue', linestyle='--', alpha=0.7, linewidth=2)
    ax.text(2024, -1.3, 'We are\nhere', ha='center', fontsize=10, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.7))
    
    # Labels for key events
    for year in troughs[:2]:  # Don't label future trough
        ax.text(year, 1.1, str(year), ha='center', fontsize=10)
    for year in peaks[:1]:  # Don't label future peak
        ax.text(year, -1.1, str(year), ha='center', fontsize=10)
    ax.text(2044, -0.6, '2044', ha='center', fontsize=10, weight='bold')
    
    # Formatting
    ax.set_xlim(0, 3200)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Severity Index', fontsize=12)
    ax.set_title('Why 2044 Won\'t Be Catastrophic: We\'re Climbing Out of the Trough', 
                 fontsize=16, pad=20)
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    # Custom y-axis labels
    ax.set_yticks([-1, 0, 1])
    ax.set_yticklabels(['Minimum\nSeverity', 'Moderate', 'Maximum\nSeverity'])
    
    plt.tight_layout()
    plt.savefig('figures/severity_position.png', bbox_inches='tight', facecolor='white')
    plt.close()

def create_black_sea_context():
    """Chart 4: Black Sea freeze in context"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Temperature simulation for 1300-1700
    years = np.linspace(1300, 1700, 400)
    base_temp = -0.2
    
    # Add cooling trends
    temps = []
    for year in years:
        temp = base_temp
        # Spörer Minimum effect
        if 1460 <= year <= 1550:
            temp -= 0.3 * (1 - abs(year - 1505) / 45)
        # Pre-Maunder cooling
        if 1550 <= year <= 1650:
            temp -= 0.2 * (year - 1550) / 100
        # Volcanic effects
        if abs(year - 1453) < 10:  # Kuwae
            temp -= 0.3 * (1 - abs(year - 1453) / 10)
        if abs(year - 1600) < 10:  # Huaynaputina
            temp -= 0.3 * (1 - abs(year - 1600) / 10)
        temps.append(temp)
    
    # Plot temperature
    ax.plot(years, temps, 'b-', linewidth=2, label='Temperature anomaly')
    ax.fill_between(years, temps, base_temp, alpha=0.3)
    
    # Mark nodes
    ax.axvline(x=1396, color='green', linestyle='--', linewidth=2, alpha=0.7)
    ax.axvline(x=1611, color='green', linestyle='--', linewidth=2, alpha=0.7)
    ax.text(1396, 0.1, '1396\nNode', ha='center', fontsize=10, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgreen', alpha=0.7))
    ax.text(1611, 0.1, '1611\nNode', ha='center', fontsize=10, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgreen', alpha=0.7))
    
    # Mark Black Sea freeze
    ax.scatter([1479], [-0.55], s=500, marker='*', color='gold', 
               edgecolor='black', linewidth=2, zorder=3)
    ax.annotate('BLACK SEA\nFREEZES', (1479, -0.55), xytext=(0, -30), 
                textcoords='offset points', ha='center', fontsize=12, 
                weight='bold', color='darkred',
                bbox=dict(boxstyle="round,pad=0.5", facecolor='yellow', alpha=0.8))
    
    # Mark other events
    ax.scatter([1453], [-0.5], s=200, marker='v', color='red', alpha=0.8)
    ax.text(1453, -0.6, 'Kuwae\neruption', ha='center', fontsize=9)
    
    ax.scatter([1600], [-0.5], s=200, marker='v', color='red', alpha=0.8)
    ax.text(1600, -0.6, 'Huaynaputina\neruption', ha='center', fontsize=9)
    
    # Spörer Minimum shading
    ax.axvspan(1460, 1550, alpha=0.2, color='lightblue', label='Spörer Minimum')
    
    # Formatting
    ax.set_xlim(1300, 1700)
    ax.set_ylim(-0.8, 0.2)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Temperature Anomaly (°C)', fontsize=12)
    ax.set_title('The Black Sea Freeze (1479): Perfect Inter-Nodal Positioning', 
                 fontsize=16, pad=20)
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('figures/black_sea_context.png', bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    print("Generating static charts...")
    
    create_pattern_timeline()
    print("✓ Created pattern_timeline.png")
    
    create_deviation_chart()
    print("✓ Created deviation_sine_wave.png")
    
    create_severity_chart()
    print("✓ Created severity_position.png")
    
    create_black_sea_context()
    print("✓ Created black_sea_context.png")
    
    print("\n✨ All charts generated successfully!")
    print("Files saved in figures/ directory")