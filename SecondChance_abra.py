def findAndUpdate(x, arr, second_chance, frames):    
    for i in range(frames):
        if arr[i] == x:
            second_chance[i] = True
            return True
    return False

def replaceAndUpdate(x, arr, second_chance, frames, pointer):
    while(True):
        if not second_chance[pointer]:
            arr[pointer] = x
            return (pointer+1)%frames
        second_chance[pointer] = False
        pointer = (pointer + 1) % frames

def printHitsAndFaults(reference_string, frames):
    pointer = 0
    pf = 0
    arr = [-1]*frames
    second_chance = [False]*frames
    reference = reference_string.split(' ')
    
    # Print table header
    print(f"\nSC {frames} | Hiba {len(reference)}")
    print("-"*50)
    
    # Print reference row
    print("| Reference |", " | ".join(reference), "|")
    print("|-----------|" + "|".join(["-"*4 for _ in range(len(reference))]) + "|")
    
    # Initialize frame rows
    frame_rows = [[] for _ in range(frames)]
    sc_rows = []
    action_rows = []
    
    for i, x in enumerate(reference):
        action = ""
        if not findAndUpdate(x, arr, second_chance, frames):
            old_page = arr[pointer]
            pointer = replaceAndUpdate(x, arr, second_chance, frames, pointer)
            pf += 1
            action = f"{old_page} cseréje" if old_page != -1 else f"{x} betöltés"
        else:
            action = "Hit"
        
        # Record current state
        for f in range(frames):
            frame_rows[f].append(str(arr[f]) if arr[f] != -1 else "-")
        sc_rows.append(str(second_chance.copy()))
        action_rows.append(action)
    
    # Print frame rows
    for f in range(frames):
        print(f"| Frame {f+1}   |", " | ".join(frame_rows[f]), "|")
    
    # Print SC bits row
    print("| SC Bits   |", " | ".join(sc_rows), "|")
    
    # Print action row
    print("| Action    |", " | ".join(action_rows), "|")
    
    print("\nTotal page faults:", pf)

# Test cases
reference_string = "1 2 3 4 0 2 5 1 2 3 4 5 1 2"

print("Second Chance Page Replacement Algorithm Results")
print("="*60)

# Test 1
print("\nTest Case 1: 3 Frames")
printHitsAndFaults(reference_string, 3)

# Test 2
print("\nTest Case 2: 4 Frames")
printHitsAndFaults(reference_string, 4)