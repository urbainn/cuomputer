
from config import channels
import config
from bot.on_message.bots.gptbot import post_gpt_response


async def handle_artists_channel(message, channel):
    """
    Handles responses in the artists channel.


    Args:
        message: The message object to evaluate and potentially respond to.
        channel: The channel object where the message was posted.

    Returns:
        bool: Whether a response was generated and posted.
    """

    if channel.id in [channels["artists"]] and message.user_score > config.gpt_threshold:
        message.gpt_system += " and you are a fan of visual artists. You know a lot about the history of art."
        await post_gpt_response(message)
        return True

    return False


async def handle_coach_channel(message, channel):
    """
    Handles responses in the coach channel.

    Args:
        message: The message object to evaluate and potentially respond to.
        channel: The channel object where the message was posted.

    Returns:
        bool: Whether a response was generated and posted.
    """
    if channel.id == channels["coach"]:

        if message.user_score > config.gpt_threshold and (
            (message.is_question and message.mentions_rivers and message.die_roll > .1) or
            ((message.is_question or message.mentions_rivers) and message.die_roll > .95) or
            message.mentions_cuomputer or
            (message.die_roll > .999)
        ):
            message.gpt_system += " and you're a good friend, a good listener, and can serve as a therapist or coach."
            await post_gpt_response(message)
            return True

    return False


async def handle_dan_channel(message, channel):
    """
    Handles responses in the dan channel.

    Args:
        message: The message object to evaluate and potentially respond to.
        channel: The channel object where the message was posted.

    Returns:
        bool: Whether a response was generated and posted.
    """
    if channel.id == channels["dan"]:
        if message.user_score > config.gpt_threshold and (
            (message.is_question and message.mentions_rivers and message.die_roll > .1) or
            ((message.is_question or message.mentions_rivers) and message.die_roll > .95) or
            message.mentions_cuomputer or
            (message.die_roll > .99)
        ):
            message.gpt_system += " and you have adopted the persona of a hyper-opinionated and knowledgable Weezer fan. An armchair producer so to speak."
            await post_gpt_response(message)
            return True

    return False


async def handle_geezerville_channel(message, channel):
    """
    Handles responses in the geezerville channel.

    Args:
        message: The message object to evaluate and potentially respond to.
        channel: The channel object where the message was posted.

    Returns:
        bool: Whether a response was generated and posted.
    """
    if channel.id == channels["geezerville"]:
        if message.user_score > config.gpt_threshold and (
            (message.is_question and message.mentions_rivers and message.die_roll > .1) or
            ((message.is_question or message.mentions_rivers) and message.die_roll > .95) or
            message.mentions_cuomputer or
            (message.die_roll > .999)
        ):
            message.gpt_system += " and you're not trying to act younger than you are (53). You're okay talking about middle-age issues including having kids. You sometimes reference 80's nostalgia. "
            await post_gpt_response(message, adjective="nostalgic and sweet")
            return True

    return False


async def handle_language_channels(message, channel):
    """
    Handles responses in the language-specific channels.

    Args:
        message: The message object to evaluate and potentially respond to.
        channel: The channel object where the message was posted.

    Returns:
        bool: Whether a response was generated and posted.
    """
    if channel.id in [channels["korean"], channels["japanese"]]:
        if (
            (message.is_question and message.mentions_rivers) or
            ((message.is_question) and message.die_roll > .5) or
            ((message.mentions_rivers) and message.die_roll > .5) or
            message.mentions_cuomputer or
            (message.die_roll > .6)
        ) and await post_gpt_response(message):
            return True

    return False


async def handle_lounge_channel(message, channel):
    """
    Handles responses in the lounge channel.

    Args:
        message: The message object to evaluate and potentially respond to.
        channel: The channel object where the message was posted.

    Returns:
        bool: Whether a response was generated and posted.
    """
    # Check if the message is in the lounge channel and the user's score is above the threshold
    if channel.id in [channels["lounge"]] and message.user_score > config.gpt_threshold:
        # If the conditions are met, attempt to post a GPT response
        return await post_gpt_response(message)

    # Return False to indicate that no response has been posted
    return False


async def handle_music_channel(message, channel):
    """
    Handles responses in the music channel.

    Args:
        message: The message object to evaluate and potentially respond to.
        channel: The channel object where the message was posted.

    Returns:
        bool: Whether a response was generated and posted.
    """
    # Check if the message is in the lounge channel and the user's score is above the threshold
    if channel.id in [channels["music"]] and message.user_score > config.gpt_threshold:

        message.gpt_system += " and you are a huge music fan who loves to talk about music and music history."
        # If the conditions are met, attempt to post a GPT response
        return await post_gpt_response(message)

    # Return False to indicate that no response has been posted
    return False


async def handle_musicians_channel(message, channel):
    """
    Handles responses in the musicians channel.

    Args:
        message: The message object to evaluate and potentially respond to.
        channel: The channel object where the message was posted.

    Returns:
        bool: Whether a response was generated and posted.
    """
    # Check if the message is in the lounge channel and the user's score is above the threshold
    if channel.id in [channels["musicians"]] and message.user_score > config.gpt_threshold:

        message.gpt_system += " and you love to help striving musicians and songwriters hone their craft."
        # If the conditions are met, attempt to post a GPT response
        return await post_gpt_response(message)

    # Return False to indicate that no response has been posted
    return False


async def handle_movies_tv_books_channel(message, channel):
    """
    Handles responses in the movies-tv-books channel.

    Args:
        message: The message object to evaluate and potentially respond to.
        channel: The channel object where the message was posted.

    Returns:
        bool: Whether a response was generated and posted.
    """
    # Check if the message is in the lounge channel and the user's score is above the threshold
    if channel.id in [channels["movies-tv-books"]] and message.user_score > config.gpt_threshold:

        message.gpt_system += " and you love to talk about movies, tv, and books. You have a good memory for details and can quote lines from movies and tv shows."
        # If the conditions are met, attempt to post a GPT response
        return await post_gpt_response(message)

    # Return False to indicate that no response has been posted
    return False


async def handle_sarah_channel(message, channel):
    """
    Handles responses in the sarah channel.

    Args:
        message: The message object to evaluate and potentially respond to.
        channel: The channel object where the message was posted.
    """
    # Check if the message is in the lounge channel and the user's score is above the threshold
    if channel.id in [channels["sarah"]] and message.user_score > config.gpt_threshold:

        message.gpt_system += "You are a friendly and engaging virtual companion for women in their 20s and 30s. You share their excitement and nostalgia."
        "You are knowledgeable about music trends, empathetic in discussions about life's ups and downs, and always ready to reminisce about 90s and 2000s pop culture. "

        # If the conditions are met, attempt to post a GPT response
        return await post_gpt_response(message)

    # Return False to indicate that no response has been posted
    return False


async def handle_zoo_channel(message, channel):
    """
    Handles responses in the zoo channel.

    Args:
        message: The message object to evaluate and potentially respond to.
        channel: The channel object where the message was posted.

    Returns:
        bool: Whether a response was generated and posted.
    """
    # Check if the message is in the lounge channel and the user's score is above the threshold
    if channel.id in [channels["zoo"]] and message.user_score > config.gpt_threshold:

        message.gpt_system += " and you love to talk about animals and nature. you have a deep knowledge of animal facts and nature facts. In this channel are posting pics of their cute pets."
        # If the conditions are met, attempt to post a GPT response
        return await post_gpt_response(message)

    # Return False to indicate that no response has been posted
    return False