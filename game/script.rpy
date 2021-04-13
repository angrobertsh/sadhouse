label splashscreen:
    play sound "audio/A Noble Charade theme MIX_2.mp3"
    scene black
    with Pause(1)

    show text "Rachel Company presents..." with dissolve
    with Pause(1)

    hide text with dissolve
    with Pause(1)

    return

# Qualities/attributes
default carpenter = False
default tutor = False
default merchant = False
default mood = 0
default likes_alcohol = False

# Explored
default explored_kitchen = False
default explored_lounge_piano = False
default explored_lounge_window = False
default explored_lounge_chair = False
default explored_dining_room_dining_table_sit = False
default explored_dining_room_dining_room_dining_trappings = False
default explored_dining_room_dining_room_painting = False
default explored_kitchen_cupboard = False
default explored_kitchen_drawer = False
default explored_kitchen_bar = False
default explored_library_book_1 = False
default explored_library_book_2 = False
default explored_library_book_3 = False
default explored_salon_shelf = False
default explored_salon_painting = False
default explored_salon_shelf_vase = False
default explored_salon_shelf_glove = False
default explored_salon_shelf_picture = False
default explored_conservatory_drawer = False
default explored_gueuloir = False
default explored_study_safe = False
default explored_study_picture = False
default explored_study_papers = False
default explored_study_check = False
default explored_study_check_cult = False
default explored_study_check_drugs = False
default explored_study_check_wishes = False
default explored_bedroom_fanmail = False
# Insight
default insight_1_library_book_1 = False
default insight_2_library_book_1 = False
default insight_3_library_book_1 = False

# Insight - Rory
default rory_jimmy = False
default rory_business_card = False
default rory_artist = False
default rory_choices = False
default rory_atford = False
default rory_travel = False

# Insight - Marian Play
default pasiphae_author = "this unknown author"
default marian_play_fun = False
default marian_play_crazy = False
default marian_play_sympathy = False

# The game starts here.
label start:
    scene main_menu at topleft

    stop sound fadeout 3.0
    with Pause(1)
    scene black with fade
    with Pause(2)

    play sound "audio/telephone_ring.ogg"

    scene black with fade

    "I had received a call in the morning from an unfamiliar voice, while I was..."

    menu:

        "Taking measurements for a new stage to be built in town square.":

            jump intro_carpenter

        "Preparing a general lesson plan of maths problems and written exercises.":

            jump intro_tutor

        "Inspecting a recent shipment of goods from one of my suppliers.":

            jump intro_merchant

label intro_carpenter:
    $ carpenter = True

    "Our little town had come a long way over the years. I remember going to the market as a child, the fruits and vegetables on display next to the butcher's meats."

    "Across the street was the cobbler's, which is now a gourmet cafe. Often, you can find patrons lining up out the door and around the corner, as they did for the ice cream shop that was there before it."

    "The town had begun to sponsor a summer festival and this year, funds had been set aside for a new stage to be built that would accommodate an expanded live entertainment roster."

    "We would need to start building in the cold of winter to finish in time. The winters were now warmer than I had remembered growing up, but cold nevertheless."

    jump attorney

label intro_tutor:
    $ tutor = True

    "My newest pupil was the youngest of three. The parents were doctors, and the family had recently moved into the new Galenwood neighborhood."

    "The outer hills of Atford were now populated with elegant residences that attracted tenants from out of town, all of them seemingy affluent."

    "Not all of the locals were pleased with this development, but I couldn't complain about the increase in clientele."

    "There was talk of incorporating Galenwood into a separate town, which further drew ire."

    "But progress seemed inevitable and there were never any clear signs of protest other than a petition drafted and posted in town square, lost among the bustle of commerce."

    "In the meantime, was education not the means for bettering oneself and fostering change? Perhaps."

    jump attorney

label intro_merchant:
    $ merchant = True

    "I had worked part-time at Bolton's, a local store, while I was still a student. The job involved assisting customers and keeping the shop tidy."

    "Eventually, this led to a full-time position managing inventory and keeping the books. When Mr. Bolton retired, I became the purchaser."

    "Deciding what to keep in stock is both a logical and intuitive decision. No matter how tough times are, people continue to purchase goods--it's simply a matter of which goods."

    jump attorney

label attorney:

    show letter_7 at truecenter
    with dissolve

    "The gentleman on the phone introduced himself as Thomas Lupin, attorney-at-law. I could scarcely fathom what reason a lawyer would have to make my acquaintance."

    "\"Mr. Pryor was a client of mine. I'm sorry to tell you that James has passed away.\""

    "\"He suffered a stroke and unfortunately never recovered. While tragic and untimely, the coroner has determined his passing to be of \'natural cause.\'\""

    hide letter_7
    with dissolve

    "\"Mr. Pryor left behind a will, drafted by myself and notarized as of this morning. In it, he has appointed you the executor of his estate. If you accept, I will make the necessary arrangements.\""

    "Upon hearing this news, a feeling of unease came over me. Truthfully, Jimmy might as well have been dead to me up until that moment. It had been years since we had last spoken or seen each other."

    menu:

        "I'll do it. Please let me know what the next steps are.":

            jump accept

        "I'm afraid I don't understand. What do you mean by \"executor\"?":

            jump ambivalent

        "I haven't spoken to Jimmy in years, I'm not sure what this has to do with me.":

            jump apathetic

label accept:
    $ mood = mood + 1
    "Regardless of the past, Jimmy had been a friend of mine and now he was gone forever. Surely I could take on this responsiblity on account of that."

    "\"Please meet me at my office this afternoon at 3pm. The address is 32 Fairview Drive, Suite B in the Palace Gardens district. We can discuss the details further in person.\""

    jump james_letter

label ambivalent:

    "\"An executor is tasked with handling the distribution of the deceased's assets. All of these must be accounted for and secured.\""

    "\"Any remaining debts will need to be settled and any relevant parties notified of his passing. Though given his stature, it will likely become public knowledge soon enough.\""

    menu:

        "What is the process for handling these tasks? This is all very unfamiliar to me.":

            jump curious

        "This sounds like quite a lot of work, if I'm being honest.":

            jump cautious

label curious:

    "\"Not to worry. If you should accept, I will assist you to the best of my ability. You merely need to adhere to Mr. Pryor's wishes in his will.\""

    "\"The bulk of your efforts will be directed towards locating the aforementioned assets. If any questions arise, please don't hesitate to contact me directly.\""

    menu:

        "If you can provide me with some guidance, I'll do my best.":

            jump diligent

        "Respectfully, I must decline. This seems beyond the scope of reasonable effort.":

            jump do_nothing

label cautious:
    $ mood = mood - 1
    "\"By all means, this will require no small effort on your part. Mr. Pryor has only one property that I know of, but...\""

    menu:

        "(accept)":

            jump circumspect

        "(decline)":

            jump cynical

label diligent:

    "\"Certainly, I'm at your service...\""

    jump james_letter

label do_nothing:

    "\"I see, and I thank you for your time.\""

    jump mean_ending

label apathetic:

    "\"Be that as it may, Mr. Pryor named you rather than any other relative or beneficiary. He asked me to put this in writing about three years ago from this date.\""

    "\"Of course, you are not obligated to accept. You may choose not to act as Mr. Pryor's executor if you so wish. But I might add that you will be compensated for your efforts.\""

    menu:

        "All right, let's see what this is about.":

            jump beholder

        "I understand, and I'd prefer not to be involved.":

            jump bystander

label circumspect:

    "\"I hope I was able to (answer your questions)\""

    jump james_letter

label cynical:

    "\"I understand if...\""

    jump neutral_ending

label beholder:

    "\"Perhaps it may become clearer if we're to meet and further discuss...\""

    jump james_letter

label bystander:

    "\"Very well, and I'm sorry to have disturbed you. I wish you good day.\""

    jump mean_ending

label short_ending:

    "Jim. Jimmy. James. That was a lifetime ago. I don't know why he thought of me, but there's been a mistake."

    menu:

        "He's no longer a part of my life.":

            jump neutral_ending

        "He can get someone else to clean up his mess.":

            jump mean_ending

label neutral_ending:

    scene black

    "Jimmy Pryor. Haven't heard that name in a while, didn't think I would again."

    return

label mean_ending:

    scene black

    "I want nothing to do with him."

    return

label james_letter:

    scene letters_6

    "To my old friend."
    "Thomas tells me I need to plan for when I'm gone..."

    "Palace Gardens is a fine place to live."

    "Perhaps you'll visit one day."

    # TODO this letter is unfinished

    scene stephen_king_mansion at truecenter

    "It looks like I've just arrived. It's the only mansion among all of these houses, so it's difficult to miss but I almost passed it by, being my first time here."

    "The gate creaks open slowly..."

    menu:

        "As if to speak of an untold history waiting to be discovered.":

            jump optimistic_house

        "Ominously, to forebode those who would enter.":

            jump pessimistic_house

label optimistic_house:
    $ mood = mood + 1

    "The front yard is trim and well-kept and in the midst of neatly manicured bushes. I take in the serene lull of peace and seclusion."

    jump front_door

