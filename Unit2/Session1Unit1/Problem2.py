def can_trust_message(message):
    '''
    U:
    P:
    I:
    '''
    a = set()  # Use a set to store unique letters
    for char in message.lower():  # Convert to lowercase for case insensitivity
        if char.isalpha():  # Only consider alphabetic characters (ignore spaces, punctuation, etc.)
            a.add(char)
    return len(a) == 26  # Return True if we have all 26 letters, False otherwise



message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))