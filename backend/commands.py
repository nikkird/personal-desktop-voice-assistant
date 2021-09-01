from backend import desk_automate, automate, mail, today, stt


def get_commands(tag, query):
    if 'wikipedia' == tag:
        automate.call_wiki(query)
        return True

    elif 'youtube_query' == tag:
        automate.open_youtube(query)
        return True

    elif 'songs' == tag:
        automate.play_songs(query)

    elif 'songs_command' == tag:
        automate.play_songs(query)

    elif 'google' == tag:
        automate.open_google(query)
        return True

    elif 'open_sites' == tag:
        automate.open_sites(query)

    elif 'mail' == tag:
        mail.send_email()

    elif 'joke' == tag:
        automate.get_jokes()

    elif 'maps' == tag:
        automate.get_maps(query)

    elif 'write_note' == tag:
        automate.write_notes()

    elif 'get_note' == tag:
        automate.get_notes()

    elif 'launch_app' == tag:
        desk_automate.launch_app(query)

    elif 'close_app' == tag:
        desk_automate.close_app(query)

    elif 'empty_recycle_bin' in query:
        desk_automate.empty_bin()

    elif 'wolfram' == tag:
        automate.call_wolframalpha(query)

    elif 'weather' == tag:
        automate.get_weather()

    elif 'get_news' == tag:
        automate.get_news()

    elif 'pronounce' == tag:
        desk_automate.get_pronunciation()

    elif 'time' == tag:
        print("yes")
        today.call_time()
        return True

    elif 'date' == tag:
        print("yes")
        today.date_today()
        return True

    elif 'month' == tag:
        print("yes")
        today.call_month()
        return True

    elif 'day' == tag:
        print("yes")
        today.call_day()

    elif 'holiday_today' == tag:
        today.is_holiday()

    elif 'goodbye' == tag:
        quit()

    else:
        pass