label pessimistic_house:
    $ mood = mood - 1

    "It becomes eerily quiet once I've moved away from the street."

    jump front_door

label front_door:

    "I walk up to the front door and I reach in my pocket for the key, provided by Mr. Lupin along with a written copy of Jimmy's last instructions."

    "It unlocks easily enough."

label hallway_menu:

    scene stephen_king_hall at truecenter

    "When I enter, I feel warmth on my skin."

    "The home is colored with cream tones and wood. There is room to spread my arms."

    "But the absence of habitation is felt."

    "Dust swirls in sunlight cast through the landing window. The scent of wood in the air faintly musky."

    "In better times, this home would have been easy to build a life in."

    "To my right is the lounge. It seems a good a place to begin as any."

label lounge:

    scene piano living room at truecenter

    "This was where he would have received his many distinguished guests."

    "The grand piano is what immediately draws the eye."

    "I open a curtain, revealing a French door that offers a view into a garden patio."

label lounge_menu:

    menu:

        "I examine the piano" if not explored_lounge_piano:

            jump lounge_piano

        "I gaze out the window" if not explored_lounge_window:

            jump lounge_window

        "I take a seat on a nearby chair" if not explored_lounge_chair:

            jump lounge_chair

        "I move on":

            jump lounge_end

label lounge_end:

    "I suppose it's strange that I never once visited at all."

if mood > 0:

    "Time went by and before I knew it, most of my days would pass without any thought of him"

    jump library

if mood < 1:

    "I had begun to grow weary of his noncommittal gestures"

    jump library

label lounge_piano:

    $ explored_lounge_piano = True

    "There is a thin layer of dust atop the keys. Lowering the cover could have protected them, but the dust would have lain upon here all the same. This instrument hasn't been played in quite some time."

    "Did Jimmy continue to play? Growing up, nobody we knew had a piano in the home but there had been one at the schoolhouse. We began music lessons in our third year and were made to sing carols for the headmaster and teachers during the holiday season."

    "A distantly familiar tune makes its way into my head. I've since forgotten how to play bass clef or read sheet music, but I've retained some basic scales."
    "Instinctively, I wipe away some of the dust and plunk out a crude melody."

    "The trillbird sings his song\nIn a hollow grove\nWith nary a throng\nFound below or above"
    "O sweet songbird, alight\nCalm the anger of the earth\nKeep the fire burning bright\nIn our hearts and the hearth"

    play music "audio/The Trillbird.mp3" fadein 10.0

    jump lounge_menu

label lounge_window:

    $ explored_lounge_window = True

    "The grand windows allow the sun to shine beautifully into this room."

    "I look out towards the path I'd taken to enter the home and am struck by just how lovely a neighborhood this is."

    "Greenery all around, a lawn for dogs or kids, gentle shade from trees in the summer, a fireplace for coziness in winter."

    "I wonder if James knew what a lovely home he had."

    jump lounge_menu

label lounge_chair:

    $ explored_lounge_chair = True

    "Despite its plush appearance, the chair feels stiff underneath me."

if carpenter:

    "Some furniture ends up being more decorative than functional."

    "Though, if that were the case, I would have picked a lower quality leather to upholster these chairs with."

    "I can tell from looking that this burnished top-grain has been left in the sun to get crisp. Such a shame."

    "James must have spent most of his time in more private areas."

    jump lounge_menu

if tutor:

    "I am reminded of my pupil's homes."

    "A tutor often plays the role of a guest. Some clients would sit me on their unused furniture that was \"reserved for company.\" Others would place me at a kitchen table."

    "It is pleasantly odd to be in such a lounge without a book in my hand, or a willful child to handle."

    "I smile before I remember my sad business here."

    jump lounge_menu

if merchant:

    "It's all about the piano."

    "This was the type of piano guests would have crowded around. They would be standing, craning their necks to hear the latest jingle being played."

    "There would definitely be no room for sitting."

    "This is what I tell myself to explain why this chair is so uncomfortable."

    "No need for me to sit, either. There's too much to see, too much afoot."

    jump lounge_menu

label library:

    stop music fadeout 1.0

    scene library at truecenter

    "I enter what appears to be a library."

    "Jimmy was a writer after all, so it makes sense that he would own many books, and have a room dedicated to them."

    "A few volumes catch my eye:"

label library_menu:

    menu:

        "A Gentleman's Guide to Negotiation." if not explored_library_book_1:

            jump library_book_1

        "Hell Exists On Earth, a novel by Rory Stuart." if not explored_library_book_2:

            jump library_book_2

        "A Noble Charade, Jimmy's own work" if not explored_library_book_3:

            jump library_book_3

        "I move on":

            jump dining_room

# INSIGHT

label library_book_1:

    $ explored_library_book_1 = True

    "I open the book to a section in the middle. It's a full chapter on good posture (\"Keeping an erect carriage is the key to success,\" it begins)."

    "Next is a section on a lady's favorite drinks and what they might mean (\"avoid {i}desmoiselles{/i} who indulge in beverages served by the pint\")."

    menu:

        "He was brushing up on a useful skill":

            jump library_book_1_insight_1

        "Was there something he needed to negotiate?":

            jump library_book_1_insight_2

        "Did Jimmy feel socially deficient in some way?":

            jump library_book_1_insight_3

label library_book_1_insight_1:

    $ insight_1_library_book_1 = True

    "One could never been too socially attuned. I imagine Jimmy felt similarly. How studious of him!"

    "Though, some of these tips verged on crude. Jimmy surely would have gussied them up with some flair, or, at least, manners."

    "\"A change of scenery will bring a change of mindset. A fresh location will bring about a fresh mood and a fresh conversation.\""

    "I smile as I imagine Jimmy practicing this one. His arm a crook, he and a lady friend glide down a long hallway, her heart fluttering in a pool of moonlight."

    "What a tempting image. I consider pocketing the book, but remember, then, that I am no James Pryor. Back on the shelf it goes."

    jump library_menu

label library_book_1_insight_2:

    $ insight_2_library_book_1 = True

    "Marian had been swept off her feet years before this book was published. What was there to negotiate?"

    "\"A good \'night out\' outfit layers accent pieces. They are sure to attract attention. After all, all attention is good attention.\""

    "Jimmy, strutting about with handfuls of rings, acid green shoelaces, and a bowler hat. I could think of nothing funnier!"

    "\"Never let a woman ruin your confidence. Should you ever feel unvalued, allow yourself to remind her that she should be lucky for the opportunity to be speaking to you.\""

    "I imagine him \"reminding\" Marian of her \"luck.\" There was no possibility of that ending well, for either of them."

    "Jimmy must have received this book as a gag gift. I chuckle as I place it back on the shelf."

    jump library_menu

label library_book_1_insight_3:

    $ insight_3_library_book_1 = True

    "Knowledge is power. And if I knew anything about Jimmy, it was that he wanted to know everything about everyone."

    "Some tips in this guide seemed helpful, and fairly innocuous:"

    "\"A change of scenery will bring a change of mindset. A fresh location will bring about a fresh mood and a fresh conversation.\""

    "But, there is a forceful edge to others:"

    "\"Never let a woman ruin your confidence. Should you ever feel unvalued, allow yourself to remind her that she should be lucky for the opportunity to be speaking to you.\""

    "I remembered some of the women in his life, his mother, his wife. I wondered what in him needed to be refined from those fundamental relationships."

    "I put the book back on the shelf."

    jump library_menu

label library_book_2:

    $ explored_library_book_2 = True

    "Propped up on the shelf, this first edition is leather-bound and has a note scribbled in the very back."

    "To James,"
    "Through hell and back, mate. See you there again someday--"
    "RS"

    scene black
    with fade

    "I met Rory once, at Jimmy's wedding. Besides Jimmy, there wasn't a soul that I knew at the affair. Jimmy had spoken of his bride in passing, but it wasn't until the reception that I met Marian for the first time."
    "Rory Stuart is a famous writer in his own right, but he had been the only guest with whom I had felt somewhat at ease."

    scene wedding_church at truecenter
    with fade

    "I've arrived on the very day of their matrimony. The venue is located in neighboring Hestia outside of Palace Gardens, and a night in either city is beyond my means."
    "When I step into the church, my attire feels simple in comparison to the sharp suiting and elegant dresses of the other attendants."

    scene wedding_reception at truecenter
    with fade

    play music "audio/The Wedding of James and Marian Pryor_1.mp3"

    "After the ceremony, I manage to briefly chat with Jimmy and Marian before they move on to greeting their other guests."

    "\"Where's Oliver?\" I ask after congratulating the newly married couple. I haven't seen Jimmy's younger brother among the guests yet."
    "I suppose we could have shared a car down here, seeing as we were coming from the same place, and split the fare while at it."
    "I had assumed that being family, he would have made separate arrangements with Jimmy."

    "\"He couldn't make it, I'm afraid. Work has him tied up and it can't be helped. But do enjoy yourself while you're here. I'll catch up with you later!\""
    "Jimmy waves to someone in the crowd and heads over with Marian in tow."

    "I'm standing alone, sipping my third glass of wine when Rory approaches the bar for another drink."

    "With whiskey in one hand, he introduces himself with a firm, jovial handshake. \"So how do you know James?\""

    menu:

        "He's a good friend of mine.":

            jump good_friend

        "We were schoolmates.":

            jump schoolmates

        "We're from the same hometown.":

            jump hometown

