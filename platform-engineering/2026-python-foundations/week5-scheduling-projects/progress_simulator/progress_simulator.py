#!/usr/bin/env python3
'''Deployment Simulator with Progress Bar and Timer.
Simulates a long deployment process with visual feedback.'''

import time, sys, random

BAR = chr(9608)  # █

def show_progress_bar(progress, total, bar_width=40):
    '''Displays a progress bar.'''
    percent = (progress / total) * 100
    filled = int(bar_width * progress / total)
    bar = BAR * filled + ' ' * (bar_width - filled)
    return f'[{bar}] {percent:.1f}% ({progress}/{total})'

def countdown(seconds):
    '''Simple countdown timer.'''
    for i in range(seconds, 0, -1):
        print(f'\r Waiting {i} seconds...', end='', flush=True)
        time.sleep(1)
    print('\r Ready!            ')
    
def simulate_deployment():
    '''Simulates a multi-step deployment.'''
    steps = [
        (" Checking dependencies...", 30),
        (" Installing packages...", 50),
        (" Configuring services...", 40),
        (" Deploying application...", 60),
        (" Finalizing...", 20)
    ]
    
    print("\n DEPLOYMENT SIMULATOR\n")
    
    # Countdown before starting
    countdown(3)
    
    total_steps = len(steps)
    for step_num, (description, duration) in enumerate(steps, 1):
        print(f'\nStep {step_num}/{total_steps}: {description}')
        
        for i in range(duration + 1):
            bar = show_progress_bar(i, duration)
            print(f'\r {bar}', end='', flush=True)
            time.sleep(0.1)
            
        print() # New line after each step
        time.sleep(0.5) 
        
    print("\n" + "="*50)
    print(" DEPLOYMENT COMPLETED SUCCESSFULLY! ")
    print("="*50)
    
if __name__ == "__main__":
    try:
        simulate_deployment()
    except KeyboardInterrupt:
        print("\n\n Deployment cancelled by user.")
        sys.exit(1)
