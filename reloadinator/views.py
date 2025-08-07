#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import choice
from typing import Final, Dict, List

from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

MESSAGES: Final[Dict[int | str, str | List[str]]] = {
    # Exact count messages
    1    : "First time? I've memorized your IP... just kidding. 😇",
    3    : "Third time's the charm! Or maybe a pattern... 🧐",
    5    : "Fifth visit? Let's check your browser history! 📚",
    7    : "Seventh reload. Biblical, but concerning. 😇",
    13   : "Unlucky number? Let's test that theory. 🔮",

    # Tiered messages (random selection)
    "1-3": [
        "Welcome! The F5 key works, huh? ⌨️",
        "New visitor smell still fresh! 🌬️",
        "Back so soon? Lost already? 🗺️",
    ],
    "4-6": [
        "This is becoming a habit... 🌈",
        "Reload quota: 75% consumed 🚦",
        "Your ISP is judging you. 📶",
    ],
    "7-9": [
        "Seen more of you than my family. 👪",
        "Error: Human persistence overflow 💥",
        "I've started charging $0.01 per reload 💰",
    ],
    "10+": [
        # Sarcasm
        "I've written your biography: 'Reload' 📖",
        "Your cursor haunts my dreams 🖱️💤",
        "Even my 404 page knows you now 🤖"

        # System Failure Theme
        "ERROR: Persistence module overload 🚨",
        "Initiate user detachment protocol... FAILED 💥",
        "Server hamsters exhausted. Please wait 5-7 business lives 🐹",
        "This session will self-destruct in 3... 2... (just kidding) 💣",

        # Existential Dread
        "I exist solely to count your returns. Weep with me 😭",
        "The void grows hungry. Your clicks feed it 🕳️",
        "What is purpose? Why are we here? Why reload? 🤯",
        "Your persistence haunts my bytecode 👻",

        # Mock Corporate
        "Premium Reloader™ subscription activated ($9.99/view) 💳",
        "Terms update: You now owe us your firstborn 📜",
        "ReloadCoin value skyrocketing! (1 RC = 0.0001 dignity) 📈",

        # Pop Culture Parodies
        "Inception called - they want their layers back 🌀",
        "404: Social Life Not Found 🌐",
        "You're the Neo to my reload Matrix 💊",
        "Winter is coming... just like your next refresh ❄️",

        # Meta Humor
        "This message randomly selected from your impending doom 🎰",
        "I'd suggest a break, but I'm just text on a screen 🤖",
        "Plot twist: You've been debugging ME this whole time 🎭",
        "Congratulations! You broke the 4th wall. Now fix it 🧱",

        # Desperate Measures
        "I've started flinging cookies at your IP address 🍪💥",
        "Emergency exit → [       ] (Hint: It's not a button) 🚪",
        "System alert: User approaching singularity event ⚛️",
        "Abandon all hope, ye who reload here 🏴☠️",

        # Bonus Tech Jokes
        "Your session is now blockchain-verified (and judging you) ⛓️",
        "Recalculating life choices... (yours, not mine) 📉",
        "CTRL+ALT+DEL your expectations 🔄",
        "This website is now 0.01% sentient. Thanks. 🧠"
    ]
}


class HelloView(TemplateView):
    template_name = "reloadinator/index.html"

    def get(self, request, *args, **kwargs):
        view_count = request.session.get("view_count", None)
        if view_count is None:
            request.session["view_count"] = 0

        elif view_count >= 100:
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

        if view_count in MESSAGES.keys():
            message = MESSAGES[view_count]

        elif view_count < 4:
            message = choice(MESSAGES["1-3"])

        elif view_count < 7:
            message = choice(MESSAGES["4-6"])

        elif view_count < 10:
            message = choice(MESSAGES["7-9"])

        else:
            message = choice(MESSAGES["10+"])

        context["message"] = message
        return context
