from random import randint

from instapy import InstaPy, smart_run

import env
import env_secrets


def main() -> None:

    username, pwd = env_secrets.get_login_pwd()
    session = InstaPy(username=username, password=pwd)
    with smart_run(session):
        session.set_quota_supervisor(
            enabled=True,
            sleep_after=["likes", "server_calls_h"],
            sleepyhead=True,  # can help to sound more humanly which will wake up a little bit later in a randomly chosen time interval around accurate wake up time
            stochastic_flow=True,  # can provide smooth peak value generation by your original values
            notify_me=True,  #  sends toast notifications (directly to your OS) about the important states of supervisor- sleep, wake up and exit messages
            peak_likes_hourly=57,
            peak_likes_daily=585,
            peak_server_calls_hourly=None,
            peak_server_calls_daily=4700,
        )

        # like config
        session.set_mandatory_language(enabled=True, character_set=["LATIN"])
        session.set_relationship_bounds(
            enabled=True, min_posts=3, min_followers=25, min_following=25
        )

        session.set_mandatory_words(env.get_mandatory_words())

        session.set_dont_like(
            ["india", "hot", "girl"]
        )  # my preferences because 1: I don't plan to work in India 2: I have a girlfriend

        session.like_by_tags(env.get_tags(), amount=randint(80, 100))


if __name__ == "__main__":
    main()