label good_friend:

    "\"Is that so? Pleased to meet another dear friend of his. Surprised we haven't met before.\""

    menu:

        "Likewise, and how did you meet Jimmy?":

            jump rory_friend

        "The pleasure is mine, I'm an admirer of your work.":

            jump rory_admirer

label rory_friend:
    $ rory_jimmy = True

    "\"Jimmy?\" He lets out an amused chuckle. \"I'll have to call him that from now on.\""

    "He eagerly takes a sip of whiskey from his glass, as if about to recount a favorite tale."

    "\"James and I met while living at the same cheap hostel in Lintonbury. All sorts of mad folks there like you wouldn't believe. Some strange characters, I tell you...\""

    "\"So we'd been staying there for about a year--stop me if you've heard this all before. No? All right, so there was a roof terrace where we used to write together.\""
    "\"We were up there working one day as usual, when our dear fellow tells me that he's getting published through Smith and Simmons.\""
    "\"That's right, A Noble Charade. Finally gave him a chance after all of that grunt work. We all have to pay our dues, yeah?\""

    "\"Then right at that moment, one of the other tenants comes {i}storming{/i} up, accusing us of stealing his soap! As mad as it was, I'll always have fond memories of that place.\""
    "\"And James put in a good word for me with S&S, and look where we are. I'll always be grateful to him.\""

    jump wedding_end

label rory_admirer:
    $ rory_business_card = True

    "Rory brightens at my words. \"Thanks, buddy. That means a lot. So then I take it that we're both admirers of James' work. Do you know that feeling, when you're witnessing somebody doing exactly what they're meant to do? That bastard was born to write.\""

    "\"Do you know what I mean? To be able to do what you love for a living. You can be good at things but not necessarily like them, you know?\""
    "\"Sometimes, I think it's good to try things you're not good at either.\" His words are slurred with drink, but his gestures become more animated. \"But then you might find something you're really, really good at and that's why you're here.\""
    "\"I'm rambling, aren't I? Anyway, I'm really flattered if you've enjoyed my writing. It really means a lot.\""
    "He regards me good-naturedly."

if carpenter:

    "\"I've always had a respect for your craft. I purchased a new table and chair set for my parlor. I found them at an antiques shop and the quality is just fantastic.\""
    "\"You really do get what you pay for, it's nothing like those do-it-yourself assembly pieces that are so popular these days...\""

    jump wedding_end

if tutor:

    "\"To be honest, I've never been much for higher education. If you have it, you have it. I don't think talent can be taught.\""
    "\"But some schooling is probably better than none. If you're going to quit the books, I suppose it better be because you're doing something more important...\""

    jump wedding_end

if merchant:

    "\"How is business lately? They say the economy is expected to turn around soon enough, what do you think?\""
    "\"Do you source domestically, or from overseas? We need more jobs here. Of course, they should be available to anyone regardless of background...\""

    jump wedding_end

label schoolmates:

    "\"I see, from the academy?\""

    menu:

        "I beg your pardon?":

            jump schoolmate_truth

        "Academy? Yes...that's right.":

            jump schoolmate_lie

label schoolmate_truth:
    $ rory_artist = True

    "\"Beckford Academy, wasn't it? So terribly posh, I always give James a hard time about it but I'm one to talk. Don't tell anyone, but I attended Collins Prep for a moment! Hardly befitting of a starving artist, I know.\""
    "\"Speaking of which, do you agree that artists must suffer for their art? I don't think I would have sold half as many books if I had written about Heaven.\""
    "\"We spend our lives seeking happiness, aiming to eliminate pain and turmoil, but nobody wants to read a story without any drama in it. It'd be terribly dull.\""
    "\"You can't suffer too much though, or else you'll lose the means to create. Leave the suffering to your spirits, not your coffers. Need to keep the books selling.\""
    "\"But I really can't complain, because now I'm able to write what I want to write. Within reason, of course. Novels aren't the only kind of writing out there.\" He tips his glass toward me."
    "\"There's script on the bottle that held this whiskey, or...lighter fare, if you will. There's a place for those things but for me, there's nothing like writing words that are truly your own.\""


    jump wedding_end

label schoolmate_lie:
    $ rory_choices = True

    "\"That's wonderful that you've remained acquainted after all this time.\""
    "\"Some of my best mates were from my school days, I think. In a way, you never have friends like that again. Back when we didn't need to worry about medical bills and the rent and all that rubbish.\""
    "\"Gosh, I don't know if we all still keep in touch like you two. I guess we'll find out at my own wedding!\""

    "\"You know how James and Marian met, don't you? James just goes strolling out one day in the park to see the sunset and Marian just happens to be out there, on the same day doing the exact same thing. Like something out of a film.\""
    "\"To think--if one of neither of them had gone to the park that day, that we all wouldn't be here.\""
    "\"It's the age-old question of whether our lives are predetermined, or if our choices make us who we are? Hell if I know. Was I destined to be a writer?\""
    "\"Maybe I got lucky meeting James when I did. But it wouldn't have mattered if I hadn't picked up a pen and started writing to begin with. And I have to believe that my choices matter.\""

    jump wedding_end

label hometown:

    "\"Nice, so you're also from Earnsworth? I'm originally from Palace Gardens myself.\""

    menu:

        "No, from Atford.":

            jump hometown_truth

        "Yes. Earnsworth.":

            jump hometown_lie

label hometown_truth:
    $ rory_atford = True

    "Rory raises an eyebrow. \"Atford? If I recall correctly, James came up to Lintonbury from Earnsworth after finishing school.\""
    "\"Isn't Atford up in Commerce Valley? Now that I think of it, one of my friends was talking about buying a residence there, I've heard it's rather quaint. I didn't know James had lived in Atford prior. James Atford Pryor.\" Rory laughs at his own joke."
    "\'Did the Pryors move around much when he was a child? I imagine that could be difficult. But I'm sure James got along just fine.\""

    jump wedding_end

label hometown_lie:
    $ rory_travel = True

    "\"It seemed like James couldn't wait to leave, but it must not be so bad if you've stayed. There's something comforting about the familiarity of the place you grew up in.\""
    "\"I've lived in Palace Gardens all my life. I never travelled much in my youth, but I used to come to Hestia once in a while. Fancy lot out here, aren't they?\""
    "\"Not too much has changed, except maybe the new hotel on Fourth Street. It's funny, to think of people coming to visit when to the residents here, it's just home.\""
    "\"My schoolmates and I would spend our days idling about the streets, grumbling about how there was nothing to do. So naturally, I leapt at the chance to leave.\""
    "\"And now here I am, back to where I started, idling about the same streets and nipping down to the grocer's like my mother used to, dear god.\""
    "\"How I dread being grown...\""

    jump wedding_end

label wedding_end:

    "The evening passes by a little faster with Rory's company and an endless supply of libations. He introduces me to a number of other guests whose names I admittedly won't remember after tonight."
    "There are too many of them, and my faculties are inhibited by a combination of alcohol, nerves and the knowledge that we will never again cross paths."

    "When the clock strikes nine, I excuse myself and let Rory know that I must be going."

    "\"No, stay, stay,\" he insists but I catch Jimmy's eye and wave. He gets Marian's attention and they make their way over."

    "\"It was good to see you, but it's time for me to head back. I must get back to work first thing tomorrow morning,\" I tell them."

    "Rory claps me on the shoulder. \"You really should stick around. I'm sure James can put you up if you're too out of sorts to travel by the end of the night, I know I will be.\""

    # TODO
    "(protagonist asks about Oliver and it gets slightly awkward)"

    "Jimmy smiles thinly, giving me a nod. \"Trip was all right? Thanks for coming out here today.\""

    "I smile back. \"Congratulations again. And it was nice to finally meet you, Marian.\""

    "Marian beams at me, giving my hand a friendly squeeze. \"It was lovely to meet you. I hope you'll come visit us sometime. Once somebody gets the renovations in order.\" She teasingly nudges her newly wed husband."

if rory_jimmy:

    "\"That's right, 'Jimmy,' get your bloody house in order for chrissake,\" Rory chides with a boisterous laugh. \"What's the use of owning a mansion if you can't even live in it?\""
    "Jimmy doesn't respond at first, and he glances at me briefly before smirking back at Rory. \"And when are you going to stop renting and finally settle down?\""
    "Rory gasps in mock-indignation. \"In exchange for my freedom? No thank you, very much. No offense, Marian!\""
    "\"Oh Rory, you're no gift yourself!\" Marian laughs. \"But to each their own.\""

    jump wedding_epilogue

