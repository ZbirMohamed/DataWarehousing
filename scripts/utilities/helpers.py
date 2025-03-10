import random

def add_noise(country:str):
    
    noise_types = ['space', 'special_char', 'uppercase', 'lowercase', 'mixed_case', 'repeated_char']
    noise_type = random.choice(noise_types)

    if noise_type == 'space':
        idx = random.randint(0, len(country))
        return country[:idx] + ' ' + country[idx:]
    
    elif noise_type == 'special_char':
        special_chars = ['@', '#', '$', '%', '&', '!', '*']
        idx = random.randint(0, len(country))
        return country[:idx] + random.choice(special_chars) + country[idx:]
    
    elif noise_type == 'uppercase':
        return country.upper()
    
    elif noise_type == 'lowercase':
        return country.lower()
    
    elif noise_type == 'mixed_case':
        return ''.join(random.choice([char.upper(), char.lower()]) for char in country)
    
    elif noise_type == 'repeated_char':
        idx = random.randint(0, len(country)-1)
        char = country[idx]
        return country[:idx] + char*random.randint(2, 4) + country[idx+1:]
    
    return country
