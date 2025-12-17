#!/usr/bin/env python3
"""
Calculate progress metrics across multiple index files.
"""

import re
from pathlib import Path


def analyze_research_queue(file_path):
    """Calculate the percentage of resolved research items."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all status lines
    status_pattern = r'\*\*Status:\*\*\s*`([^`]+)`'
    statuses = re.findall(status_pattern, content)

    if not statuses:
        return None

    total_items = len(statuses)
    resolved_items = sum(1 for status in statuses if status == 'resolved')
    in_progress_items = sum(1 for status in statuses if status == 'in-progress')
    open_items = sum(1 for status in statuses if status == 'open')

    return {
        'total': total_items,
        'resolved': resolved_items,
        'in_progress': in_progress_items,
        'open': open_items,
    }


def analyze_confidence_file(file_path):
    """Calculate the percentage of CERTAIN items in places/quotes indexes."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all confidence lines
    confidence_pattern = r'\*\*Confidence:\*\*\s*`([^`]+)`'
    confidences = re.findall(confidence_pattern, content)

    if not confidences:
        return None

    total_items = len(confidences)
    certain_items = sum(1 for conf in confidences if conf == 'CERTAIN')
    likely_items = sum(1 for conf in confidences if conf == 'LIKELY')
    maybe_items = sum(1 for conf in confidences if conf == 'MAYBE')

    return {
        'total': total_items,
        'certain': certain_items,
        'likely': likely_items,
        'maybe': maybe_items,
    }


def print_summary(title, data, primary_metric, primary_label):
    """Print a formatted summary for a file."""
    print(f"\n{title}")
    print(f"=" * 50)
    print(f"Total items:       {data['total']:>4}")

    primary_count = data[primary_metric]
    primary_percentage = (primary_count / data['total'] * 100) if data['total'] > 0 else 0
    print(f"{primary_label:18} {primary_count:>4} ({primary_percentage:>5.1f}%)")

    # Print other metrics
    for key, value in data.items():
        if key not in ['total', primary_metric]:
            percentage = (value / data['total'] * 100) if data['total'] > 0 else 0
            label = key.replace('_', ' ').capitalize() + ':'
            print(f"{label:18} {value:>4} ({percentage:>5.1f}%)")


if __name__ == '__main__':
    indexes_dir = Path(__file__).parent / 'Indexes'

    # Analyze research queue
    research_queue_path = indexes_dir / 'research_queue.md'
    queue_data = analyze_research_queue(research_queue_path)
    if queue_data:
        total = queue_data['total']
        print(f"\nResearch Queue (research_queue.md)")
        print(f"=" * 50)
        print(f"Open:          {queue_data['open']:>3}/{total} ({queue_data['open']/total*100:>5.1f}%)")
        print(f"In progress:   {queue_data['in_progress']:>3}/{total} ({queue_data['in_progress']/total*100:>5.1f}%)")
        print(f"Resolved:      {queue_data['resolved']:>3}/{total} ({queue_data['resolved']/total*100:>5.1f}%)")

    # Analyze places
    places_path = indexes_dir / 'places.md'
    places_data = analyze_confidence_file(places_path)
    if places_data:
        total = places_data['total']
        print(f"\nPlaces Index (places.md)")
        print(f"=" * 50)
        print(f"Maybe:         {places_data['maybe']:>3}/{total} ({places_data['maybe']/total*100:>5.1f}%)")
        print(f"Likely:        {places_data['likely']:>3}/{total} ({places_data['likely']/total*100:>5.1f}%)")
        print(f"Certain:       {places_data['certain']:>3}/{total} ({places_data['certain']/total*100:>5.1f}%)")

    # Analyze quotes
    quotes_path = indexes_dir / 'quotes.md'
    quotes_data = analyze_confidence_file(quotes_path)
    if quotes_data:
        total = quotes_data['total']
        print(f"\nQuotes & Allusions (quotes.md)")
        print(f"=" * 50)
        print(f"Maybe:         {quotes_data['maybe']:>3}/{total} ({quotes_data['maybe']/total*100:>5.1f}%)")
        print(f"Likely:        {quotes_data['likely']:>3}/{total} ({quotes_data['likely']/total*100:>5.1f}%)")
        print(f"Certain:       {quotes_data['certain']:>3}/{total} ({quotes_data['certain']/total*100:>5.1f}%)")

    # Overall summary
    if queue_data and places_data and quotes_data:
        total_resolved = queue_data['resolved']
        total_certain = places_data['certain'] + quotes_data['certain']
        total_items = queue_data['total'] + places_data['total'] + quotes_data['total']
        total_high_conf = total_resolved + total_certain
        overall_percentage = (total_high_conf / total_items * 100) if total_items > 0 else 0
        print(f"\n{'=' * 50}")
        print(f"Overall: {total_high_conf}/{total_items} ({overall_percentage:>5.1f}%) resolved/certain")
        print(f"=" * 50)