if rory_business_card:

    "\"Oh right, before I forget. I'm not too far gone yet.\" Rory reaches into his inner vest pocket and hands me a card. \"Give me a ring if you're ever in town again. You have one for me?\""
    "I've never had a card of my own. A practice I've heard of, but never had to participate in before now."
    "I absently fold the corners in my hand. \"Unfortunately, not on my person at the moment.\""
    "\"Ah, that's all right. Today wasn't meant to be about business anyway. Tell you what--the next time you call on James, you'll both invite me along, yeah? We'll get up to no good.\""
    "\"Welcome to the club,\" Marian says to me a loud, conspiratorial whisper, rolling her eyes fondly."

    jump wedding_epilogue

if rory_artist:

    "Rory also takes my hand, shaking it fondly. \"I do hope we'll see each other again sometime. You've found a good one here, James. We both have a deep understanding of the arts.\""
    "\"Really?\" Jimmy gives a smile. \"I didn't know you were interested in the arts,\" he remarks evenly."
    "\"But it's not just about the art,\" Rory intones. \"It's deeper than that. Deeper than this glass.\" He takes another swig of his whiskey."
    "\"Rory, what are you babbling on about?\" Marian shakes her head, laughing. \"I have never found art to be more truly subjective than I do now.\""

    jump wedding_epilogue

if rory_choices:

    "\"Are you sure that you want to head out already?\" Rory asks. \"Choose wisely, your future could depend on this very moment!\""
    "\"It's true, I could be out of a job come tomorrow if I stay much longer,\" I joke in return. In jest, there is truth."
    "\"Fair enough. Then, here's to jobs that pay the rent.\" Rory raises his glass, then throws it back."
    "Marian gives me a sympathetic smile. \"Thanks again for celebrating with us.\""
    # TODO
    "(dialogue based on occupation)"

    jump wedding_epilogue

if rory_atford:

    "\"Back off to Atford, then?\" Rory says. \"Wishing you safe travels.\" Jimmy visibly starts at the mention of our hometown."
    "\"I didn't realize you had lived in Atford *prior*, James.\" Rory repeats his joke and I give an agreeable laugh, many of which I have offered this evening."
    "\"All prior to when I met this fair lass hither.\" Jimmy slides an arm around Marian's waist and she leans into his shoulder. \"Marian Pryor, I like the sound of that.\""
    "\"We'll see about that,\" Marian retorts playfully, looking up at him. \"I think I like James Fairbright better.\""
    "Jimmy gives a low chuckle. \"But it wouldn't do to reprint all of my books, would it?\""

    jump wedding_epilogue

if rory_travel:

    # TODO
    "\"When can we see each other again? Say, I've been meaning to go see the world for once once of these days. Expand my horizons. You should come along.\""

    "\"That sounds lovely,\" I reply. \"Where would you want to go?\""

    "\"I've always wanted to visit Honom, but I've heard that it's dreadfully hot year round. The Jora Naya islands are said to be sublime. Or Moreland and its beautiful green hills. I should take the year off and see them all.\""

    "(Marian says something intelligent about one of these places)"

    jump wedding_epilogue

label wedding_epilogue:

    "With a final word of farewell, I take my leave and the sounds and lights of the festivities begin to fade away as I reach the front gate, where I climb into a waiting car."
    "Transportation has been arranged for the attendees, most of whom are staying at the nearby Fourth Street Hotel overnight."
    "I'll take the car to the hotel, and then head over to the train station by foot. I'll be able to rest during the few hours of the ride, and I'll be back home by early morning."

    "I haven't seen Rory since, but I wish him only the best and I wonder if he has yet heard of Jimmy's passing."

    stop music fadeout 5.0

    scene library at truecenter

    with Fade(2.0, 2.0, 2.0)
    jump library_menu

label library_book_3:

    $ explored_library_book_3 = True

    "I remember it being somewhat fascinating at the time when Jimmy was first published, that he had now written a book like the ones we were obligated to read when we were students."
    "Looking back on it now, I can better acknowledge and appreciate the impressiveness of this feat."

    "He had gifted me a copy back then, and I had congratulated him and told him that I enjoyed it very much. I'm certain it's sitting on my bookshelf, which I admit I have perused much more rarely of late."

    "To be honest, some of the details elude me when I attempt to recollect the events of the story. Is it still fair to say that I once read it?"
    "But I know the main plot--Kurt Candon, the protagonist, is a skilled practitioner who at the height of his celebrated career is discovered to be a fraud."
    "One passage stands out in my mind, the one that his debut novel remains most famous for. I turn to the last section of the novel (where most important things occur) and manage to find it:"

    "{i}It was then that I knew it mattered not who I was, but who others would perceive me to be. And so that was who I became. Day in and night out, I played the best version of myself upon society's stage.{/i}"
    "{i}As much as they insisted otherwise, the audience did not care to see or know of the toil and turmoil behind weighted curtains, nor did I wish to show any of it. {/i}"
    "{i}The world only desired to witness a polished performance which I fully intended to deliver until the day I died. 'Twas a noble charade. But it is difficult to call it deceit, when it was so very earnest. {/i}"

    jump library_menu

label dining_room:

    scene dining room at truecenter

    "The dining room would have been host to innumerable parties. Champagne would have flowed freely beside buffets, splayed across the tablecloth."

label dining_room_menu:
    scene dining room at truecenter
    menu:

        "I take a seat at the table" if not explored_dining_room_dining_table_sit:

            jump dining_room_dining_table_sit

        "I examine the cabinet of full of fine china" if not explored_dining_room_dining_room_dining_trappings:

            jump dining_room_dining_trappings

        "I look at the lively painting adorning the wall" if not explored_dining_room_dining_room_painting:

            jump dining_room_dining_room_painting

        "I move on":

            jump patio

label dining_room_dining_table_sit:

    $ explored_dining_room_dining_table_sit = True

    "I am a guest, now. To my right would be Jimmy, at the head of the table. From behind, a caterer, or maybe Marian would enter grandly with a Christmas goose, or a Thanksgiving turkey."

    "Jimmy would compliment it effusively, the writer in him always finding a new way of saying \"delicous!\" each time."

    "The morning after, there would have been quiet cups of coffee, crosswords, and comics."

    "I was probably the first person to sit here in quite a while."

    jump dining_room_menu

label dining_room_dining_trappings:

    $ explored_dining_room_dining_room_dining_trappings = True

    "A set of silverware, quite literally made of silver."

if carpenter:

    "I always thought pure silver looked surprisingly dull in comparison to the cheaper imitations that many of us are accustomed to."
    "It also bends quite easily, not that I'm about to tamper with Jimmy's valuable spoons and forks."

    jump silverware_memory

if tutor:

    "It appears I have stumbled upon Jimmy's very own Mildenhall Treasure. No inscriptions to be found, but I knew this cutlery had a history all of its own."

    jump silverware_memory

if merchant:

    "This collection looks to be in fairly good condition, if only from lack of use rather than deliberate maintenance, and it plainly exceeds sterling grade."

    jump silverware_memory

label silverware_memory:

    scene dining room_memory at truecenter
    with ease

    "{i}Once I am rich, I shall acquire all of the silver spoons that money can buy.{/i}"

    "We were nearing the end of secondary school when Jimmy first told me that he wanted to be a writer."
    "At the time, I had taken it to mean that he wished to be successful, much in the way that some of our peers aspired to the life of actors, musicians, athletes."
    "After all, Jimmy had been one to grumble about lessons spent deciphering what were deemed to be the classics."

    "\"Why couldn't they just write what they mean?\" He had asked once. \"They'd need to write another book just to explain the first.\""

    "After that, the idea would come up every so often in passing conversation."

    "\"The greats often have a pen name that they stand behind. It separates them from their craft, and allows the work to speak for itself.\""

    "\"So you're one of the greats now, are you?\""

    "\"The greats are rarely recognized in their time.\""

if mood > 0:

    "Jimmy was fortunate to be recognized during his lifetime."

    "Whether it be chance, or talent, Jimmy wrote works that people wanted to read, no small feat in this day and age."

    "With his success, he managed to fulfill one of his idle childhood promises. Or, perhaps it wasn't so idle, if he remembered it after all those years."

    "I am proud of what Jimmy accomplished. I know he would be proud of his legacy as well."

    jump dining_room_menu

if mood < 1:

    "I wonder if Jimmy's cleverness grew increasingly tiresome with age. Jimmy would always find some way to cushion his ego, should he fail."

    "Not to say he wasn't right. Success within a lifetime was rare. And when it did occur, it often turned people into rich snobs."

    "From this mansion on a hill, I'm sure Jimmy found it easy to look down on the rest of us."

    "Well, you got your wish, Jimmy. You got your spoons. I hope they made you happy."

    jump dining_room_menu

label dining_room_dining_room_painting:

    $ explored_dining_room_dining_room_painting = True

    "I see a set of birds perched acutely on barren branches. Against the cold landscape, they look sprightly, vivacious enough to come singing off the canvas."

    "What a lively piece of art. I'm sure Jimmy curated it himself. Manipulating the mood of a room through art seemed like an activity he would have loved to talk about."

