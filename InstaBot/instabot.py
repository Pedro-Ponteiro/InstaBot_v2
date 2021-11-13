from random import randint

import env
from instapy import InstaPy, smart_run


def main() -> None:

    username, pwd = env.get_login_pwd()
    session = InstaPy(username=username, password=pwd, headless_browser=True)
    with smart_run(session):

        # sleepyhead: wake up a little bit later in a randomly chosen time interval
        # stochastic_flow: can provide smooth peak value generation
        # notify_me: sends toast notifications (directly to your OS)

        session.set_quota_supervisor(
            enabled=True,
            sleep_after=["likes", "server_calls_h"],
            sleepyhead=True,
            stochastic_flow=True,
            notify_me=True,
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

        session.set_dont_like(env.get_dont_like())

        session.like_by_tags(env.get_tags(), amount=randint(40, 50))


if __name__ == "__main__":
    main()
