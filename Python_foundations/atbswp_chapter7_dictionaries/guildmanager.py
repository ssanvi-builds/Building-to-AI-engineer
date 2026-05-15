guild = {
      'patrol_alpha': {
          'members': {
              'Aria': {'class': 'mage', 'level': 12, 'inventory': {'potion': 3,
  'fire_scroll': 2, 'staff': 1}},
              'Bram': {'class': 'warrior', 'level': 10, 'inventory': {'potion': 1, 'sword':
  1, 'shield': 1}},
              'Cira': {'class': 'healer', 'level': 11, 'inventory': {'potion': 5,
  'heal_scroll': 3}}
          },
          'quest': 'dark_dragon'
      },
      'patrol_beta': {
          'members': {
              'Drek': {'class': 'warrior', 'level': 8, 'inventory': {'sword': 1, 'potion':
  2}},
              'Elara': {'class': 'mage', 'level': 9, 'inventory': {'ice_scroll': 4,
  'potion': 1}}
          },
          'quest': None
      }
  }

"""
Function inventory_summary(adventurer) — takes an adventurer dictionary (like Aria's)
and returns a string with the total number of items they carry. Example: "Aria carries 6
items"
"""

def inventory_summary(adventurer): # The parameter passed to the function is the adventurer dictionary
    total_items = 0
    for item in adventurer['inventory'].values():
        total_items += item
    print(f'This adventurer carries {total_items} items.')

inventory_summary(guild['patrol_alpha']['members']['Cira'])
inventory_summary(guild['patrol_alpha']['members']['Aria'])
inventory_summary(guild['patrol_beta']['members']['Drek'])


"""
Function patrol_level(patrol) — takes a patrol dictionary and returns the average level
of its members (as an integer, use int())
"""

def patrol_level(patrol):
    levels = 0
    for member in patrol['members'].values(): # Here member is the complete path to the specific member dictionary 
        levels += member['level'] # So I can just access its keys
    average_level = levels / len(patrol['members'])
    print(f'The average level of the patrol is {int(average_level)}.')

patrol_level(guild['patrol_alpha'])
patrol_level(guild['patrol_beta'])

"""
Function find_by_class(guild, class) — returns a list of names of all adventurers in
the guild that match the given class. Example: find_by_class(guild, 'mage') → ['Aria',
'Elara']
"""

def find_by_class(guild, memberclass): # Cannot use class because it is a Python keyword
    members_class = []
    for patrol, patrol_data in guild.items():
         for member, member_data in patrol_data['members'].items():
            if member_data['class'] == memberclass:
                members_class.append(member)
    return members_class


find_by_class(guild, 'mage')
find_by_class(guild, 'warrior')
find_by_class(guild, 'healer')

"""
Function total_resource(guild, resource) — returns the total amount of a specific
resource across the entire guild. Example: total_resource(guild, 'potion') → 12
"""
def total_resource(guild, resource):
    resource_count = 0
    for patrol, patrol_data in guild.items():
        for member, member_data in patrol_data['members'].items():
            resource_count += member_data['inventory'].get(resource, 0)
    return resource_count

total_resource(guild, 'potion')
total_resource(guild, 'sword')

"""
Function patrol_ready(patrol) — returns True if all members of the patrol are level 10
or higher, False otherwise
"""

def patrol_ready(patrol):
    for member, member_data in patrol['members'].items():
        if member_data['level'] < 10:
            return False
    return True