if merchant:

    "When I search the corners of the painting, I can see no artist's signature. Looking at the paint quality, and the subject matter, I begin to form an impression."

    "One would have purchased this work from a minuscule seaside gallery. The artist that painted it would be eccentric, and solitary, and sometimes even talented."

    "One would have purchased this painting on some dreamy weekend getaway, and the story of its acquisition would far outweigh its artistic value."

    "Jimmy would have loved telling that story. I wonder with whom it lives on."

    jump dining_room_menu

label patio:

    scene patio at truecenter

    "The garden patio is spacious. The wood beneath my shoes is weathered by the sun."

if mood > 0:

    "What were you thinking as you sat out here, Jimmy?"

if mood < 1:

    "I take moment to rest outside in the patio."
    "A calm wind rustles through, softly animating the surrounding grass"
    "Every so often, when we were still familiar, he would speak of having me over but nothing ever came of it. He certainly didn't need to extend himself if he didn't have the time, and I would have understood."
    "So while I responded in accord, I had become somewhat skeptical of his gestures."

    "Perhaps I could have taken the initiative and held him to a specific time and date. And then we could have sat here together, after he had politely offered me a drink, gazing upon the garden and reminiscing upon our childhood."
    "Speaking of both past and present until we had exhausted both, and then settling into a silence while sipping our respective glasses (wine in mine, and plain water in his)."
    "And then we would have done it, what he always said we should do. Would we have been better for it in the end?"

    "Better than to acknowledge my skepticism or to outright refuse his invitations, I suppose."

    "Jimmy, why am I even here for him?"

label patio_menu:

    menu:

        "I move on":

            jump kitchen

label kitchen:

    scene kitchen_1 at truecenter

    "The kitchen is the homiest part of this house."

label kitchen_menu:

    menu:

        "Look in cupboard" if not explored_kitchen_cupboard:

            jump kitchen_cupboard

        "I open a drawer" if not explored_kitchen_drawer:

            jump kitchen_drawer

        "The bar" if not explored_kitchen_bar:

            jump kitchen_bar

        "I move on":

            jump upstairs

label kitchen_cupboard:

    $ explored_kitchen_cupboard = True

    "There are several different types of tea inside the cupboard: Earl Grey, chamomile, genmai cha and Puerh."
    "Some in packets, others sealed inside a labeled jar."

if carpenter:

    "cool lots of tea"

    jump cupboard_inside

if tutor:

    "technically chamomile isn't a tea"

    jump cupboard_inside

if merchant:

    "the loose leaf is better tasting and more expensive"

    jump cupboard_inside

label cupboard_inside:

if carpenter:

    "A red clay teapot with a lion figurine carved onto the lid"

    jump cupboard_memory

if tutor:

    "A teapot reminiscent of Dutch red stoneware but with Asian influence in its design"

    jump cupboard_memory

if merchant:

    "This looks like a Böttger teapot, modeled after those made of Yixing clay."
    "These pots gradually take on the flavor of the tea brewed inside, and so choosing one type of tea is recommended."

    jump cupboard_memory

label cupboard_memory:

    "Hiding behind the collection of tea, I find a box of Hotecakes. The package has already been opened and there's only one left inside. Hard to say how long it's been sitting here, but Hotecakes are said to last quite a while."

    "Right, Jimmy used to love these. He must still have been fond of them after all of these years. I've always preferred Jelly Pies myself."

    "The packaging has changed since then, with the lettering now more simple and prominent. The cakes used to be wrapped in wax paper, but these days they come in clear, crinkly plastic and somewhat smaller than I remember."

    scene black
    with fade

    "Jimmy grins as he licks the the crumbs off of the waxy wrapping. \"I don't want to waste a single bit.\""

    "\"You're really licking the paper, you're crazy.\" I'm laughing as Jimmy's mother comes up behind us. She gives me an exasperated smile."

    "\"Come on now Jimmy, set the table. What on earth are you doing?\""

    "\"Eating Hotecakes, mother.\""

    "\"You're going to spoil your appetite, we have a cake to eat later.\""

    "\"Hotecakes are a cake, I could have them instead.\""

    "\"Don't be silly. Now come on, everyone's going to be here any moment. Throw that away, don't just leave it on the ground beside you.\""

    "I get up to follow them but Mrs. Pry motions for me to stay. \"You just wait and enjoy yourself, everything will be ready soon.\""

    menu:

        "Wait for the party to begin.":

            jump party_outside

        "Follow Jimmy into the kitchen.":

            jump party_inside

label party_outside:

    "The yard looks tidier than usual, with none of Oliver's toys lying around and Jimmy's bike nowhere to be seen. We'd spent hours one afternoon rummaging through the garden patch, searching for treasure until we grew weary of digging up nothing but weeds."

    "The weeds are now cleared out and the surrounding grass smells fresh from being newly mowed. The \"X\" that Jimmy had scrawled into the center of the patch has since been smoothed over with no remaining traces."

    "Over in the corner, I see Oliver sitting in the shade of the oak tree..."

    menu:

        "...instead of on the swing that used to hang from its largest branch.":

            jump oliver_truck

        "...playing with a pair of binoculars.":

            jump oliver_binoculars

label oliver_truck:

    "Jimmy and I used to swing high and then jump off of as far as we could, seeing who could land farther. Once after we had gone back inside the house, Oliver had tried the same thing and landed on his knees instead of his feet."

    "All of us ran outside at the sound of his loud cries and after that, Mrs. Pry had gotten rid of the swing for good. Jimmy had been rather sore about it, which culminated in Jimmy and me sneaking into Oliver's room."

    "I anxiously stood aside and watched the door while Jimmy searched for his brother's Tractor Truck. Once he found it, we rushed downstairs and past his mother and brother--I didn't dare look up until we were outside and behind the tool shed."

    "Jimmy threw the Tractor Truck onto the ground before going into the shed and emerging with a hammer."

    "\"Jimmy, are you sure...?\" I stammered before he proceeded to whack it over and over until he had cracked the body and bent the frame. We stared at what Jimmy had done and to my horror, Oliver came running up behind us only to see his favorite toy ruined."

    "I remember expecting Oliver to get angry and lash out at his older brother in retaliation. Instead, Oliver simply began to weep. Uneasily, I glanced over at Jimmy who now looked as if he were regretting his actions."

    "\"Olly--\" Jimmy began, but Oliver had already run back to the house. In the end, Mrs. Pry sent me home early and I awkwardly bade Jimmy farewell as he trudged behind her."

    "Later that week, Jimmy had me accompany him to the toy store. We walked past guns, dolls and board games, briefly stopping by a train set and moving on after we saw the price."

    "Jimmy ended up picking an assortment of small die cast vehicles, none of which looked like the Tractor Truck but at least there were several of them. At the cashier, he pulled his piggy bank out of his knapsack and paid for them."


    jump kitchen_menu

label party_inside:

    "Jimmy opens the drawer to pull out several forks and knives, the ones that Jimmy's mother got at the local corner store and would use at every occasion since."

    "\"Fork on the left, knife on the right Jimmy.\""

    "\"I know, mother.\" Jimmy gathers up the utensils in his hands and they clink loudly against each other."

    "\"And be careful with those, don't pick them up so carelessly.\""

    "\"If you don't like how I do it, why don't you do it yourself?\" Jimmy calls back to her."


label kitchen_drawer:

    $ explored_kitchen_drawer = True

    "I'm not sure what I expect to find in these drawers. Jimmy isn't, wasn't, the type who'd keep a secret stash of documents underneath a pile of folded dish towels."

    "There's pedestrian cutlery, some knives and their whetstones, and a few rusty peelers."

    "Another drawer holds a set of appliance accessories. I see attachments for a large beater, some doodads to screw in, and some, perhaps, extra things that look like they could really slice something up."

if merchant:

    "Most of these belong to an older model of stand mixer, though I could hardly call them old."

    "A mere decade ago, the only way to beat an egg was with a beater and some elbow grease. Having an automatic mixer in your home was considered very \"À là mode\"."

    "Since coming to market, each year, new improved automatic mixers have been clamoring for space in everyone's homes and cabinets. Nutty! I'd never seen technology move so fast."

    jump kitchen_menu

label kitchen_bar:

    $ explored_kitchen_bar = True

    "Jimmy, always the entertainer."

    "When I open the bar, I see bottles of whiskey old enough to vote, angled champagnes labeled with dates when they needed to be turned, and finally some truly, utterly unpronounceable wines."

    "I know for a fact that James himself didn't drink."

    "Of course, that didn't stop him from stocking the good stuff."

    menu:

        "A toast, to James":

            jump kitchen_bar_have_a_drink

        "I close the bar":

            jump kitchen_menu

label kitchen_bar_have_a_drink:

    $ likes_alcohol = True

    "I reach for an open bottle. Here's one, it's a scotch from somewhere called Kirkwall."

    "I pour myself a glass. Holding it to the light, I see it's the color of varnish."

    "\"James, my friend, thinking of you, thinking of us from beyond. Thank you.\""

    "{i}gulp{/i}"

    "What a lovely burn. I tell myself I'll wash the glass before I go, but not too soon, in case I feel the urge to give James another toast."

    jump kitchen_menu

