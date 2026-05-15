### Insight 5

Looping over dictionaries can be done throughpout their keys or their keys and values. The project is done using .items() which unpacks every pair of key and values of that partiular dictionary. Then, we loop over the keys and their values which can also be dictionaries. To access a particular value we will need to do it from the value of the current dictionary:

``` 
def find_by_class(guild, memberclass):
    members_class = []
    for patrol, patrol_data in guild.items():
         for member, member_data in patrol_data['members'].items():
            if member_data['class'] == memberclass:
                members_class.append(member)
    return members_class
```

In the example above, patrol stores the names or keys of the guild dictionaries while patrol_data holds the values of those particular keys, which can and indeed are dictionaries. Therefore, to access the dictionary members, we'll iterate over the different member dictionaries or keys, to access their values.

If we did this using only keys the code would look as follows.

````
def find_by_class(guild, memberclass):
    members_class = []
    for patrol in guild:
        for member in guild[patrol]['members']:
            if guild[patrol]['members'][member]['class'] == memberclass:
            members_class.append(member)
    return members_class
````

The key (no pun intended) is that accesing the keys of a dictionary we get a string. To access values, we must index back into the dictionary using those strings. With .items(), we unpack both the key and value directly, avoiding the need to re-index.

### Insight 6

Return inside a function acts as break, so when one condition is reach we can just use:

````
for i in list:
    if condition:
        return False
return True    
````
and it will automatically get out of the function. If the conditin is not met, the loop continues to the next iteration. Only after all iterations complete without triggering return False does the function reach return True. 