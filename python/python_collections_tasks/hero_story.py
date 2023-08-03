# hero story

"""
Story beginning:

Next time it's beautifully sunny in your area, watch out for LAUNDRY MAN! dada da da daaaaa!
Laundry man has the superpower of making sure clothes out on the line dry really fast on a good drying day.
He can also make sure you remember to get your washing done and make the most of the nice weather, because he knows you live in Scotland and you only realistically get a handful of days like that per year.

Story middle:

On this particular day in June, it was an absolute belter of a day. Those lucky enough to have a 15min wash setting on their washing machines could expect to get half a dozen loads of laundry done and hung out to dry in batches.
However, DISASTER! The MET Office releases a severe weather warning for thunderstorms nationwide! OH NO! What will we do? I've just put out my second load of towels on the whirlygig!
This looks like a job for... LAUNDRY MAN!

Story end:

Laundry man, ever courageous and fully committed to the preservation of good drying days, flew so fast he left earth's atmosphere. He then flew to the sun and brought it just a tiny wee bit closer to the earth. This dispelled the pressure and the gathering clouds.
Hurray! We are all saved! We can get the rest of our laundry out to dry today! Thank you Laundry Man!
He says, "All in a day's work - a drying day's work!
THE END
(Please note: I am not a meteorologist and have no idea if bringing the sun slightly closer to the earth would stop a highly localised weather event.)

"""

story_1 = {
    "story_beginning" : "Next time it's beautifully sunny in your area, watch out for LAUNDRY MAN! dada da da daaaaa! \nLaundry man has the superpower of making sure clothes out on the line dry really fast on a good drying day. \nHe can also make sure you remember to get your washing done and make the most of the nice weather, because he knows you live in Scotland and you only realistically get a handful of days like that per year.",
    "story_middle" : "On this particular day in June, it was an absolute belter of a day. Those lucky enough to have a 15min wash setting on their washing machines could expect to get half a dozen loads of laundry done and hung out to dry in batches.\nHowever, DISASTER! The MET Office releases a severe weather warning for thunderstorms nationwide! \nOH NO! What will we do? I have just put out my second load of towels on the whirlygig!\nThis looks like a job for... LAUNDRY MAN!",
    "story_end" : "Laundry man, ever courageous and fully committed to the preservation of good drying days, flew so fast he left the atmosphere. He then flew to the sun and brought it just a tiny wee bit closer to the earth. This dispelled the pressure and the gathering clouds.\nHurray! We are all saved! We can get the rest of our laundry out to dry today! Thank you Laundry Man!\nHe says All in a days work - a drying days work! \nTHE END\nPlease note: I am not a meteorologist and have no idea if bringing the sun slightly closer to the earth would stop a highly localised weather event."
}

print(story_1)
print(type(story_1))
print(story_1.keys())
print(story_1.values())
print("\n")
print(story_1["story_beginning"])
print("\n")
print(story_1["story_middle"])
print("\n")
print(story_1["story_end"])
print("\n")
story_1.update({"my_super_hero": "laundry man"})
print(story_1)
print(*story_1, sep="\n")