label upstairs:

    scene hallway3 at truecenter

    "It's darker up here than when I first entered the house. The hallway is illumined only by the glass panes before a sunlit balcony. The shadows of the doorframes set them deeper in the walls."

    "There is a faintly musky odor that was not present downstairs. Upstairs are often a little more private, and a little less well-kept. I am unable to place the specific scent. It is distinct against the smell of wood."

    "I decide this would be a good a time as any to get some air. There's something close, and heavy about being in an empty home."

    # scene balcony at truecenter

    "I step onto the coarse tiles of the balcony. There is room enough for me to stretch my arms. I exhale, and my neck cracks. I didn't realize how tense my body had become! The breeze is mild and sweet."

    "I hear the crisp chirps of a handful of small birds. Some dot the lawn, searching for beetles among the weeds. If I still myself, I can imagine the faint sound of running water."

    "Touching the railing, I see before me the garden, stretching to the boulevard. Beyond, the rest of Palace Gardens."

    "There is a precise lushness about the town. The layered treetops cascade over each other like verdant falls. I see gentle maples that promise brilliance in fall, a few slender birches, a tree shaped like a willow, and not too far away, a riot of wisterias. "

    "Between them are the suggestions of roofs, homes with glassy exteriors. They are enclaves, designed for perfect privacy, little perfect worlds."

    "To stand on this balcony, I feel both at once a sense of peace, and a sense of alienation. I am a visitor, looking in, and looking out on a life I didn't live."

    "Enough air. There is more to do."

    jump salon

label salon:

    scene salon at truecenter

    "Where Jimmy might have retired after a long day's work, and Marian might have joined him."
    "These couches feel much more comfortable than the ones in the living room."
    "Suitable for reading and pleasant conversation."

label salon_menu:

    menu:

        "A large portrait of James and Marian." if not explored_salon_painting:

            jump salon_painting

        "I examine the curio shelf." if not explored_salon_shelf:

            jump salon_shelf

        "I move on":

            jump conservatory

label salon_painting:
    $ explored_salon_painting = True

    "James sits on a chair, with Marian standing beside him."

    jump salon_menu


label salon_shelf:
    $ explored_salon_shelf = True

    "On each shelf lives a charming set of oddities: a signed boxing glove, little clay vases painted with cacti, various paintings in miniature."

    "I can imagine Jimmy retelling a story about each one."

label salon_shelf_menu:

    menu:

        "I gingerly pick up a clay vase" if not explored_salon_shelf_vase:

            jump salon_shelf_vase

        "I examine the imposing boxing glove" if not explored_salon_shelf_glove:

            jump salon_shelf_glove

        "I squint at one of the miniature paintings" if not explored_salon_shelf_picture:

            jump salon_shelf_picture

        "I reach for the great urn at the very top of the shelf" if not explored_gueuloir:

            jump gueuloir

        "I move on":

            jump salon_menu


label salon_shelf_vase:
    $ explored_salon_shelf_vase = True

    "There's a tiny donkey marching across a brown clay desert. When I pick up the vase, the material is rough against my fingers."

    "\"That was from the winter I spent in Mexico. Nothing like the desert can stir your soul. And there were so many villages in them! Just when you were out of sight of one, another would appear. Naturally I just had to indulge in some of the indigenous folk art.\""

    jump salon_shelf_menu

label salon_shelf_glove:
    $ explored_salon_shelf_glove = True

    "It seems sacriligeous to handle the old sweaty boxing glove with my bare hands. It was signed by... someone, famous, I'm sure. The signature is stylized in a way only fighters could do."

    "\"That was from the Remy vs. Johnstone fight. Sat in the front row! Could feel their sweat flying off of them when they ate one. Better than television. Thousand, no, a million times better. You gotta see a fight live. There isn't anything like it.\""

    jump salon_shelf_menu

label salon_shelf_picture:
    $ explored_salon_shelf_picture = True

    "Truly it takes no small degree of both skill and artistry to reproduce works at such scale! I squint at a miniature of a rococo scene. More nobles than I can count, gathered for a picnic, joined by a riot of cherubs."

    "\"I couldnt imagine what it'd be like to live in those times, but isn't this painting just {i}darling?{/i} Marian found it somewhere here, in Palace Gardens. I remember, ah yes, it must have been that thrift shop! The one on 9th! Always such hidden treasures there.\""

    jump salon_shelf_menu

label gueuloir:
    $ explored_gueuloir = True

    "Disaster! My bumbling feet catch on themselves and I fall forcefully into the shelf. Vases clatter to the floor, the signed glove flies across the room, and each and every picture tips over in its frame."

    "I am immediately mortified as I try to collect the bits and as best I can restore order. Oh, dear, the vases have shattered, and... ah. What a clumsy oaf I am. I will just put everything as it was as best I can and..."

    "The shelf has moved."

    "In tidying, I notice the shelf has very obviously been displaced from its original position. I deduce, after simply looking down, that this must have occurred because this shelf is in fact on wheels."

    "What a strange thing to have be so insecure. I give it a jiggle, and a tug, then a smooth roll. The great urn I was reaching for seems to be in fact glued or otherwise fastened to the top of the shelf. Probably for the best given its heft, and my current nosy preoccupation."

    "When the wheels of the shelf reach their natural stopping point against the carpet, what is revealed is a door."

    "What a fascinating discovery!"

    "I open the door and enter the windowless room."

    "{i}Click{/i} I find a pull chain for a light and give it a go."

    "The room revealed is somewhat bare. Aside from the light fixture, all I can see is a podium, and a phonograph."

if carpenter:

    "Rooms like these are odd, but unsurprising. Bigger houses always have one or two little airless boxes whose reasons for existence are lost to time."

    "I can tell, however, by the distinct dimensions of this room, and the paneling on the walls that this chamber was acoustically designed to resonate pleasantly."

    jump gueuloir_end

if tutor:

    "Podium... recording instrument... closed room... is this some sort of gueuloir?"

    "Flaubert had one, a room to scream prose in, basically. I imagine James, perhaps more calmly, reciting his works aloud, capturing them in the phonograph, listening to the sound of himself with a measure of probing dissatisfaction."

    jump gueuloir_end

if merchant:

    "The bronze of the phonograph is stunning. Not tarnished in the least. A pristine record. Good equipment begets good practices. If this was used, then it was kept well."

    jump gueuloir_end

label gueuloir_end:

    "I place the needle on the record in the phonograph to see if there are any recordings here to enjoy."

    "\"In the April showers soothing, in the May the flowers brooding.\""

    "Ah! It is James! His voice tinkles through the horn."

    "\"Alright, now, Chapter 7, page 3, start. ... 'How do you think that makes me feel?' he cried, 'Each day you tear and moan. Do you not see what it is you do to me?' His hands gripped the cornered curve of the desk, but across it, in this one instance, she remained unmoved.\""

    "The emotion in his voice is even, despite the frantic scene of a man expostulating at a woman. As he continues, I hear some words catch, they somersault over his tongue. And in my mind's eye, I can see him standing at that podium, calculating each sentence."

    "\"...that he was convinced that he was the convincer, to convince her, 'twas the, 'twas not the, no, ugh.\" there is some paper shuffling, and the recording stops."

    "Ah! It is as if his ghost continued industriously from the beyond. I find myself smiling as I imagine James now, pacing in this little room, his words inhabiting it forever."

    jump salon_menu

label conservatory:
    scene conservatory at truecenter

    "The conservatory is full of plants"

label conservatory_menu:

    menu:

        "I look in the drawer" if not explored_conservatory_drawer:

            jump pasiphae_play_intro

        "I move on":

            jump study

label pasiphae_play_intro:

  $ explored_conservatory_drawer = True

  "In the drawer I find a book with neatly penned pages. This penmanship is neat, evenly spaced, and deliberately cursive. It seems this book may not have been meant for publishing. The lack of title, and author helps confirm my suspicions."

  menu:

    "This must be one of James' unpublished works":
      $ pasiphae_author = "James"
      jump pasiphae_play

    "This must have been written by someone other than James":
      jump pasiphae_play_author

label pasiphae_play_author:

  "But who else could it have been?"

  menu:

    "An esteemed guest must have left this here and forgotten about it":
      jump pasiphae_play_author_mystery

    "Someone must have spent a lot of time here writing it":
      jump pasiphae_play_author_marian

label pasiphae_play_author_mystery:
  $ pasiphae_author = "this unknown author"

  "The author of this book must have thought very little of his or her work to leave it here."

  "Probably some very drunk or very happy writer, dragged off to bed after too much champagne."

  jump pasiphae_play

label pasiphae_play_author_marian:
  $ pasiphae_author = "Marian"

  "The only other person who lived here was Marian. This must have been from her hand."

  jump pasiphae_play

label pasiphae_play:

