'''
U: Nested Dictionary "name" is a string, "criteria" is a list, return the name with correct input criteria
    Edge case 1: typo return a empty list
    Edge case 2: empty input returns a empty list

P: loop through brands, check criteria for matches, append the name to a list

I:
'''


def filter_sustainable_brands(brands, criterion):
    result = []
    if not brands or criterion == "":
        return result
    else:
        for brand in brands:
            if "criteria" in brand and criterion in brand["criteria"]: 
                result.append(brand["name"])
        return result



brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]

print(filter_sustainable_brands(brands, "eco-friendly"))
print(filter_sustainable_brands(brands_2, "ethical labor"))
print(filter_sustainable_brands(brands_3, "carbon-neutral"))