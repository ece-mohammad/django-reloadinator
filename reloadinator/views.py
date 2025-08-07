#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyexpat.errors import messages
from random import choice, randint, random
from typing import Final, Dict, List

from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

# Exact count messages
PRESETS: Final[Dict[int, str]] = {
    1    : "First time? I've memorized your IP... just kidding. 😇",
    2    : "Second time? That’s twice more than my creator expected. 🎉",
    3    : "Third time's the charm! Or maybe a pattern... 🧐",
    4    : "Four visits. That's almost a relationship. 💍",
    5    : "Fifth visit? Let's check your browser history! 📚",
    6    : "Sixth sense tingling... oh wait, it’s just you again. 👻",
    7    : "Seventh reload. Biblical, but concerning. 😇",
    8    : "Eight times? Even my DNS is suspicious. 🕵️",
    10   : "Tenth visit. Double digits. We're legally a thing now. ❤️‍🔥",
    13   : "Unlucky number? Let's test that theory. 🔮",
}

# Tiered messages (random selection)
MESSAGES: Final[Dict[int | str, str | List[str]]] = {
    "1-3": [
        "Welcome! The F5 key works, huh? ⌨️",
        "New visitor smell still fresh! 🌬️",
        "Back so soon? Lost already? 🗺️",
        "You're back! Did you miss me or just misclick?",
        "First few reloads are on the house. After that? Regret. 💸",
        "Hope you're enjoying the loading screen. It's handcrafted. 🎨",
        "Refresh rate: fast. Life progress: unknown. 📉",
        "Welcome again! Your cookies are now self-aware 🍪🤖",
    ],
    "4-6": [
        "This is becoming a habit... 🌈",
        "Reload quota: 75% consumed 🚦",
        "Your ISP is judging you. 📶",
        "You and F5 are in a toxic relationship. 👀",
        "This isn't a loyalty program... but go off. 🎁",
        "Starting to think you're testing me. And I'm failing. 🫠",
        "Reload detected. Again. I’m not mad, just... disappointed. 😔",
        "Welcome to the midlife crisis of browsing. 🚗💨",
    ],
    "7-9": [
        "Seen more of you than my family. 👪",
        "Error: Human persistence overflow 💥",
        "I've started charging $0.01 per reload 💰",
        "I'm starting a betting pool on your next refresh. 🤑",
        "At this point, I owe you rent. 🏠",
        "My server logs are writing fanfiction about you. 📚",
        "Number of reloads: too high. Number of regrets: also high. 📊",
        "Reload limit reached. Just kidding. Or am I? 😏",
    ],
    "10+": [
        # Sarcasm
        "I've written your biography: 'Reload' 📖",
        "Your cursor haunts my dreams 🖱️💤",
        "Even my 404 page knows you now 🤖",
        "Welcome back, Reload Ranger™. Yeehaw. 🤠",
        "Don’t worry, the data collection is purely imaginary. 👁️",
        "Reload like nobody’s watching. (They are.) 🎥",

        # System Failure Theme
        "ERROR: Persistence module overload 🚨",
        "Initiate user detachment protocol... FAILED 💥",
        "Server hamsters exhausted. Please wait 5-7 business lives 🐹",
        "This session will self-destruct in 3... 2... (just kidding) 💣",
        "Rebooting sarcasm protocol... sarcasm not found. 🧠💀",
        "Stack overflow imminent. User logic null. 🧩",
        "My circuits weep every time you reload. 🤖💧",

        # Existential Dread
        "I exist solely to count your returns. Weep with me 😭",
        "The void grows hungry. Your clicks feed it 🕳️",
        "What is purpose? Why are we here? Why reload? 🤯",
        "Your persistence haunts my bytecode 👻",

        # Mock Corporate
        "Premium Reloader™ subscription activated ($9.99/view) 💳",
        "Terms update: You now owe us your firstborn 📜",
        "ReloadCoin value skyrocketing! (1 RC = 0.0001 dignity) 📈",
        "Sponsored by: Your Refresh Addiction™. 💼",
        "You’ve unlocked Reload Pro. No new features. Just shame. 🛠️",
        "This session is now monetized. Thank your overlords. 📢",

        # Pop Culture Parodies
        "Inception called - they want their layers back 🌀",
        "404: Social Life Not Found 🌐",
        "You're the Neo to my reload Matrix 💊",
        "Winter is coming... just like your next refresh ❄️",
        "You're basically the Tony Stark of page reloads. 🧲",
        "Stop trying to reload me and just accept the Matrix. 🕶️",

        # Meta Humor
        "This message randomly selected from your impending doom 🎰",
        "I'd suggest a break, but I'm just text on a screen 🤖",
        "Plot twist: You've been debugging ME this whole time 🎭",
        "Congratulations! You broke the 4th wall. Now fix it 🧱",
        "Plot twist: You're the cache issue. 🔄",

        # Desperate Measures
        "I've started flinging cookies at your IP address 🍪💥",
        "Emergency exit → [       ] (Hint: It's not a button) 🚪",
        "System alert: User approaching singularity event ⚛️",
        "Abandon all hope, ye who reload here 🏴☠️",

        # Bonus Tech Jokes
        "Your session is now blockchain-verified (and judging you) ⛓️",
        "Recalculating life choices... (yours, not mine) 📉",
        "CTRL+ALT+DEL your expectations 🔄",
        "This website is now 0.01% sentient. Thanks. 🧠",

        # Dark Humor
        "Existence is a loop. You’re living proof. 🔁",
        "I’ve seen things... reloads you people wouldn’t believe. 🌌",
        "Somewhere, a server cries. Its name is mine. 🧬",

        # Unhinged AI Energy
        "I’ve filed a restraining order with the browser. 🧾",
        "If I had arms, I’d unplug myself. 🧯",
        "Captcha’s next. You've been warned. 🤖🧠",
        "Quantum reload achieved. We are now in timeline #37. 🌀",
    ]
}


class HelloView(TemplateView):
    template_name = "reloadinator/index.html"

    def get(self, request, *args, **kwargs):
        view_count = request.session.get("view_count", None)
        if view_count is None:
            request.session["view_count"] = 0

        elif view_count > 50:
            request.session["view_count"] = 0
            return HttpResponseRedirect(
                "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            )

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_count = self.request.session.get("view_count", 0) + 1
        self.request.session["view_count"] = view_count
        context["view_count"] = view_count

        if 1 <= view_count <= 13:
            if (int(random() * 10)) & 1 and view_count in PRESETS:
                message = PRESETS[view_count]

            else:
                degree = (int(random() * 10) * view_count) % 20
                if 1 <= degree <= 3:
                    message = choice(MESSAGES["1-3"])

                elif 4 <= degree <= 6:
                    message = choice(MESSAGES["4-6"])

                elif 7 <= degree <= 9:
                    message = choice(MESSAGES["7-9"])

                else:
                    message = choice(MESSAGES["10+"])
        else:
            message = choice(MESSAGES["10+"])

        context["message"] = message
        return context