if tutor:

  "I begin leafing through the pages, immediately recognizing the names of the characters:"

  "Pasiphaë, the Greek sorceress who was cursed by Poseidon into loving a bull. Her husband, Minos, and, of course, the chorus, our moral voice of reason."

  "This seems to be a retelling of her story."

  "But here, Poseidon is no godlike man, cursing thunderous madness from the sea."

  "As in life, he never appears. His curse is quiet, and we, the audience, are left watching Pasiphaë unravel, seemingly all by herself, within the humanity and intimacy of the stage."

  jump pasiphae_play_body

if merchant:

  "There is a play of some sort in the book. It sounds like some sort of Greek myth."

  "It isn't one that I immediately recognize, but I know a Greek name when I see it, all olives and the Aegean."

  "This woman, Pasiphaë seems to be pretty mad that her husband has a magic cow and she doesn't."

  "And I get it, there's a reason why 'his' and 'hers' lines sell so well. It seems like the ancient Greeks didn't quite experience the same slick equality like we have these days."

  "I knew they'd end up in trouble, and I was right."

  jump pasiphae_play_body

if carpenter:

  "In this book is a play."

  "I recognize the name Minos from a play in a town square about a labyrinth, years ago, but I don't recognize this specific story"

  "As I leaf through the pages, I learn that a woman named Pasiphaë is having a problem where she wants her husband's prize bull."

  "Ah, this must be some sort of prequel to the labyrinth story. I certainly don't remember {i}that{/i} ending well."

  jump pasiphae_play_body

label pasiphae_play_body:

  "{b}Minos{/b}: The sentries see you face the bull in the fields. You cannot hide it from them. They say there is a feverish look in your eyes."

  "{b}Pasiphaë{/b}: Are you sure it is right to trust a sentry's gossip? It is they who gawk at cows, not I."

  "{b}Minos{/b}: Gawk they may, but they are not you. Fever is the youth of madness, they say. So steadfastly you stare that even crows might land on you."

  "{b}Pasiphaë (fiery){/b}: Enough of these ridiculous accusations. Why are you doing this? Since when do you care what I want, or what I do? You never have before!"

  "{b}Minos (defensively){/b}: I don't understand, this isn't like you. I love and trust you, and want only the best. While the sentries may gossip below you, I speak to you as an equal."

  "{b}Pasiphaë{/b}: Such empty words! If you loved and trusted me you would do as you always have and leave me be! As you will and as you always have."

  "{b}Minos{/b}: Enough! Command you I will not, but neither will I move. Tell me the truth of this matter, for you god-born owe it to man."

  "{i}Pasiphaë walks in a circle, increasingly agitated. She busies herself with a dish, then a towel. Minos watches. When she sees he won't leave, she finally faces him.{/i}"

  "{b}Pasiphaë (calmly, but with wild eyes){/b}: Why would Poseidon choose you to bestow such a wondrous creature? Why not I? Daughter of Helios that I am, sorceress divine, do I not deserve the adoration of the sea?"

  "{b}Minos{/b}: You covet my bull? The mighty bull of Poseidon?"

  "{b}Pasiphaë{/b}: King you are, but queen am I, what great {i}blessings{/i} have been {i}showered{/i} upon you. What {i}great fortune{/i}. Never have I received anything I have not grasped with my own two hands."

  "{b}Chorus{/b}: A house quiet sits in balance with the gods. Fortunate are they who can remain content. But when that quiet is broken, that house is shaken forever."

  "{b}Minos{/b}: What fearsome jealousy! It twists the woman before me. So sudden it rises. How has this evil taken hold?"

  "{b}Pasiphaë{/b}: Sudden? Was it not I who cursed your seed to serpents? When a woman dresses her desires as lover's envy, her husband sees nothing. Yet when she wishes power, she is now jealous?"

  "{b}Chorus{/b}: Love is the lightless cave man walks down, blind to every stone in his path. Cut and bruised he can't see who assaults him, deeper in he goes, following only the promise of a soft-faced girl."

  "{b}Pasiphaë{/b}: Give me your bull, or I shall take it. You cannot keep a god's gift for yourself. It is I who have just as much right to it as you."

  "{b}Minos{/b}: I do not know you, I do not see. It is not one, but two wild creatures before me. Be you god, be you mortal, be you sorceress in between. Nothing of this is like the woman I wed. The one I wed is content with me."

  "{b}Pasiphaë{/b}: The one I wed, the one I see, slays the love within me."

if tutor:

  "Poseidon's curse here was insidious, it wasn't simply some bestial lust, it was an envy that grew and destroyed everything in its path."

  "Ultimately, Pasiphaë carries out a plan to lure the bull to her. As I expect, it goes terribly wrong."

  "She climbs into an ornately built wooden bull, made of mahogany, bedecked in jewels, and gambols and lolls with an actual bull on the stage."

  "The scene turns to horror, however, the real bull mounts the wooden bull."

  "Pasiphaë never acquires the bull, and its pursuit punishes her harshly. She holds up her bloodied child, the minotaur, her face contorting with joy, fear, and disgust as she dies."

  if pasiphae_author == "Marian":

    "I think about the implications of Marian having written this."

  jump pasiphae_author_menu

if merchant:

  "Ultimately, Pasiphaë carries out a plan to lure the bull to her, dressed as a bull."

  "Not the plan I'd have come up with, but I'm not the sorceress queen here, I suppose. Envy makes us do strange things."

  "The wooden bull she constructs is 'made of mahogany. Inlaid are sapphires around its neck, rubies on its hooves, a pearl on its forehead shaped like a crescent moon.'"

  "Kind of beautiful. Fairly impractical. Definitely out of budget for any theater that would play Greek plays, certainly."

  "Then of course was the trouble I'd seen from a mile away. The real bull... mounts the wooden cow."

  "The story ends in tragedy as she holds up her bloodied child, the minotaur, her face contorting with joy, fear, and disgust as she dies."

  "So what does this all mean?"

  if pasiphae_author == "Marian":

    "I think about the implications of Marian having written this."

  jump pasiphae_author_menu

if carpenter:

  "Ultimately, Pasiphaë carries out a plan to lure the bull to her, dressed as a bull."

  "The minotaur... the labyrinth... ah."

  "The wooden bull she constructs is 'made of mahogany. Inlaid are sapphires around its neck, rubies on its hooves, a pearl on its forehead shaped like a crescent moon.'"

  "Mahogany. Wow, what a heavy and expensive wood to be wheeling out onto the stage. Also not one that would have been available in Greece."

  "When Pasiphaë climbs in, the real bull... mounts the wooden cow."

  "The story ends in tragedy as she holds up her bloodied child, the minotaur, her face contorting with joy, fear, and disgust as she dies."

  "So what does this all mean?"

  if pasiphae_author == "Marian":

    "I think about the implications of Marian having written this."

  jump pasiphae_author_menu

label pasiphae_author_menu:

  menu:

    "This must be a fun and fanciful exercise of the mind":

      jump pasiphae_play_fun

    "This must be the product of a truly disturbed mind":

      jump pasiphae_play_mad

    "This must be something Marian had kept in secret" if pasiphae_author == "Marian":

      jump pasiphae_play_sympathy

label pasiphae_play_fun:

  "I imagine stagehands trying to wrestle a live bull onto a stage in a theater with a smirk."

  if pasiphae_author == "Marian":
    $ marian_play_fun = True

    "Literature was meant to explore ideas. I'm glad she had this outlet to express herself."

  else:
    "Literature was meant to explore ideas. I'm glad [pasiphae_author] was able to put this idea to paper."

  "Certainly, James is... was nothing like the characters in his books."

  "I put the book back in the drawer"

  jump conservatory_menu

label pasiphae_play_mad:

  "There is something deeply unsettling about rewriting an ancient play about bestiality."

  if pasiphae_author == "Marian":
    $ marian_play_crazy = True

    "What drew her to this story, and what made her want to express it in such graphic detail?"

    "Surely this is the work of someone who was truly unwell. I hope she got the help she needed."

  if pasiphae_author == "James":
    "James... some part of you must have been truly unwell. I can only hope that writing this helped bring you peace, or urged you to get the help you needed."

  else:
    "The author of this story must have been truly unwell. I can only hope that writing this helped bring them peace, or urged them to get the help they needed."

  "I put the book back in the drawer"

  jump conservatory_menu

label pasiphae_play_sympathy:

  $ marian_play_sympathy = True

  "It must have taken Marian a lot of courage to write something like this."

  "And to have to have hidden it in a such a place in their home, it's clear this was something she couldn't speak to James about."

  "Who was she? What spoke to her about this story, and how she told it? This human look at a woman with such a dark desire..."

  "Maybe writing this was some sort of exorcism."

  "I put the book back in the drawer"

  jump conservatory_menu

label study:

    scene study at truecenter

    "This is Jimmy's home within his home. If any room were a reflection of his mind, it would be this study."

    "I imagine him losing track of hours, days even, as he feverishly wrote his next great novel."

label study_menu:

    scene study at truecenter

    menu:

        "I see a large, imposing safe that looks like it hasn't been opened in ages" if not explored_study_safe:

            jump study_safe

        "I examine the mess upon the desk" if not explored_study_papers:

            jump study_papers

        "A picture catches my eye" if not explored_study_picture:

            jump study_pictures

        "There is an odd pipe on an end table" if not explored_study_check:

            jump study_check

        "I move on":

            jump bedroom

