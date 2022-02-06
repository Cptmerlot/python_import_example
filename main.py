from discord.server import create_client
from discord import create_client as create_client2


def main():
    c = create_client()
    print(c)

    # this works as well
    c = create_client2()
    print(c)

main()