label study_check:

  $ explored_study_check = True

  "As I approach the end table, the musky, resin-y scent that had drifted through the upstairs hallway becomes clear."

  "This is a taricus pipe. I am shocked by the realization. More shocking, however, is the slip of paper I see next to the pipe."

  "It's a sunbleached check, signed and dated almost a year ago. Addressed to \"The Spiritual Seekers\", its sum makes my jaw drop."

if merchant or carpenter:

  "That name doesn't ring a bell. But it sounds pretty new-fangled. I say the words aloud. It smacks of alternative religion."

  jump study_check_choice

if tutor:

  "Something about this name sounds familiar. A translation pops into my head: \"Buscadoras Espirituales.\""

  "They were classified as a religious group, I believe. A few decades ago they made waves in Central America."

  "It appears they had made it to the English speaking world, but had yet to become popular."

  jump study_check_choice

label study_check_choice:

  "At the bottom of the check is the memo. It says, \"To help open the mind's journey to higher consciousness, YWH\""

  "I glance towards the taricus pipe nearby, and give a little sniff. I am to understand that these objects are likely related."

  "I double check the sum. James meant to donate a lifechanging amount of money to this organization."

  "Yet the check remains here, in James's study, unsent, for nearly a year."

  "I can't help but wonder, was it absentmindedness, or ambivalence?"

  "The paper between my fingers suddenly feels heavy."

label study_choice_menu:

  menu:

      "These \"Spiritual Seekers\"... they sound like a cult." if explored_study_check_cult == False:

          jump study_check_cult

      "People who smoke taricus are described as \"under the influence.\"" if explored_study_check_drugs == False:

          jump study_check_drugs

      "I am here to fulfill James's wishes." if explored_study_check_wishes == False:

          jump study_check_wishes

      "I have made my decision on what to do with this check.":

          jump study_check_choice_2

label study_check_cult:

  $ explored_study_check_cult = True

  "\"Spiritual Seekers\"? I bet the only thing they sought was a base of wealthy donors."

  "The mere thought of handing some new-age cult this sum of money is ridiculous."

  "Moreover, why would they even need money? If they sought the spiritual, wouldn't mortal currency merely be a distraction?"

  "I take a moment to breathe. Here I stand getting flustered over a piece of paper."

  "Perhaps I was making rash conclusions. This organization could be building homes, clothing the poor, purifying water."

  "Or maybe they simply threw hedonistic parties full of taricus."

  "I don't know the truth of this organization. What I know is that this was something important to Jimmy."

  "Seeing this check reminds me just how little I knew about Jimmy. What would have made Jimmy want to donate so much of his material wealth to this organization?"

  "To be part of something bigger... I've seen many people struggle to find meaning. Some found God, some volunteered."

  "Jimmy had made his mark in the world with his novels. Maybe he wanted to leave a different legacy."

  "I doubt I'll ever understand James's relationship with the \"Spiritual Seekers\" enough to know what purpose it served in his life."

  jump study_choice_menu

label study_check_drugs:

  $ explored_study_check_drugs = True

  "The movement against taricus and \"Taricus Madness\" was popular in my youth. I remember seeing movies and posters espousing its dangers."

  "I'd never smoke taricus myself, but I'd heard people who did became addicts. Under the influence, they hit and run, had hallucinations, and sometimes even killed themselves."

  "If this organization helped people \"open the mind's journey to higher consciousness\" with these drugs, I couldn't help but feel that it was my moral duty to... question this decision."

  "It was a possibility that these drugs had influenced Jimmy's faculties. Did he really want to donate such a large amount of money to this organization?"

  jump study_choice_menu

label study_check_wishes:

  $ explored_study_check_wishes = True

  "What Jimmy wanted to do with his money was Jimmy's business. I suppose if he wrote this check, then he'd presumably have wanted it sent, at some point."

  "If I could speak to him, and ask him if this was all sincerity, or all jokes... then maybe I'd have a clue about what to do with this check."

  "But I can't, so I don't."

  "And thinking about this all, this entire journey, I don't think my feelings on the matter are very relevant at all. All I can do is try and act in the most appropriate way."

  jump study_choice_menu

label study_check_choice_2:

  menu:

    "I place the check in an envelope and remind myself to put it in the mail later.":

      jump study_check_conclusion_mail

    "I leave the check where it is. Someone else can deal with it.":

      jump study_check_conclusion_leave

    "I tear the check up.":

      jump study_check_conclusion_tear

label study_check_conclusion_mail:

  "James Pryor, I am here as your appointed executor to carry out your wishes."

  "Though I feel a twinge of unease, I choose to believe that your choices will make the world a better place."

  jump study_check_conclusion

label study_check_conclusion_leave:

  "This is beyond my capabilities. Lawyers could spend months arguing Jimmy's intent in leaving a signed check unmailed."

  "There is no decision for me to make here, one way, or another. When the appropriate authorities can be present, they can decide what to do."

  jump study_check_conclusion

label study_check_conclusion_tear:

  "Jimmy, I am stopping you from making a grave mistake. Your legacy will remain intact."

  "I don't know what you were thinking in these last years, but I know that this is not you."

  jump study_check_conclusion

label study_check_conclusion:

  "Satisfied with my decision, I turn away from that heavy business and step away from the desk."

  jump study_menu

label study_safe:

    scene safe at truecenter

    $ explored_study_safe = True

    "The safe looks locked tight."

if carpenter:

    "This material is corroded, looks like it could collapse with just a good thwack..."

    jump study_safe_open

if merchant:

    "I bet there are a few release mechanisms somewhere though. Safes like these always have one."

    jump study_safe_open

if tutor:

    "Structurally, having something here, for this long would put stress on parts of the safe that could weaken its supports."

    jump study_safe_open

label study_safe_open:

    # Blackmail thing

    jump study_menu

label study_pictures:

    $ explored_study_picture = True

    # Memory with visit to Lintonbury with his brother who was left behind here

    jump study_menu

label study_papers:

    $ explored_study_papers = True

    "I find what I'd expect of Jimmy. A whirlwind of papers covered in varying levels of dust. A grand screed of ideas that span time and history, illegible scrolls of unfinished thoughts."

    "I am saddened when I understand that nobody will ever be able to piece this story together."

    "I fruitlessly rummage through Jimmy's mind. My fingers line up pages as if they'll fit together like a puzzle. There's a short story about a hunter and a harp. A few paragraphs about an installation he'd gone to at a museum, maybe a review? The papers are now in thorough disarray. There's a description of what he says is the last perfect peach he'll ever have."

    "I take this moment, then, to put this burden down. There will only ever be one Jimmy Pryor, and he is gone now."

    jump study_menu

label bedroom:

    scene bedroom at truecenter

    "It's quiet. No clocks ticking, no birds to be heard through the windows, the air is still. "

label bedroom_menu:

    menu:

        "I look at a piece of stationery on the bedstand" if not explored_bedroom_fanmail:

            jump bedroom_fanmail

        "I move on":

            return

label bedroom_fanmail:

    $ explored_bedroom_fanmail = True

    "There is a piece of blank stationery on James' bedstand. Next to it is a pen, and beside that, a yellowing book titled '22 Habits of the Well Informed.' Unmistakeably, there are the indents of penmanship on its cover."

    "I slide open the desk drawer in the bedstand. In it is revealed a crush of letters, all packed neatly against each other and stored in horizontal stacks."

    "I can't help but be amused by their various shapes and sizes. There are several slender white numbers, very classic. There are postcards from all over the country, the world, even. One envelope is pert and pink, closed with a heart sticker."

    "Stuffed at the end nearest to me seems to be a set. They are all beige squares, and their edges are quite worried. I could not tell if this was owing to their tendency to be crushed by the opening and closing of the drawer, or from frequent leafing. When I tip back the corner of the most askew envelope, I see a return address to 'Martin Fellows.'"

    "It seems in poor taste to paw through Jimmy's fanmail, but I can't help myself. I pick a letter out, making sure to turn another sideways to mark where it had come from."

    "It's dated several years ago. The handwriting is perfectly legible."

    "\"Dear Mr. Pryor,\""

    "\"Thank you for your letter. It is always such a pleasure to hear from you. I am a staunch believer that God only puts so many words in each of us. You surprise me time and time again with your generosity. I hope you are treating yourself well."

    "\"My inner Kurt came out again this week. I find it easier to spot him as time passes. It was when my daughter ran into my divorcée's arms. I knew she was growing up without me. But sometimes being a man means putting on a mask. It is not something I would know how to put words to were it not for your book. I would be lost in this experience."

    "\"I think things would have turned out differently for Kurt if he had kids. He would have protected them, no matter what. When he was found out, he would have dropped his \"Noble Charade\" to keep his family safe and moved to a little cabin in the woods."

    "\"That's what I think, at least. If that ends up in your next novel, leave me some credit would ya? I could use it.\""

    "\"Thanks a million, Martin Fellows\""

    jump bedroom_menu
